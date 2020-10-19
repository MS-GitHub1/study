import pymysql
from comon.log_handel import logger
# 建立连接
from pymysql.cursors import DictCursor


class My_sql():
    def __init__(self,host,db,user="root",pwd=None):
        self.host=host
        self.user=user
        self.pwd=pwd
        self.db=db
        self.con = pymysql.connect(host=self.host, port=3306, user=self.user, password=self.pwd, db=self.db, charset="utf8",
                              cursorclass=DictCursor)

# 添加信息   批量操作信息时候，不要开一次数据库在关一次    cour.close()  self.con.close()   updata 与insert
    def insert_into_data(self,sql):
            try:
                cour=self.con.cursor()
                cour.execute(sql)
                logger.info("更新成功")
                self.con.commit()
            except pymysql.MySQLError as error:
                logger.info("错误信息为{}".format(error))
                self.con.rollback()

#  查询一条信息
    def check(self,sql):
        try:
            with self.con.cursor() as cur :
                res = cur.execute(sql)
                if res ==1:
                    logger.info("查询successful")
                    return cur.fetchone()
                self.con.commit()
        except pymysql.MySQLError as error:
            logger.info("错误信息为{}".format(error))
            # 回滚
            self.con.rollback()
        self.con.cursor().close()
        self.con.close()

#  查询多条信息
    def check_all(self,sql):
        try:
            with self.con.cursor() as cur:
                cur.execute(sql)
                logger.info("查询successful")
                # self.con.commit()
                return cur.fetchall()

        except pymysql.MySQLError as error:
            print(error)

    # def updata(self,sql):
    #     cur = self.con.cursor()
    #     cur.execute(sql)




Mysql = My_sql(host='47.105.48.249',user='root',pwd='Chao1116..',db='data')
# if __name__ == '__main__':
#     Mysql.insert_into_data(sql='insert into name (name,class,age) value ("张起灵","一年級","10")')

