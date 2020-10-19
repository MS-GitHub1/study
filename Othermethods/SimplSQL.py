from comon.sql_handel import My_sql
from comon.config import con
# 读取配置文件的中数据的配置
def sjk_pz():

    host = con.article(section="Mysql",option="host")
    db = con.article(section="Mysql",option="db")
    pwd = con.article(section="Mysql",option="pwd")
    sjk = [host,db,pwd]
    return sjk

# 继承sql_handel
class sql(My_sql):
    def __init__(self):
        super().__init__(host=sjk_pz()[0],
                         db=sjk_pz()[1],
                         pwd =sjk_pz()[2])
sql = sql()


if __name__ == '__main__':
    check = 'select * from test_res where test_id=1'
    c=sql.check(check)
    print(c)



