
'''
    w:写
    r:读取
    +：
    a:附加

    b:字节



try:
    file = open(file="baidu_x_system.log",mode="r+",encoding="utf-8")

    # data = file.read()  # read() 一下读取全文数据
    # readline() 读取一行数据

    # data = file.readline()
    # data1 = file.readline()
    # data = file.readlines()  # readlines()将所有行的数据放在列表里

    # 写：w+  write()
    file=file.read(file)
    print(file)



except FileNotFoundError:
    print("没有这个文件！重新适配文件！")
finally:
    file.close()  # 关闭资源
'''
import time
pin = 0
count=0
while True:
    with open('baidu_x_system.log', 'r') as f:
        f.seek(pin) #定位到上次读取文件后，游标的位置
        ips = []   #每次循环时把列表清空，因为是按1分钟进行统计的
        for line in f:
            ip = line.split(' ')[0] #提取每一行的ip，保存到list中
            ips.append(ip)
        for ip in set(ips):
            print('ip为： %s'%ip,"个数为：",ips.count(ip))
        pin = f.tell() #读取游标当前的位置
    time.sleep(60) #休息60s后开始下一个循环




