import os
import subprocess

LIBPNG = "libpng-1.6.37"

TOP_DIR = os.getcwd()
INSTALL_PREFIX = os.path.abspath(os.path.join(TOP_DIR, "..", "library"))

LIBPNG_DIR = os.path.join(TOP_DIR, LIBPNG)

#------------------------------------------------------------
# 外部コマンド実行
def Do(cmd):
    command = " ".join(cmd)
    Log("Run: " + command)
    result = subprocess.call(command, shell=True)
    if result != 0:
        Error(command + "  result=" + str(result))

#------------------------------------------------------------
# エラー出力
def Error(msg):
    Log("Error !!! " + msg)
    os.sys.exit(0)

#------------------------------------------------------------
# ログ出力
def Log(msg):
    print("* " + msg)
