
@echo off
cd /d %~dp0
echo 正在运行关键词增强脚本...
python scripts\get_mixed_keywords.py
pause
