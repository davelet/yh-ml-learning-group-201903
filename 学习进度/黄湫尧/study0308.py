# 第一个注释
# 第二个注释

'''
第三注释
第四注释
'''

"""
第五注释
第六注释
"""
print("Hello, Python!");

"""
使用缩进来表示代码块，不需要使用大括号 {} 。

缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。

"""
if True:
    print("hello helen")
else:
    print("hello stranger")


'''
多行
'''

val= 1 + 2 + \
    3 + 4 +\
    5 + 6
print(val);

name=['你',"hao",
      "huang",'湫'
      ,"yao"]
print(name)


str='Helen~la'

print(str)                 # 输出字符串
print(str[0:-1])           # 输出第一个到倒数第二个的所有字符
print(str[0])              # 输出字符串第一个字符
print(str[2:5])            # 输出从第三个开始到第五个的字符
print(str[2:])             # 输出从第三个开始的后的所有字符
print(str * 2)             # 输出字符串两次
print(str + '你好')        # 连接字符串

print('------------------------------')

print('hello\n'+str)      # 使用反斜杠(\)+n转义特殊字符
print(r'hello\n'+str)     # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# input("\n\n按下 enter 键后退出。")

"""
一行多条语句
"""
import sys; sys.stdout.write("dd")


name="helen"
if name=="li" :
   print("1")
elif name=="mi" :
   print("3")
else :
   print("####")


