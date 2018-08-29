#!/usr/bin/env python
# -*- coding: UTF-8 -*-
#从命令行读入一个字符串，表示一个年份，输出该年的世界杯冠军是哪支球队。如果该 年没有举办世界杯，则输出：没有举办世界杯。
FIFA = {"1930":"乌拉圭","1934":"意大利","1938":"意大利","1950":"乌拉圭","1954":"西德","1958":"巴西","1962":"巴西","1966":"英格兰","1970":"巴西","1978":"阿根廷","1982":"意大利","1986":"阿根廷","1990":"西德","1994":"巴西","1998":"法国","2002":"巴西","2006":"意大利","2012":"西班牙","2016":"德国"}

def menu():
    print("\n")
    print ("1. 查询该年份世界杯冠军球队")
    print ("2. 查询该国家球队获得哪几年世界杯冠军")
    print ("3.退出程序")

def yearcheck():
    year = input("输入年份:")
    if (int(year)-1930)%4==0:
        print(FIFA[year])
    else:
        print("该年没有举办世界杯")

def countrycheck():
    none = 0
    country = input("输入国家:")
    for key in FIFA:
        if country == FIFA[key]:
            print(key+"年")
        else:
            none = none + 1
    if none == 19:
        print("该国家没有拿过世界杯冠军\n")

def main():
    choice = '1'
    while choice!='3':
        menu()
        choice = input('选择功能: ')
        if choice == '1':
            yearcheck()
        elif choice == '2':
            countrycheck()
        elif choice == '3':
            print('程序退出！！')
        else:
            print('[-] 无效的选项!')

if __name__ == "__main__":
    main()
