import pymongo
client =pymongo.MongoClient('localhost' ,27017)
ceshi = client['ceshi']
item_info = ceshi['item_infoX']

for i in item_info.find().limit(300):
    print(i)