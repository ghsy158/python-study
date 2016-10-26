import pymysql

conn = pymysql.connect(host="172.16.88.187",
                       user='hxerp', password="2wsx3edc",
                       db="pbs191", charset="utf8")
cur = conn.cursor()
cur.execute("use pbs191")

cur.execute("select * from sys_user ")

users = cur.fetchall();
count = 0;
for user in users:
    print(user)
    count += 1;
# print(cur.fetchall())

# print(cur.fetchone())
print("总条数:", count)

cur.close()
conn.close()
