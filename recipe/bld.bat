@echo on

set "CONDA_ROOT=%LIBRARY_PREFIX:\=/%"

%PYTHON% -m pip install . --no-deps -vv
if %ERRORLEVEL% neq 0 exit 1
