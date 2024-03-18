import os
print("CF_CUDA_ENABLED:", os.environ.get('CF_CUDA_ENABLED', "False"))
cuda_compiler_version = os.environ.get('cuda_compiler_version', "None")
print("cuda_compiler_version:", cuda_compiler_version)

test_cuda = cuda_compiler_version != "None"
if test_cuda:
    print("TESTING CUDA")
else:
    print("CUDA NOT ENABLED FOR TESTING")


if __name__ == '__main__':
    if not test_cuda:
        import _kalpy
        import kalpy

