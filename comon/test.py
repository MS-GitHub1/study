import hashlib
import random
from comon.sql_handel import Mysql
from Othermethods.sj_number import numbers
path=r'C:\Users\Administrator\Desktop\1.txt'
def read_data2():
    with open(path,'r',encoding='utf-8') as f:
        files = f.readlines()
        data=random.choice(files)
        name2=random.choice(data)
        if name2 =='\n' or name2 ==',':
            while True:
                data = random.choice(files)
                name2 = random.choice(data)
                if name2 !='\n' and name2 !=',':
                    break
        return name2

def read_data():
    with open(path,'r',encoding='utf-8') as f:
        files = f.readlines()
        data=random.choice(files)
        name2=random.choice(data)
        if name2 =='\n' or name2 ==',':
            while True:
                data = random.choice(files)
                name2 = random.choice(data)
                if name2 !='\n' and name2 !=',':
                    break
        return name2


def data_name():
    return read_data() + read_data2()

def random_num():
    list_num=[i for i in range(1,10)]
    sj_num = random.choice(list_num)
    return str(sj_num)+'年级'


def random_age():
    list_num=[i for i in range(1,20)]
    return random.choice(list_num)



def updata():
    data_all = Mysql.check_all(sql='select * from name ')
    for data in data_all:
        if data['id'] %2==0:
            Mysql.insert_into_data(sql='UPDATE name SET sex=1 WHERE id ="{}"'.format(data['id']))


# 查询空数据，添加对应的内容
def fix():
    data_all=Mysql.check_all('select * from name ')
    for datas in data_all:
        data_num = Mysql.check_all("select num from name where id ='{}'".format(datas['id']))
        if data_num[0]['num'] ==None:
            Mysql.insert_into_data("UPDATE name SET num='{}' WHERE id ='{}'".format(numbers(),datas['id']))
        # if datas['class'] =='0年级':
        #     print(datas['id'])
        #     Mysql.insert_into_data(sql='UPDATE name SET class="{}" WHERE id ="{}"'.format(random_num(),datas['id']))


def md(str):
    hl = hashlib.md5()
    hl.update(str.encode(encoding='utf-8'))
    print('MD5加密后为 ：' + hl.hexdigest()[8:-8])





if __name__ == '__main__':
    md('1111')

# # 生成MD5
# def genearteMD5(str):
#     # 创建md5对象
#     hl = hashlib.md5()
#     hl.update(str.encode(encoding='utf-8'))
#     return hl.hexdigest()
#
# if __name__ == '__main__':
#     print(genearteMD5(str='1'))


