print("running: main_package/package_outer.py")

# 如何导入同一个 package 内部的其他内容
# 1 相对导入（感觉有点丑）
from . import math_tools
from .basic_tools import log
# 2 绝对导入
import main_package.gui.macos.main_window as mw

class package_outer_class:
    def __init__(self):
        print("class: package_outer_class")

def package_outer_func():
    print("func: package_outer_func")
    log.log()
    win = mw.main_window()
    math_tools.pre_calc_math_values()