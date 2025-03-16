@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

:: Accept command line arguments for Python executable and target path
:: Usage: setup_poetry.bat [python_path] [target_path]
set "PYTHON_PATH=%~1"
set "TARGET_PATH=%~2"

:: Validate arguments
if "%PYTHON_PATH%"=="" (
    echo Python path not specified.
    echo Usage: setup_poetry.bat [python_path] [target_path]
    exit /b 1
)

if "%TARGET_PATH%"=="" (
    echo Target path not specified.
    echo Usage: setup_poetry.bat [python_path] [target_path]
    exit /b 1
)

:: Create directories if they don't exist
if not exist "%TARGET_PATH%" mkdir "%TARGET_PATH%"
if not exist "%TARGET_PATH%\.local\bin" mkdir "%TARGET_PATH%\.local\bin"
if not exist "%TARGET_PATH%\.local\share" mkdir "%TARGET_PATH%\.local\share"

:: Create and activate virtual environment
echo Creating virtual environment at %TARGET_PATH%\venv...
"%PYTHON_PATH%" -m venv "%TARGET_PATH%\venv"

:: Activate the virtual environment
call "%TARGET_PATH%\venv\Scripts\activate.bat"
if %errorlevel% neq 0 (
    echo Failed to activate virtual environment.
    exit /b 1
)

:: Set temporary environment variables for pipx
set "PIPX_HOME=%TARGET_PATH%\.local\share"
set "PIPX_BIN_DIR=%TARGET_PATH%\.local\bin"
echo Setting PIPX_HOME to %PIPX_HOME%
echo Setting PIPX_BIN_DIR to %PIPX_BIN_DIR%

:: Update pip in the virtual environment
echo Updating pip...
python -m pip install --upgrade pip
if %errorlevel% neq 0 (
    echo Failed to update pip.
    exit /b 1
)

:: Install pipx
echo Installing pipx...
python -m pip install pipx
if %errorlevel% neq 0 (
    echo Failed to install pipx.
    exit /b 1
)

:: Install poetry using pipx
echo Installing poetry using pipx...
python -m pipx install poetry
if %errorlevel% neq 0 (
    echo Failed to install poetry.
    exit /b 1
)

:: Verify poetry installation
if not exist "%TARGET_PATH%\.local\bin\poetry.exe" (
    echo Poetry installation could not be verified.
    exit /b 1
)

@REM :: Add poetry.exe to the PATH environment variable (user level)
@REM echo Adding %TARGET_PATH%\.local\bin to PATH...
@REM for /f "tokens=2*" %%A in ('reg query HKCU\Environment /v PATH') do set "CURRENT_PATH=%%B"
@REM setx PATH "%CURRENT_PATH%;%TARGET_PATH%\.local\bin"
@REM if %errorlevel% neq 0 (
@REM     echo Failed to update PATH environment variable.
@REM     exit /b 1
@REM )

:: Report success
echo.
echo Setup completed successfully!
echo.
echo Poetry has been installed at %TARGET_PATH%\.local\bin\poetry.exe
echo The directory has been added to your PATH environment variable.
echo.
echo You may need to restart your command prompt for the PATH changes to take effect.
echo You can activate this virtual environment in the future by running:
echo     call "%TARGET_PATH%\venv\Scripts\activate.bat"
echo.

:: Deactivate the virtual environment before exiting
deactivate

endlocal
