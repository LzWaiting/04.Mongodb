from pymongo import MongoClient

# 1. 创建数据库连接
conn = MongoClient('localhost',27017)

# 2. 创建数据库对象
db = conn.stu 
# db = conn['stu']

# 3. 创建集合对象
myset = db.class4
# myset = db['class4']

# 4. 数据操作
# print(dir(myset)	# 获取myset属性

# 插入操作
# myset.insert({'name':'张铁林','King':'乾隆'})	# 插入一条文档
# myset.insert([{'name':'张国立','King':'康熙'},{'name':'陈道明','King':'康熙'}])	# 插入多条文档
# myset.insert_one({'name':'郑少秋','King':'乾隆'})
# myset.insert_many([{'name':'唐国强','King':'雍正'},{'name':'陈建斌','King':'雍正'}])

# 查找操作
# cursor = myset.find({},{'_id':0})	# 可以遍历
# print(cursor)
# for i in cursor:
# 	print(i['name'],'---',i['King'])

# dic = myset.find_one({},{'_id':0})
# print(dic)

# 查找操作符使用
# myset1 = db.class0
# query = {'$or':[{'age':{'$lt':19}},{'gender':'w'}]}
# field = {'_id':0}
# cursor = myset1.find(query,field)
# for i in cursor:
# 	print(i)
# print(cursor.next())
# for i in cursor.skip(2).limit(2):
# 	print(i)
# for i in cursor.sort([('age',1),('name',-1)]):
# 	print(i)

# 修改操作
# myset1 = db.class0
# query = {'name':'Tom'}
# update = {'$set':{'age':20}}
# myset1.update(query,update,multi=True) 

# 如果匹配文档不存在则插入
# query = {'name':'霍建华'}
# update = {'$set':{'King':'乾隆'}}
# myset.update(query,update,upsert=True)
# myset.update_many({'King':'乾隆'},{'$set':{'name':'老年人'}})
# myset.update_one({'King':'康熙'},{'$set':{'Kingname':'玄烨'}})

# 删除操作
# myset.remove({'name':'陈道明'})
# myset.remove({'name':'老年人'},multi=False)
# myset.remove({'King':{'$exists':False}})

# 复合操作
# 查找name='老年人'，并删除
# print(myset.find_one_and_delete({'name':'老年人'}))

# 5. 关闭数据库连接
conn.close()