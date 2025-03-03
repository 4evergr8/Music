@echo off
setlocal enabledelayedexpansion

:: 检查是否在 Git 仓库中
git rev-parse --is-inside-work-tree >nul 2>&1
if %errorlevel% neq 0 (
    echo 当前目录不是一个 Git 仓库，请先初始化 Git 仓库。
    pause
    exit /b 1
)

:: 遍历当前文件夹及其子文件夹中的所有文件
for /r %%f in (*) do (
    set "filename=%%f"
    set "relative_path=!filename:~2!"

    :: 添加文件到 Git
    echo 正在添加文件：!relative_path!
    git add "!filename!"

    :: 提交文件
    echo 正在提交文件：!relative_path!
    git commit -m "Add file: !relative_path!"
    echo 文件 !relative_path! 已提交。
)

echo 所有文件已成功添加并提交。
pause