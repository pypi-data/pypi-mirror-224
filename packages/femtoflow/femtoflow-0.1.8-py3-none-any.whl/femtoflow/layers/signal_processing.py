"""
Signal Processing Layers Utilities
"""

import tensorflow as tf
import numpy as np
import tensorflow_model_optimization as tfmot
from typing import Union, List, Callable, Any, Tuple

# Setup Logging
import logging
logging.basicConfig(level=logging.INFO)

import tensorflow as tf
from python_speech_features.base import get_filterbanks


"""
Cartesian Magnitude Layer
"""

class CartesianMagnitudeLayer(tf.keras.layers.Layer):
    """Custom layer for computing the Cartesian magnitude of complex numbers."""

    def call(self, inputs):
        """Compute the Cartesian magnitude.

        Args:
            inputs: A tuple containing the real and imaginary components of the complex numbers.

        Returns:
            The Cartesian magnitude of the complex numbers.
        """
        re, im = inputs

        r = tf.abs(re)
        i = tf.abs(im)
        a = tf.math.maximum(r, i)
        b = tf.math.minimum(r, i)

        eps = b / a
        mag = a * tf.sqrt(1 + eps**2)

        return mag


def CartesianMagnitudeModel(feat_dim=None, batch_size=None, time_steps=None, real_ip_name='real', imag_ip_name='imag', output_name='op'):
    """Create a model for computing the Cartesian magnitude of complex numbers.

    Args:
        feat_dim: The dimensionality of the input features.
        batch_size: The batch size of the input data.
        time_steps: The number of time steps in the input data.
        real_ip_name: The name of the input layer for the real component.
        imag_ip_name: The name of the input layer for the imaginary component.
        output_name: The name of the output layer.

    Returns:
        A Keras model for computing the Cartesian magnitude.
    """
    real_ip = tf.keras.Input(batch_size=batch_size, shape=(time_steps, feat_dim), name=real_ip_name)
    imag_ip = tf.keras.Input(batch_size=batch_size, shape=(time_steps, feat_dim), name=imag_ip_name)

    inputs = [real_ip, imag_ip]

    output = CartesianMagnitudeLayer()(inputs)

    output_dict = {output_name: output}

    model = tf.keras.Model(inputs=inputs, outputs=output_dict)
    return model



"""
MelFrontend
"""

class MelTransformLayer(tf.keras.layers.Layer):
    """Custom layer for computing mel filterbank coefficients."""

    def __init__(self, sr, n_fft, n_mels, fmin=0.0, fmax=None):
        """Initialize the MelFrontendLayer.

        Args:
            sr: The audio sampling rate (in Hz).
            n_fft: The number of FFT frequencies.
            n_mels: The number of mel frequencies to create.
            fmin: The minimum frequency (in Hz).
            fmax: The maximum frequency (in Hz). If not provided, the Nyquist frequency will be used.

        """
        super(MelTransformLayer, self).__init__()
        mel_matrix = self.get_mel_matrix(sr, n_fft, n_mels, fmin, fmax)
        self.weight = tf.Variable(mel_matrix.T, trainable=False, dtype=tf.float32)

    @staticmethod
    def get_mel_matrix(sr, n_dft, n_mels=128, fmin=0.0, fmax=None, **kwargs):
        """Get the mel filterbank matrix.

        Args:
            sr: The audio sampling rate (in Hz).
            n_dft: The number of DFT frequencies.
            n_mels: The number of mel frequencies to create.
            fmin: The minimum frequency (in Hz).
            fmax: The maximum frequency (in Hz). If not provided, the Nyquist frequency will be used.
            kwargs: Additional arguments to pass to `get_filterbanks`.

        Returns:
            The mel filterbank matrix.

        """
        mel_matrix = get_filterbanks(
            nfilt=n_mels,
            nfft=n_dft,
            samplerate=sr,
            lowfreq=fmin,
            highfreq=fmax
        )
        return np.float32(mel_matrix)

    def call(self, x):
        """Compute mel filterbank coefficients.

        Args:
            x: The input power spectrum.

        Returns:
            The mel filterbank coefficients.
        """
        melfbank = tf.matmul(x, self.weight)
        return melfbank


def MelTransformModel(sr, n_fft, n_mels, batch_size=None, time_steps=None, ip_name='ip', output_name='op'):
    """Create a model for mel frontend transformation.

    Args:
        sr: The audio sampling rate (in Hz).
        n_fft: The number of FFT frequencies.
        n_mels: The number of mel frequencies to create.
        batch_size: The batch size of the input data.
        time_steps: The number of time steps in the input data.
        ip_name: The name of the input layer.
        output_name: The name of the output layer.

    Input:
        The input to this model is a PowerSpectrum (||STFT|^2) of dimension (batch_size, seq_len, n_fft//2 + 1)

    Outputs:
        Mel transformed features, multiplied by MelMatrix of dimension (batch_size, seq_len, n_mels)
        
    Returns:
        A Keras model for performing mel frontend transformation.
    """
    feat_dim = n_fft // 2 + 1
    ip = tf.keras.Input(batch_size=batch_size, shape=(time_steps, feat_dim), name=ip_name)

    output = MelTransformLayer(sr=sr, n_fft=n_fft, n_mels=n_mels)(ip)

    output_dict = {output_name: output}

    model = tf.keras.Model(inputs=ip, outputs=output_dict)
    return model
