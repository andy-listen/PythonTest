'''
Created on 2016年3月17日

@author: Administrator
'''
# str = raw_input("请输入：");
# print("HHHHH:x"+str);
from builtins import bytes
from cgitb import text
 
# str = input("请输入：");
# print("你输入的内容是："+str);
# fo = open("foo.txt", mode='wb')
# print("文件名: "+fo.name)
# print("是否已关闭 : ", fo.closed)
# print("访问模式 : ", fo.mode)
# fo.write(bytes("hello wo\n" ,'utf-8') );
# fo.close();
# with open("foo2.txt", mode='wt',  encoding=None, errors=None, newline=None, closefd=True, opener=None) as fp:
#     fp.write("next");
#     fp.close();
# fo = open("foo.txt", "r+")
# str = fo.read(1);
# print(str)
# # 查找当前位置
# position = fo.tell();
# print ("当前文件位置 : ", position)
#  
# # 把指针再次重新定位到文件开头
# position = fo.seek(0, 0);
# str = fo.read(10);
# print ("重新读取字符串 : ", str)
# # 关闭打开的文件
# fo.close();

import os;
# os.renames("foo.txt", "fnew.txt");
# os.remove("foo2.txt");
# os.mkdir("newdir");
# os.chdir("newdir");
# print(os.getcwd());
os.rmdir('newdir')
