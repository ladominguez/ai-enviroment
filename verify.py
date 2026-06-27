import sys

print("="*60)
print("Python")
print(sys.version)

print("="*60)

try:
    import torch

    print("PyTorch:", torch.__version__)
    print("CUDA:", torch.cuda.is_available())

    if torch.cuda.is_available():
        print("GPU:", torch.cuda.get_device_name(0))
except Exception as e:
    print("PyTorch FAILED")
    print(e)

print("="*60)

try:
    import tensorflow as tf

    print("TensorFlow:", tf.__version__)
    print("GPUs:", tf.config.list_physical_devices("GPU"))
except Exception as e:
    print("TensorFlow FAILED")
    print(e)

print("="*60)

try:
    import obspy
    print("ObsPy:", obspy.__version__)
except Exception as e:
    print(e)

print("="*60)


x = torch.randn(1000, 1000, device="cuda")
y = torch.matmul(x, x)
print("PyTorch GPU test: OK")

import tensorflow as tf

with tf.device("/GPU:0"):
    a = tf.random.normal((1000, 1000))
    b = tf.matmul(a, a)

print("TensorFlow GPU test: OK")
