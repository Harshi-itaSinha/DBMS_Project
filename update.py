from datetime import datetime
import mysql.connector
from tracker import Tracker
import time

now = datetime.now()
current_time = now.strftime("%H")

if current_time == '13':
    pass

# Connect to the MySQL server
connection = mysql.connector.connect(user='',
                                     password='',
                                     host='localhost',
                                     database='price_tracker')

# Create a cursor object
cur = connection.cursor()

query = 'select Phone_Number,Expected_Price,Product_url,Product_Name,p.Product_Id from product p,notification n, ' \
        'user u where p.Product_Id = n.Product_Id and u.User_Id = p.User_Id '

cur.execute(query)
data = cur.fetchall()
# connection.commit()

print(data)

# time.sleep(10)
for record in data:
    product_name = record[3]
    product_url = record[2]
    expected_price = record[1]
    phone_number = record[0]
    product_id = record[4]

    print(f'{phone_number} update')

    try:
        track = Tracker(product_name, product_url, expected_price, phone_number)
        price = int(track.Update())
    except:
        pass

    update_product = "UPDATE product SET current_price = %(price)s WHERE Product_Id = %(product_id)s"

    # data_product = (price, product_id)
    # time.sleep(30)
    # cur.execute(update_product,{'price':price,'product_id':product_id})

    print(product_id)

    # select_stmt = "update product set current = WHERE username = %(username)s AND password = %(password)s AND type = %(type)s"
    # cursor.execute(
    #     select_stmt, {'username': username, 'password': password, 'type': type})

    # cur.execute("UPDATE product SET current_price = %s WHERE (Product_Id = %s)", (price, product_id))



    # Commit the changes
    connection.commit()

cur.close()
connection.close()
