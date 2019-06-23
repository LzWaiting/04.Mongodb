from pymongo import MongoClient

conn = MongoClient('localhost',27017)

db = conn.stu

myset = db.class0

# 索引操作
# index = myset.ensure_index('name')	# 正向索引
# print(index)
# index = myset.ensure_index([('age',-1)])	# 逆向索引

# 获取索引
# for i in myset.list_indexes():
# 	print(i)

# 删除索引
# myset.drop_indexes()
# 删除单个索引
# myset.drop_index('name_1')

# 复合索引
# index = myset.ensure_index([('name',1),('age',-1)])
# 唯一索引
# index = myset.ensure_index('name',name='MyIndex',unique=True) 
# 稀疏索引
# index = myset.ensure_index('age',name='MyIndex',sparse=True)

# 聚合操作
myset1 = db.class4

p = [{'$group':{'_id':'$King','count':{'$sum':1}}},{'$match':{'count':{'$gt':1}}}]
cursor = myset1.aggregate(p)
for i in cursor:
	print(i)

conn.close()