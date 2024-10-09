import subprocess

# 设置cmd命令
ICON = f'' #'--icon "{Settings.ICONS}"'
NAME = f'' #'--name "{Settings.PROJECT_NAME} {Settings.VERSION}"'
DATA = f''
FILE = f'main.py'
BUILD = f'--workpath "build"'
OUTPUT = f'--distpath "output"'

CMDS = f'{ICON} {NAME} {DATA} {FILE} {BUILD} {OUTPUT}'

cmd = f"pyinstaller --noconfirm --onefile --windowed {CMDS}"

# 执行命令
try:
    subprocess.run(cmd)
    print("执行文件已成功编译")
except subprocess.CalledProcessError as e:
    print("编译执行文件时出错:", e)