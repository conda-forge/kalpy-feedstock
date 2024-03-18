import os

test_cuda = os.environ.get('CF_CUDA_ENABLED', "False") == "True"

if test_cuda:
    print("TESTING CUDA")
else:
    print("CUDA NOT ENABLED FOR TESTING")


if __name__ == '__main__':

    if not test_cuda:
        import _kalpy
        import kalpy

