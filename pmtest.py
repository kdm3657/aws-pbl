import pymysql
import boto3

ssm = boto3.client('ssm')
parameter = ssm.get_parameter(Name='/myweb/database1_password',WithDecryption=True)
db_password = parameter['Parameter']['Value']


conn = pymysql.connect(host='database-1.c1sfhfewzr4b.ap-northeast-2.rds.amazonaws.com',db='pbldb',port=3306,passwd=db_password,user='admin')
print(conn)
# conn.close()

