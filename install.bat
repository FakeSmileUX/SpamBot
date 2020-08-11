@echo off
python -V >nul 2>&1 && (
    python spambot.py
) || (
    echo "Python 3.7 not found, plase install Python 3.7!"
    timeout /t 5 /nobreak > NUL
    exit
)

timeout /t 15 /nobreak > NUL
