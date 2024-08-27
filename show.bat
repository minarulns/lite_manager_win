@echo off
choco install anydesk -y --ignore-checksums --force --no-progress --pre
:START_ANYDESK
anydesk --start
powershell -Command "Start-Sleep -Seconds 5"
for /f "delims=" %%i in ('"C:\ProgramData\chocolatey\lib\anydesk.portable\tools\AnyDesk.exe" --get-id') do (
    set ID=%%i
)
if "%ID%"=="" (
    taskkill /f /im anydesk.exe > nul
    goto START_ANYDESK
)
if "%ID%"=="0" (
    taskkill /f /im anydesk.exe > nul
    goto START_ANYDESK
)
echo Minarul01BD | anydesk.exe --set-password _full_access
start "" /MAX "C:\Users\Public\Desktop\VMQuickConfig"
python -c "import pyautogui as pag; pag.click(143, 487, duration=5)"
python -c "import pyautogui as pag; pag.click(155, 554, duration=2)"
python -c "import pyautogui as pag; pag.click(637, 417, duration=2)"
python -c "import pyautogui as pag; pag.click(588, 10, duration=2)"
echo ............................................................
echo .................. Brought to you by .......................
echo ............................................................
echo    __  __  _____  _   _            _____   _    _  _       
echo   |  \/  ||_   _|| \ | |    /\    |  __ \ | |  | || |      
echo   | \  / |  | |  |  \| |   /  \   | |__) || |  | || |      
echo   | |\/| |  | |  | . ` |  / /\ \  |  _  / | |  | || |      
echo   | |  | | _| |_ | |\  | / ____ \ | | \ \ | |__| || |____  
echo   |_|  |_||_____||_| \_|/_/    \_\|_|  \_\ \____/ |______|
echo ............................................................
echo ....... If You want to run Windows-10 using AnyDesk ........
echo ...... Watch It Here - https://youtu.be/G2RE0DlFstg ........
echo ............................................................
echo ............................................................
echo Windows Cloud PC ID is: %ID%
echo Windows Cloud Password: Minarul01BD
echo You can login now!
