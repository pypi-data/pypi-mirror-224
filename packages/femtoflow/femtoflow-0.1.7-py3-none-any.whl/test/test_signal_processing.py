import tensorflow as tf
import os
import numpy as np
from parameterized import parameterized
from femtoflow.layers.signal_processing import CartesianMagnitudeModel, MelTransformModel
from femtoflow.quantization.quantize_tflite import TFLiteModelWrapper
from scipy.signal import stft


"""
Magnitude layer Tests
"""

def test_cartesian_magnitude_layer():
    """Test the CartesianMagnitudeModel layer for correct computation."""

    input_re = np.random.randn(32, 100, 256)  # Real component, shape (B, SEQ_LEN, DIM)
    input_im = np.random.randn(32, 100, 256)  # Imaginary component, shape (B, SEQ_LEN, DIM)

    # Using the custom CartesianMagnitudeLayer
    custom_mag_layer = CartesianMagnitudeModel(feat_dim=None, batch_size=None, time_steps=None)

    input_dict = {'real': input_re, 'imag': input_im}
    output_dict = custom_mag_layer(input_dict)

    custom_mag = output_dict['op']

    # Using the built-in TensorFlow complex number support
    complex_number = tf.complex(input_re, input_im)
    tf_mag = tf.abs(complex_number)

    # Compare the results using np.allclose() with specified tolerances
    atol = 1e-6  # Absolute tolerance
    rtol = 1e-6  # Relative tolerance
    assert np.allclose(custom_mag.numpy(), tf_mag.numpy(), atol=atol, rtol=rtol)


def test_cartesian_magnitude_tflite():
    """Test the CartesianMagnitudeModel layer in the TFLite model for correct computation."""

    batch_size = 2
    time_steps = 2
    feat_dim = 256

    model = CartesianMagnitudeModel(feat_dim=feat_dim, batch_size=batch_size, time_steps=time_steps)

    def representative_data_gen(num_samples=5):
        for i in range(num_samples):
            # Model has only one input so each data point has one element.
            yield {'real': np.random.randn(batch_size, time_steps, feat_dim).astype(np.float32),
                   'imag': np.random.randn(batch_size, time_steps, feat_dim).astype(np.float32)}

    tflite_save_path = 'tflite_cart_magnitude.tflite'
    tflite_model = TFLiteModelWrapper(quantize_mode='8x8',
                                      model=model,
                                      representative_dataset=representative_data_gen,
                                      tflite_save_path=tflite_save_path)

    # Confirm TFLite VS TF output are similar
    for i, data in enumerate(representative_data_gen(num_samples=5)):
        out_tf = model(data)['op']
        out_tflite = tflite_model(data)['op']

        # Calculate the RMSE
        rmse = np.sqrt(np.mean((out_tf - out_tflite)**2))

        tolerance = 0.2
        assert rmse < tolerance


"""
MelFbank layer Tests
"""
import numpy as np

def test_meltransform_tflite():
    """Test the MelTransformModel layer in the TFLite model for correct computation."""

    batch_size = 1
    n_fft = 512
    n_mels = 64
    sr = 16000  # sampling frequency

    model = MelTransformModel(sr=sr, n_fft=n_fft, n_mels=n_mels, batch_size=batch_size)

    def representative_data_gen(num_samples=20):
        for _ in range(num_samples):  

            sequence_length = int(np.random.uniform(1.0, 3.0) * sr)
            # Create time values for the sine wave
            time = np.linspace(0., 1., sequence_length, False)
            # Create a sine wave
            signal = np.sin(1.0 * 2.0 * np.pi * sr * time) + np.sin(1.5 * 2.0 * np.pi * sr * time)
            # Apply STFT to the signal to get the spectrogram
            _, _, spectrogram = stft(signal, fs=sr, nfft=n_fft)
            # Only take the magnitude (abs) of the spectrogram and add batch dimension
            power_spec = np.abs(spectrogram)[np.newaxis, ...]
            permuted_power_spec = np.transpose(power_spec, (0, 2, 1)) # B, Seq_len, n_fft//2 + 1
            yield {'ip': permuted_power_spec.astype(np.float32)}

    tflite_save_path = 'tflite_fbank.tflite'
    tflite_model = TFLiteModelWrapper(quantize_mode='8x16',
                                      model=model,
                                      representative_dataset=representative_data_gen,
                                      tflite_save_path=tflite_save_path)

    # Confirm TFLite VS TF output are similar
    for i, data in enumerate(representative_data_gen(num_samples=5)):
        out_tf = model(data)['op']
        out_tflite = tflite_model(data)['op']

        # Calculate the RMSE
        rmse = np.sqrt(np.mean((out_tf - out_tflite)**2))

        tolerance = 0.005
        assert rmse < tolerance
