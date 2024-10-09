import subprocess

# 设置rcc命令 https://doc.qt.io/qtforpython-6/tutorials/basictutorial/qrcfiles.html
rcc = r".\venv\Scripts\pyside6-rcc.exe"
cmd = f"{rcc} ./resources.qrc -o ./rc_resources.py"

# 执行命令
try:
    subprocess.run(cmd)
    print("资源文件已成功编译")
except subprocess.CalledProcessError as e:
    print("执行rcc时出错:", e)