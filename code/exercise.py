from pymongo import MongoClient
import random

conn = MongoClient('localhost',27017)

db = conn.grade

myset = db['class']

# 1. 为所有人添加分数域，值为字典
# cursor = myset.find()
# for i in cursor:	
# 	(ch,ma,en) = random.sample(range(60,101),3)
# 	query = {'_id':i['_id']}
# 	update = {'$set':{'score':{'chinese':ch,'math':ma,'english':en}}}
# 	myset.update(query,update)

# 2. 按照性别分组统计每组人数
# p = [{'$group':{'_id':'$sex','count':{'$sum':1}}}]

# 3. 统计每名男生的语文成绩
# p = [{'$match':{'sex':'m'}},{'$project':{'_id':0,'name':1,'sex':1,'score.chinese':1}}]


# 4. 将女生按照英语成绩降序排列
# p = [{'$match':{'sex':'w'}},{'$sort':{'score.english':-1}}]

# 显示内容
for i in myset.aggregate(p):
	print(i)

conn.close()