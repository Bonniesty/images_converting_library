import pymysql
password = "210000nian"
keyword='cool'

#mysql dbc
def dbc():
    try:
        db = pymysql.connect("localhost","root", password,"db_proj");
    except Exception as e:
        print('error!please check mysql connection!')
        raise e
    return db

def search(keyword):
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

    print("\nThe label appears in the follwing account:")
    if result:
        print(result)
    else:
        print("No account have this label!")

def stat():
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
    print("\nMost 10 popular descriptors:")
    print(data2)



if __name__ == '__main__':
    search(keyword)
    stat()
