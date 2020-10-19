import configparser
from configparser import ConfigParser
from configuration.path_config import p
class Config:
    def __init__(self):
        self.con = ConfigParser()
        self.con.read(p.con_path(),encoding='utf-8')
    # 查询数据
    def article(self,section,option):
        try:
            art = self.con.get(section,option)
            return art
        except configparser.NoSectionError as error:
            return ('没有对应的{}值'.format(error))
        except configparser.NoOptionError as error:
            return ('没有对应的{}值'.format(error))

    # 修改配置项目方法
    def modify(self,section,option,zhi):
        try:
            self.con[section][option] = zhi
            with open(p.con_path(),'w',encoding='utf-8') as config:
                self.con.write(config)
        except KeyError as error:
            return ('配置文件中key值{}不存在'.format(error))
        except configparser.NoSectionError as error :
            print(error)


con = Config()

if __name__ == '__main__':
    con = Config()
    a = con.article('school','sc_nam')
    print(a)



