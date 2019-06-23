from pymongo import MongoClient
import gridfs

conn = MongoClient('localhost',27017)

db = conn.grid

# 获取gridfs对象
fs = gridfs.GridFS(db)

f = open('bz.jpg','rb')
# 将内容写入数据库中
fs.put(f.read(),filename='bz.jpg')

conn.close()