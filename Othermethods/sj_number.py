import random
def numbers():
    num=""
    for i in range(9):
        c = random.randint(1,9)
        num = num+str(c)
    list1 = ["3", "5", "8"]
    number = "1"+random.choice(list1)+num
    return number

if __name__ == '__main__':
    print(numbers())

"""生产的操作流程,物料使用的流程，erp系统  原材料，使用添加剂等  物料  生成指令下边操作  bom   追溯 941  921  1 是b班  
输单员  生产 发货 客户订单量，那个品相 订单完成量
统计员招聘标准  数据分析 先进先出 """