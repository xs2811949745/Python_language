#coding=utf-8
import sys
# from qn_checker_func import *
# from st_checker_func import *
# from cn_checker_func import *
# from pw_checker_func import *
# from mn_checker_func import *
# from flag_checker_func import *
# from cp_checker_func import *


## QN  检查，本质是 日期检查
from datetime import datetime

# 定义日期格式 年月日时分秒毫秒
format = "%Y%m%d%H%M%S%f"
qn_minLength = 17  # 未来可从packet-schema.json 读
qn_maxLength = 17  # 未来可从packet-schema.json 读

def check_pumn(pumn):
    try:
        if(type(pumn)!=str):
            raise IndexError("包总数非字符串类型！")
        if(len(pumn)!=9):
            raise ValueError("包总数非法")
    except Exception as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)
def check_pno(pno):
    try:
        if (type(pno) != str):
            raise IndexError("包号非字符串类型！")
        if (len(pno) != 8):
            raise ValueError("包号非法")
    except Exception as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)

def check_qn(qn_str):
    qn_v = qn_str.split("=")[1]
    try:
        if(len(qn_v)==0):
            raise ValueError("QN无值")
        try:
            CN_date = datetime.strptime(qn_v, format)
        except:
            raise IndexError("QN不是日期")
            # print(qn_v)
        if (len(qn_v) > qn_maxLength):
           raise ValueError("QN长度多")
        elif (len(qn_v) < qn_minLength):
           raise ValueError("QN长度缺")
    except ValueError as e:   #传入无效参数
        #print(e)      #repr将对象转化为供解释器读取的形式
        raise ValueError(e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)

# coding=utf-8

## ST 检查
st_target_list = ["21", "22", "23", "24", "25", "26", "27", "31", "32", "33", "34", "35", "36", "37", "38", "39", "41",
                  "51", "52", "91"]


# st_target_list 未来可从packet-schema.json 读


def check_st(st_str):
    try:
        st_v = st_str.split("=")[1]
        # print(st_v)
        if (len(st_v)==0):
            raise ValueError("ST无值")
        elif st_v not in st_target_list:
            raise ValueError("ST值域错误")
    except ValueError as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)
    # except IndexError as e:
    #     print(e)
    #     raise ValueError("ST格式不合法")
    # except Exception as e:
    #     print(e)
    #     raise ValueError(e)

# coding=utf-8

#1000-9999
def check_cn(cn_str):
    cn_v=cn_str.split("=")[1]
    # print(len(cn_v))
    try:
        if(len(cn_v)==0):
            raise ValueError("CN无值")
        if(int(cn_v)<1000 or int(cn_v)>9999):
            raise ValueError("CN值域错误")
    except ValueError as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)

# coding=utf-8
# 6-6
#string
maxlen=6
minlen=6
def check_pw(pw_str):
    pw_v=pw_str.split("=")[1]
    try:
        if(len(pw_v)>maxlen):
            raise ValueError("PW长度多")
        if(len(pw_v) < minlen):
            raise ValueError("PW长度缺")
    except Exception as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)
# coding=utf-8

#6-6
size=24
def check_mn(mn_str):
    mn_v=mn_str.split("=")[1]
    try:
        if(len(mn_v)>size):
            raise ValueError("MN长度多")
        if (len(mn_v) < size):
            raise ValueError("MN长度缺")
    except Exception as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)

# coding=utf-8
#CP=&&RtdInterval=30&&
def check_cp(cp_str):
    cp_v=cp_str.split("=")
    try:
        if(cp_v[1]=="&&&&"):
            raise ValueError("CP正确无参数")
        if(cp_v[1].find('&')!=-1 and cp_v[1].find('&&')==-1):
            raise ValueError("CP缺1个左&")
        if(cp_v[1].find('&&')==-1):
            raise ValueError("CP缺2个左&")
        if (cp_v[2].find('&') != -1 and cp_v[2].find('&&') == -1):
         raise ValueError("CP缺1个右&")
        if (cp_v[2].find('&&') == -1):
            raise ValueError("CP缺2个右&")
    except Exception as e:
        raise (e)
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)

# coding=utf-8
def check_flag(flag_str):
    flag_v=flag_str.split("=")[1]

    try:
        if(int(flag_v)>255 or int(flag_v)<0):
            raise ValueError("Flag值域错误")
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)
    except Exception as e:
        raise (e)


def check_other(other_str):
    try:
        if(other_str[-1]==";"):
            raise ValueError("数据段尾部多;号")
        if(other_str.find(";;")!=-1):
            raise ValueError("数据段中部多;号")
    except IndexError as e:  #无此索引
        # print(e)
        raise ValueError(e)  #这些不要？

    except Exception as e:
        # print(e)
        raise ValueError(e)
    except Exception as e:
        raise (e)


if __name__ == "__main__":
    data_section=sys.argv[1].split(";")

    # 打印命令行参数
    # sys.arg[1]="QN=20160801085857223;ST=32;CN=;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"
    # print ("sys.arg[1]:",sys.argv[1])
    #使用分号切分数据段数据 ，赋值给变量 data_section
    # a=len(sys.argv)
    # print(data_section)
    # check_pumn(a)
    # src="QN=20160801085857223;ST=20;CN=1062;PW=100000;MN=010000A8900016F000169DC0;Flag=5;CP=&&RtdInterval=30&&"
    # data_section=src.split(";")

    # data_section=sys.argv[1].split(";")
    # 观察 data_section的值
    # print("data_section:",data_section)

    # 循环遍历data_section 的元
    str="QN;ST;CN;PW;MN;Flag;CP"
    target=str.split(";")
    count=0
    i=0
    # print(len(sys.argv))
    a=[0,0,0,0,0,0,0]
    try:
        for item in data_section:
            # print("item:",item)
            count+=1
            #如果元素内包含QN 则调用QN的检查函数check_qn
            if item.find("QN") != -1:
                # print("QN:",item) #修改？
                a[0]=1


                check_qn(item)
            if item.find("ST") != -1:
                # print("QN:",item) #修改？
                a[1] = 1


                check_st(item)
            if item.find("CN") != -1:
                # print("QN:",item) #修改？
                a[2] = 1


                check_cn(item)
            if item.find("PW") != -1:
                # print("PW:",item) #修改？
                a[3] = 1

                check_pw(item)
            if item.find("MN") != -1:
                a[4] = 1


                # print("PW:",item) #修改？
                check_mn(item)
            if item.find("Flag") != -1:
                # print("PW:",item) #修改？
                a[5] = 1


                check_flag(item)
            if item.find("CP") != -1:
                # print("PW:",item) #修改？
                a[6] = 1


                check_cp(item)
            if(item==data_section[-1]):
                flag=1
                check_other(sys.argv[-1])
                for x in range(len(a)):
                    if(a[x]==0):
                        flag=0
                        raise ValueError("数据段缺"+target[x])
                if(count>7):
                    raise ValueError("数据段多字段")
                elif(flag==1):
                    raise ValueError("数据段完整")
    except Exception as e:
        print(e)

            # for x in target:
            #    count+=1
            #    if(sys.argv[1].find((x))==-1):
            #        raise ValueError("数据段缺"+x)
            # if(count==7):
            #     print("数据段完整")
            # if (count > 7):
            #     raise ValueError("数据段多字段")







