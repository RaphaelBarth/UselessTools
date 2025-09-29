:: setting up the properties
@echo off
set INTERVAL=3600

::print some informations
echo.
echo The script is running. You can minimize this window.
echo ...

:: start the loop
:reminder
	timeout /t %INTERVAL% /nobreak >nul
	start /min /wait "" python ".\display_message.py"
	msg * "Incorporating some movement into the routine might be one possible solution."
goto reminder
