@echo on

dir %RECIPE_DIR%

echo %LIB%

"%PYTHON%" -m pip install . --no-deps -vv

if errorlevel 1 exit 1
