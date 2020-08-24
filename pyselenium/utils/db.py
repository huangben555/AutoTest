import configparser
import pymysql.cursors


class db:

    @staticmethod
    def db_connect(cmdopt):
        cfg = configparser.ConfigParser()
        cfg.read('C:\\PycharmProjects\\AutoTest\\pyselenium\\config.ini', encoding='utf-8')
        print('cmdopt值为：', cmdopt)
        db_host = cfg.get(cmdopt, 'db_host')
        db_port = cfg.get(cmdopt, 'db_port')
        db_user = cfg.get(cmdopt, 'db_user')
        db_passwd = cfg.get(cmdopt, 'db_passwd')
        db_name = cfg.get(cmdopt, 'db_name')
        db_charset = cfg.get(cmdopt, 'db_charset')
        connect = pymysql.Connect(
            host=db_host,
            port=int(db_port),
            user=db_user,
            passwd=db_passwd,
            db=db_name
        )
        cursor = connect.cursor()
        return connect, cursor

    @staticmethod
    def db_insert():
        connect, cursor = db.db_connect()
        sql = "INSERT INTO `sign_event` VALUES (3, '华为', 200, 1, '上海佘山', '2020-08-06 18:07:35.000000', '2020-03-01 16:10:34')"
        cursor.execute(sql)
        connect.commit()
        cursor.close()
        connect.close()


if __name__ == '__main__':
   db.db_insert()