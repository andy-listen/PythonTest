'''
Created on 2016年3月17日

@author: Administrator
'''
from msilib.schema import File
from pip._vendor.distlib.compat import raw_input
import sys;
from _ctypes import Array
from ctypes.wintypes import LONG
# print("Hello world")
# if True:
#     print("true")
#     print("ssss")
# else:
#     print("false")
# print("fdsdfasd")
# 
# print("saaaaaaaaaaa");
# name ="abc"
# print(name);
# raw_input(" please input ")
# x="foo";
# sys.stdout.write(x+"\n")
# var1 = 1;
# var2 = 10;
# print(var1);
# del var1;
# print(var1)
# s = "abcdefg";
# print(s[0]);
# print(s[0:]);
# print(s[1:])
# print(s[2:5])
# print(s[:5]);
# print(s*2);
# var1 = 2;
# print(var1*var1);
# arr = ["1",1,"abc",3.3];
# print(arr[0:2]);
# print(arr+arr)

    # list = ("abc",8989,22/2);
# print(list[3])
# dict = {};
# dict["code"]=1;
# dict["name"]="fuck";
# # print(dict);
# # var1 = 1.1;
# # print(int(200000000000000000000000000000000000000000000.6));
# # print(float(111111111111111111111111111111111111111111))
# print(repr(dict));
# def myFunction(params="hhh"):
#     "dsafsdfasdfasda"
#     print("my params:"+params)
#     return;
# myFunction();
def extendFunction(var1,*varN):
    print(var1);
    for var in varN:
        print(var)
    return;
# extendFunction(1,2,3,4,5)
 

sum = lambda arg1,arg2:arg1+arg2;
# print(sum(1,2));

def sumFunction(var1,var2):
    return var1+var2;
# print(sumFunction(1, 5));






