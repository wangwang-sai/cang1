'''
    用例同时去跑。
    用户同时去抢票。

    python实现多线程：
    1.继承threading 的Thread 线程类，
    2.重写run方法：
        任务代码写在run方法

    3.启动：start()
'''
from threading import Thread
import time
bread=500
#厨师：三个厨师造面包，当篮子已满，等待2秒钟，然后继续判断是否已满，
# 若没有满，造一个加1个
class chef(Thread):
   chefname=""
   def run(self)->None:

       global bread
       count = 0
       while True:
           if bread < 500:  #判断篮子数量，统计数量
               bread=bread+1
               count=count+1
               print("面包篮还有", bread, "个面包", self.chefname, "做了", count, "个面包")
           elif bread == 500:
               time.sleep(2)




#每个用户3000元，每个面包2.5元
#每个用户负责抢面包，当篮子不够，等待
#3秒后继续抢，一直到3000用完
class customer(Thread):
    username = ""

    def run(self) -> None:
        global bread
        money=3000
        count=0

        while True:
            if bread >0:
                if money>0:
                 bread=bread-1
                 money=money-2.5
                 count=count+1
                 print(self.username, "抢购了",count,"个面包","余额为:",money)
                else:
                    print(self.username, "账户余额不足了！老铁")
                    break
            else:
                print("等会，马上出锅")
                time.sleep(3)



#p1 = chef()
p1 = chef()
p2 = chef()
p3 = chef()

t1 = customer()
t2= customer()
t3 = customer()
t4 = customer()
t5 = customer()
t6 = customer()



p1.chefname = "yi师傅"
p2.chefname = "er师傅"
p3.chefname = "san师傅"

t1.username = "张三"
t2.username = "李四"
t3.username = "王五"
t4.username = "钱七"
t5.username = "田八"
t6.username = "铁九"

#p1.start()
p1.start()
p2.start()
p3.start()

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()






































