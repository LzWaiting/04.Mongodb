'''小文件存储方案
直接转换为二进制格式插入到数据库'''
from pymongo import MongoClient
import bson.binary

conn = MongoClient('localhost',27017)

db = conn.image

myset = db.picture

# 存储图片
# with open('bz.jpg','rb') as f:
	# 将图片内容转换为可存储的二进制格式
	# content = f.read()
	# data = bson.binary.Binary(content)

# 插入到文档
# myset.insert({'filename':'bz.jpg','data':data})

# 提取图片
data = myset.find_one({'filename':'bz.jpg'})	# 此时不需要二进制转换，find自动转换
# 将内容写入到本地
with open('bz.jpg','wb') as f:
	f.write(data['data'])

conn.close()