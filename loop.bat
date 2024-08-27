@echo off
pip install psutil --quiet
pip install requests --quiet
curl -s -L -o loop.py https://gitlab.com/chamod12/lite_manager_win/-/raw/main/loop.py
python loop.py
