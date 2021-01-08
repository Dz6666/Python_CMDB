import time, MySQLdb
conn = MySQLdb.connect(host='127.0.0.1', user='python', passwd='python', db='Devops_CMDB', charset='utf8')
cursor = conn.cursor()
conn.close()
