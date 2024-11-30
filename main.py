# main.py 这是模块外的一个脚本 作为程序入口实用

# 以下 py 文件称为 module 文件夹称为 package
# 注意此处用语可能不太准确

# Python 在导入 module 的时候会在 sys.modules 记录
# 所以通过正常方式导入 module 不用担心会被多次重复导入

# 导入一个 module 也就是把对应的 py 文件运行一遍
# 在函数和类的定义之外的内容在 import 的时候就会执行生效

# 首先我们要理解 Python 是如何执行 import 的
# import 可以分为两种
# 1: import package/module (as other_name)
# import package 的时候 从包的顶层到 package/__init__.py 都会被执行
# import module 的时候 从包的顶层到 module 都会被执行
# 导入包就像导入包下的 __init__.py
# 请参考以下的例子

# 2: from package/module import module/content
# 需要注意的是 即使只是导入一个 module 的部分内容
# 整个 module 的全部代码也都会被完整执行
# 同理从包的顶层目录开始的 __init__.py 也会执行

# 例子开始
# 这里我们导入了一个 package 那么其目录下的 __init__.py 就会执行
import main_package

# 那么在 main_package/__init__.py 中定义的内容也就可以访问了
main_package.package_entry()

# main_package 下面包含 basic_tools
# 那么 main_package 导入之后 basic_tools 就可以使用了吗
# 答案是不行 main_package.basic_tools 现在是访问不到的
# 注意 导入一个 package 不意味着导入其内部所有内容
# 如果需要实用其内部内容 要么单独导入 要么编辑 __init__.py
# 使用下面这句 会调用 main_package/basic_tools/__init__.py
# 实际上 main_package/__init__.py 也会被尝试调用
# 只是因为前面调用过了 所以在此处会跳过
import main_package.basic_tools

# 现在就可以使用 basic_tools 了 注意使用的时候是按照全称使用 比如
main_package.basic_tools.basic_tools_loader()

# 如果不想用全称 可以用 as 缩短一下名称
# 另外 上面都是 import package 所以调用的都是 __init__.py
# 这里 我们是 import module 所以是调用的这个 moudle 对应的 py 文件
import main_package.basic_tools.log as log
log.log()

# 现在 我们来看一下配置 __init__.py 的用法
# 我们没有导入 main_package.math_tools 但是现在可以直接使用
# 因为我们在 main_package/__init__.py 里面配置了自动导入 math_tools
main_package.math_tools.pre_calc_math_values()

# 同理
main_package.package_outer.package_outer_func()

# 这里 我们导入一个 module 观察一下输出 py 文件的执行顺序是什么
import main_package.gui.macos.main_window as mw
"""
running: main_package/gui/__init__.py
running: main_package/gui/macos/__init__.py
running: main_package/gui/macos/main_window.py
"""