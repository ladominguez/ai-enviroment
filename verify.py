#!/usr/bin/env python3

import sys

print("=" * 60)
print("Python")
print(sys.version)

print("=" * 60)

# ------------------------------------------------------------------
# PyTorch
# ------------------------------------------------------------------

try:
    import torch

    print(f"PyTorch: {torch.__version__}")
    print(f"CUDA available: {torch.cuda.is_available()}")

    if torch.cuda.is_available():
        try:
            gpu_name = torch.cuda.get_device_name(0)
            print(f"GPU: {gpu_name}")

            # Try an actual GPU computation
            x = torch.randn(1000, 1000, device="cuda")
            y = torch.matmul(x, x)

            print("PyTorch GPU test: OK")

        except Exception as e:
            print("PyTorch GPU test: FAILED")
            print(f"Reason: {e}")
            print("Falling back to CPU.")

    else:
        print("No CUDA GPU detected.")

except Exception as e:
    print("PyTorch FAILED")
    print(e)

print("=" * 60)

# ------------------------------------------------------------------
# TensorFlow
# ------------------------------------------------------------------

try:
    import tensorflow as tf

    print(f"TensorFlow: {tf.__version__}")

    gpus = tf.config.list_physical_devices("GPU")
    print(f"GPUs: {gpus}")

    if gpus:
        try:
            with tf.device("/GPU:0"):
                a = tf.random.normal((1000, 1000))
                b = tf.matmul(a, a)

            print("TensorFlow GPU test: OK")

        except Exception as e:
            print("TensorFlow GPU test: FAILED")
            print(f"Reason: {e}")

    else:
        print("TensorFlow is using the CPU.")

except Exception as e:
    print("TensorFlow FAILED")
    print(e)

print("=" * 60)

# ------------------------------------------------------------------
# ObsPy
# ------------------------------------------------------------------

try:
    import obspy

    print(f"ObsPy: {obspy.__version__}")

except Exception as e:
    print("ObsPy FAILED")
    print(e)

print("=" * 60)

print("Environment verification complete.")
