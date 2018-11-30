import pymysql
import pymongo
from collections import Counter
password = " "
keyword='hair'


#mysql dbc
def dbc():
    try:
        db = pymysql.connect("localhost","root", password,"db_proj");
    except Exception as e:
        print('error!please check mysql connection!')
        raise e
    return db
#mongo dbc
def mbc():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["mongo_proj"]
    mycol = mydb["label"]
    return mycol

def search(keyword):
    #mysql search
    db = dbc()
    cursor = db.cursor()
    sql = 'SELECT twtaccount_id FROM label WHERE labels like "%{}%"'.format(keyword)
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except Exception as e:
        print("Error: unable to fetch data")
        raise e

    result=[]
    for i in data:
        if not i[0] in result:
            result.append(i[0])

    print("\nThe label of mysql appears in the follwing account:")
    if result:
        print(result)
    else:
        print("No account in mysql have this label!")

    #mongo search
    col = mbc()
    data1 = col.find({'labels':keyword})

    result=[]
    for i in data1:
        if not i['twtaccount_id'] in result:
            result.append(i['twtaccount_id'])

    print("\nThe label of mongo appears in the follwing account:")
    if result:
        print(result)
    else:
        print("No account in mongo have this label!")






def stat():
    #mysql
    db = dbc()
    cursor = db.cursor()
    sql1 = 'SELECT twtaccount_id,count(*) FROM label GROUP BY twtaccount_id'
    sql2 = 'SELECT labels,count(*) FROM label GROUP BY labels order by count(*) desc limit 10'
    try:
        cursor.execute(sql1)
        data1 = cursor.fetchall()
        cursor.execute(sql2)
        data2 = cursor.fetchall()
    except Exception as e:
        print("Error: unable to fetch data")
        raise e
    print("\nAccount & Number of labels")
    print(data1)
    print("\nMost 10 popular descriptors in mySQL:")
    print(data2)

    #mongodb
    col = mbc()
    data1 = col.find()
    result=[]

    for i in data1:
        result.append(i['labels'])
    print("\nMost 10 popular descriptors in mongoDB:")
    print(Counter(result).most_common(10))

if __name__ == '__main__':
    search(keyword)
    stat()
