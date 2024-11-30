"""
main_package
"""

print("running: main_package/__init__.py")

from . import math_tools
import main_package.package_outer as package_outer

def package_entry():
    print("func: package_entry")
    math_tools.pre_calc_math_values()
    _t = package_outer.package_outer_class()