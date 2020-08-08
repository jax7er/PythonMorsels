@echo off

set folder=%cd%
set message=None
set branch=master
set /p folder="Folder path (default %folder%): "
set /p message="Commit message (default %message%): "
set /p branch="Branch (default %branch%): "

cd %folder%
call git add -A
call git commit -m "%message%"
call git push origin %branch%

set /p temp="Completed successfully, press <Enter> to exit"