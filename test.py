import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mong_proj"]
mycol = mydb["user"]

data = {'id':123, 'name':'Neil', 'age':80, 'sex':'male'}
mycol.insert(data)
#print(content)
