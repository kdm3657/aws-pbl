import pymysql
conn = pymysql.connect(host='database-1.c1sfhfewzr4b.ap-northeast-2.rds.amazonaws.com',db='pbldb',port=3306,passwd='star!1234',user='admin')
print(conn)
conn.close()