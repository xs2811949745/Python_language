# coding=gbk

# def add(x,y):
#     """
#
#     :param x: 参数一
#     :param y: 参数二
#     :return: 返回两个数的和
#     """
#     result=x+y
#     return result
# print(add(5,10))
money=5000000
name=input("请输入姓名")
def menu():
    print("查询余额     \t[输入1]")

    print("存款        \t[输入2]")
    print("取款        \t[输入3]")

    print("退出        \t[输入4]")
    x=int(input())
    if x==1:
        search()
        menu()
    elif x==2:
        deposit()
        menu()
    elif x==3:
        withdraw()
        menu()
    elif x == 4:
        return None
    else:
        return None
def search():
    print(f"{name},您好,您的余额剩余{money}元")
def deposit():
    x=int(input(f"{name},您好,请您存款"))
    global money
    money += x
    print(f"存款成功,余额{money}元")
def withdraw():
    x = int(input(f"{name},您好,请您取款"))
    global money
    money -= x
    print(f"取款成功,余额{money}元")

def main():
    menu()
main()




