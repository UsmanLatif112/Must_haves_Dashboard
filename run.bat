@echo off
echo Starting Must Haves Prouction App...

REM Go to main folder
cd /d C:\Users\Administrator\Desktop\Must_Haves_Production

REM Go to project folder
cd aitomation-must-haves

REM Activate virtual environment
cd venv\Scripts
call activate

REM Go back to project root
cd ..\..\

REM Go to v1 folder
cd v1

REM Run the app
python app.py

pause