@echo off
echo Setting up environment...

REM Backend Setup
echo Setting up Backend...
cd backend
if not exist venv (
    echo Creating virtual environment...
    python -m venv venv
)

echo Activating virtual environment...
call venv\Scripts\activate

echo Installing dependencies...
pip install -r requirements.txt

cd ..

REM Frontend Check
echo Checking Frontend...
where hugo >nul 2>nul
if %errorlevel%==0 (
    echo Hugo is installed.
) else (
    echo Hugo is NOT installed. Please install Hugo Extended.
)

echo Setup complete!
echo To run the backend: cd backend ^& call venv\Scripts\activate ^& uvicorn main:app --reload
echo To run the frontend: cd frontend ^& hugo server -D
