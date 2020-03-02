"""
============================
Author:luli
time:2020/2/26
company:happy
============================
"""
import pymysql
from common.handleconf import conf


class DB:
    def __init__(self):
        # 创建一个连接对象
        self.conn = pymysql.connect(host=conf.get("db", "host"),
                                    port=conf.getint("db", "port"),
                                    user=conf.get("db", "user"),
                                    password=conf.get("db", "pwd"),
                                    charset=conf.get("db", "charset"),
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        # 创建一个游标
        self.cur = self.conn.cursor()

    def find_one(self, sql):
        """获取查询出来的第一条数据"""
        # 执行查询语句
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchone()
        return data

    def find_all(self, sql):
        """获取查询出来的所有数据"""
        self.conn.commit()
        self.cur.execute(sql)
        data = self.cur.fetchall()
        return data

    def find_count(self, sql):
        """返回查询数据的条数"""
        self.conn.commit()
        return self.cur.execute(sql)

    def delete_data(self, sql):
        self.conn.commit()
        self.cur.execute(sql)
        self.conn.commit()

    def close(self):
        """关闭游标，断开连接"""
        self.cur.close()
        self.conn.close()
