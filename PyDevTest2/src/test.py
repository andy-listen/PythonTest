'''
Created on 2016年3月17日

@author: Administrator
'''
import HelloWorld
from HelloWorld import sumFunction
print(sumFunction(1,9))
totalMoney = 100;
def add():
    global totalMoney;
    totalMoney=totalMoney+1;
    return;
add()
print(totalMoney);
import math
content = dir(math);
print(content);
print(globals());
print(locals('totalMoney'));