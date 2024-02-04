@echo on

set "KALDI_ROOT=%LIBRARY_PREFIX:\=/%"
set "CMAKE_BUILD_PARALLEL_LEVEL=1"

%PYTHON% -m pip install . --no-deps -vv
if %ERRORLEVEL% neq 0 exit 1
