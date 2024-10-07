:: setting up the properties
@echo off
@REM if %1=="" (
@REM 	set interval=3600
@REM ) else (
@REM 	set interval = %1
@REM 	echo interval
@REM )

set interval=3600

::print some informations
echo.
echo The script is in progress and you can minimize the window if you would like to do so.
echo ...

:: start the loop
:reminder
	timeout /t %interval% /nobreak >nul
	start /min /wait "" python ".\display_message.py"
	msg * "Incorporating some movement into the routine might be one possible solution."
goto reminder
