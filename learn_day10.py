# coding=gbk

# def add(x,y):
#     """
#
#     :param x: ����һ
#     :param y: ������
#     :return: �����������ĺ�
#     """
#     result=x+y
#     return result
# print(add(5,10))
money=5000000
name=input("����������")
def menu():
    print("��ѯ���     \t[����1]")

    print("���        \t[����2]")
    print("ȡ��        \t[����3]")

    print("�˳�        \t[����4]")
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
    print(f"{name},����,�������ʣ��{money}Ԫ")
def deposit():
    x=int(input(f"{name},����,�������"))
    global money
    money += x
    print(f"���ɹ�,���{money}Ԫ")
def withdraw():
    x = int(input(f"{name},����,����ȡ��"))
    global money
    money -= x
    print(f"ȡ��ɹ�,���{money}Ԫ")

def main():
    menu()
main()




