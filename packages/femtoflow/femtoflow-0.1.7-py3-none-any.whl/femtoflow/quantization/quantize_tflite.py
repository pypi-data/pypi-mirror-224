"""
TFLite Utilities Related Files, for converting a Tensorflow to TFLite Quantized Model 
"""
import tensorflow as tf
import numpy as np
import tempfile
from typing import Dict, Union, Callable
from abc import ABC, abstractmethod

# Setup Logging
import logging
logging.basicConfig(level=logging.INFO)


class TFLiteUtils:
    """
    Provides utility methods for quantization-related operations during TFLite model 
    conversion and inference.
    """

    @staticmethod
    def quantize_input_tensor(x: Union[np.ndarray, tf.Tensor], runner, name: str) -> np.ndarray:
        """
        Quantizes an input tensor from float to int using metadata from the TFLite
        SignatureRunner.

        Args:
            x (Union[np.ndarray, tf.Tensor]): Unquantized tensor.
            runner: TFLite SignatureRunner instance.
            name (str): The name of the tensor corresponding to `x`.

        Returns:
            np.ndarray: The quantized tensor.
        """
        details = runner.get_input_details()[name]
        scale, zero_point = details['quantization']
        return np.round(np.array(x, dtype=float) / scale) + zero_point

    @staticmethod
    def dequantize_output_tensor(x: Union[np.ndarray, tf.Tensor], runner, name: str) -> np.ndarray:
        """
        Dequantizes an output tensor back to a float using metadata from the TFLite
        SignatureRunner.

        Args:
            x (Union[np.ndarray, tf.Tensor]): Quantized tensor.
            runner: TFLite SignatureRunner instance.
            name (str): The name of the tensor corresponding to `x`.

        Returns:
            np.ndarray: The dequantized tensor.
        """
        details = runner.get_output_details()[name]
        scale, zero_point = details['quantization']
        return scale * (np.array(x, dtype=float) - zero_point)

    @staticmethod
    def quantized_predict(interpreter: tf.lite.Interpreter, signature_name: str,
                           inputs:Dict[str, np.ndarray], predict_fn: Callable) -> Dict[str, np.ndarray]:
        """
        Performs prediction for quantized models. Can be used for TFLite inference,
        depending on the provided `predict_fn`. This method is used during inference
        to process sequences.

        Args:
            interpreter (tf.lite.Interpreter): TFLite Interpreter instance.
            signature_name (str): Name of the signature to use for inference.
            inputs (Dict[str, np.ndarray]): Dictionary of input tensor names and their corresponding arrays.
            predict_fn (Callable): Lambda function that performs a forward pass on quantized inputs.

        Returns:
            Dict[str, np.ndarray]: Dictionary of the predicted dequantized output tensor names and their corresponding arrays.
        """
        # Quantize inputs
        np_dtype = interpreter.get_input_details()[0]['dtype']
        runner = interpreter.get_signature_runner(signature_name)
        quantized_inputs = {name: TFLiteUtils.quantize_input_tensor(value, runner, name).astype(np_dtype) for name, value in inputs.items()} 
        
        # Predict
        quantized_outputs = predict_fn(quantized_inputs)
        dequantized_output = {key: TFLiteUtils.dequantize_output_tensor(value,
                                                                    runner,
                                                                    key).squeeze()
                                                for key, value in quantized_outputs.items()}
        # Dequantize outputs
        return dequantized_output


class TFLiteModelBase(ABC):
    """
    Base class for generating quantized TFLite models from TensorFlow models and performing inference
    using the quantized TFLite models. This is an abstract class that must be subclassed by concrete
    classes for specific quantization types.
    """

    def __init__(self, model: Union[tf.keras.Model, 
                                    tf.keras.Sequential], 
                       representative_dataset: Callable, 
                       tflite_save_path: str,
                       signature_name: str='serving_default') -> None:
        """
        Initializes the TFLiteModelBase instance.

        Args:
            model (Union[tf.keras.Model, tf.keras.Sequential]): The TensorFlow model to be converted.
            representative_dataset (Callable): A callable that produces representative data samples
                used for calibration during quantization.
            tflite_save_path (str): Path where the converted TFLite model will be saved.
            signature_name (str, optional): The name of the signature to be used for inference.
                Defaults to 'serving_default'.

        Note:
            1) The inputs to the model are expected to be in dictionary format, i.e.
                {'foo_ip': tf.Tensor(..), 'foo_ip_two': tf.Tensor(..)}
               The outputs will also be a dictionary, of the format
                {'foo_op_name': output_tensor_one, 'foo_op_name_two': output_tensor_two}

            2) For models with multiple inputs or outputs, it is recommended to supply a model
                of type `tf.keras.Model(inputs=inputs, outputs=outputs)` with the input/output
                names and shapes explicitly defined. The model should also have `model.input_spec`
                defined. There could be TFLite conversion errors if the inputs/outputs aren't
                explicitly defined.
        """
        self.flatbuffer = self.generate_tflite_flatbuffer(model=model,
                                                          representative_dataset=representative_dataset)

        # Save the TFLite Flatbuffer to a TFLite file
        self.save_tflite_model(tflite_flatbuffer=self.flatbuffer, tflite_save_path=tflite_save_path)


        self.interpreter = tf.lite.Interpreter(model_content=self.flatbuffer)

        self.signature_name = signature_name
        self.runner = self.interpreter.get_signature_runner(self.signature_name)

        self.input_details = self.runner.get_input_details()
        self.output_details = self.runner.get_output_details()

        self.tflite_pred_fn = lambda inputs: TFLiteUtils.quantized_predict(interpreter=self.interpreter,
                                                                            signature_name=self.signature_name,
                                                                            inputs=inputs,
                                                                            predict_fn=lambda quantized_inputs: self.runner(**quantized_inputs))

    def save_tflite_model(self, tflite_flatbuffer: bytes, tflite_save_path: str):
        """
        Saves the TFLite model to the specified path.

        Args:
            tflite_flatbuffer (bytes): The TFLite binary flatbuffer to be saved.
            tflite_save_path (str): Path where the TFLite model will be saved.
        """
        with open(tflite_save_path, 'wb') as f:
            f.write(tflite_flatbuffer)

    @abstractmethod
    def generate_tflite_flatbuffer(self, model: Union[tf.keras.Model, 
                                               tf.keras.Sequential], 
                                  representative_dataset: Callable) -> bytes:
        """
        Generates the TFLite binary flatbuffer for the given TensorFlow model.
        This method must be implemented by subclasses of TFLiteModelBase.

        Args:
            model (Union[tf.keras.Model, tf.keras.Sequential]): The TensorFlow model to be converted.
            representative_dataset (Callable): A callable that produces representative data samples
                used for calibration during quantization.

        Returns:
            bytes: The TFLite binary flatbuffer.

        Raises:
            Exception: If the method is not implemented by the subclass.
        """
        raise Exception(f"ERR: Method `generate_tflite_flatbuffer` needs to be implemented by Subclass")

    def __call__(self, inputs: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Performs a quantized forward pass using the TFLite model.

        Args:
            inputs (Dict[str, np.ndarray]): A dictionary of unquantized inputs.

        Returns:
            Dict[str, np.ndarray]: A dictionary of unquantized outputs.
        """
        output = self.tflite_pred_fn(inputs)
        return output

class TFLiteModelInt8(TFLiteModelBase):
    """
    Int 8 Activations, Int 8 Weights
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate_tflite_flatbuffer(self, model: Union[tf.keras.Model, 
                                                tf.keras.Sequential], 
                                    representative_dataset: Callable) -> bytes:
        """
        Converts a TensorFlow model into its TFLite equivalent with INT-8 quantization for both
        weights and activations. Returns the converted TFLite model flatbuffer.

        Args:
            model (Union[tf.keras.Model, tf.keras.Sequential]): The TensorFlow model to be converted.
            representative_dataset (Callable): A callable that produces representative data samples
                used for calibration during quantization.

        Returns:
            bytes: The TFLite binary flatbuffer.

        Raises:
            AssertionError: If the model input specifications are not defined.
        """
        assert model.input_spec is not None, "model.input_spec() was None. Expected to be Defined. \
                                                Please define explicit Input/Output Signatures to your model using \
                                                tf.keras.Model(inputs=inputs, outputs=outputs)"
        ip_shapes = [tf.TensorSpec(shape=x.shape, name=x.name) for x in model.input_spec]
        with tempfile.TemporaryDirectory() as dirname: 

            run_model = tf.function(lambda x: model(x))

            concrete_func = run_model.get_concrete_function(ip_shapes)
            model.save(dirname, save_format="tf", signatures=concrete_func)

            tf_dtype = tf.int8
            converter = tf.lite.TFLiteConverter.from_saved_model(dirname)
            converter.inference_input_type = tf_dtype 
            converter.inference_output_type = tf_dtype
            converter.optimizations = [tf.lite.Optimize.DEFAULT]
            converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]

            converter.representative_dataset = representative_dataset

            # Convert the inference model to TFLite
            logging.info("Converting TF model to TFLite 8x8...")
            tflite_model = converter.convert()
        
        return tflite_model


class TFLiteModelInt16(TFLiteModelBase):
    """
    Int 16 Activations, Int 8 Weights
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def generate_tflite_flatbuffer(self, model: Union[tf.keras.Model, 
                                                tf.keras.Sequential], 
                                    representative_dataset: Callable) -> bytes:
        """
        Converts a TensorFlow model into its TFLite equivalent with INT-16 quantization for activations
        and INT-8 quantization for weights. Returns the converted TFLite model flatbuffer.

        Args:
            model (Union[tf.keras.Model, tf.keras.Sequential]): The TensorFlow model to be converted.
            representative_dataset (Callable): A callable that produces representative data samples
                used for calibration during quantization.

        Returns:
            bytes: The TFLite binary flatbuffer.

        Raises:
            AssertionError: If the model input specifications are not defined.
        """
        assert model.input_spec is not None, "model.input_spec() was None. Expected to be Defined. \
                                              Please define explicit Input/Output Signatures to your model using \
                                              tf.keras.Model(inputs=inputs, outputs=outputs)"
        ip_shapes = [tf.TensorSpec(shape=x.shape, name=x.name) for x in model.input_spec]
        with tempfile.TemporaryDirectory() as dirname: 

            run_model = tf.function(lambda x: model(x))

            concrete_func = run_model.get_concrete_function(ip_shapes)
            model.save(dirname, save_format="tf", signatures=concrete_func)

            tf_dtype = tf.int16
            converter = tf.lite.TFLiteConverter.from_saved_model(dirname)
            converter.inference_input_type = tf_dtype 
            converter.inference_output_type = tf_dtype
            converter.optimizations = [tf.lite.Optimize.DEFAULT]
            converter.target_spec.supported_ops = [tf.lite.OpsSet.EXPERIMENTAL_TFLITE_BUILTINS_ACTIVATIONS_INT16_WEIGHTS_INT8]

            converter.representative_dataset = representative_dataset

            # Convert the inference model to TFLite
            logging.info("Converting TF model to TFLite 8x16...")
            tflite_model = converter.convert()
        
        return tflite_model


class TFLiteModelWrapper:

    def __init__(self, quantize_mode: str, 
                       model: Union[tf.keras.Model, 
                                    tf.keras.Sequential], 
                       representative_dataset: Callable, 
                       tflite_save_path: str,
                       signature_name: str='serving_default'):
        """
        Initializes the TFLiteModelWrapper instance.

        Args:
            quantize_mode (str): The quantization mode to use. Supported values are '8x16' and '8x8'.
                8x16 quantizes the model to INT-8 Weights and INT-16 Activations
                8x8 quantizes the model to INT-8 Weights and INT-8 Activations
            model (Union[tf.keras.Model, tf.keras.Sequential]): The TensorFlow model to be converted.
            representative_dataset (Callable): A callable that produces representative data samples
                used for calibration during quantization.
            tflite_save_path (str): Path where the converted TFLite model will be saved.
            signature_name (str, optional): The name of the signature to be used for inference.
                Defaults to 'serving_default'.

        Raises:
            AssertionError: If the specified quantization mode is not supported.
        """
        assert quantize_mode in ('8x16', '8x8'), f"ERR: Invalid Quant Mode. Supported: ('8x16', '8x8')"
        self.model_cls_map = {'8x16': TFLiteModelInt16, '8x8': TFLiteModelInt8}
        self.instance = self.model_cls_map[quantize_mode](model=model, representative_dataset=representative_dataset,
                                                          tflite_save_path=tflite_save_path, signature_name=signature_name)

    def __call__(self, inputs: Dict[str, np.ndarray]) -> Dict[str, np.ndarray]:
        """
        Performs a quantized forward pass using the TFLite model.

        Args:
            inputs (Dict[str, np.ndarray]): A dictionary of unquantized inputs.

        Returns:
            Dict[str, np.ndarray]: A dictionary of unquantized outputs.
        """
        return self.instance.__call__(inputs)