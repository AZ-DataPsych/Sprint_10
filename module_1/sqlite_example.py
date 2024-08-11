# Step 0 import sqlite
import sqlite3
import queries as q
# step 1
# connect to database
connection = sqlite3.connect('rpg_db.sqlite3')

# step 2
cursor = connection.cursor() 

# step 3 write a query

 

# step 4 pulling the result from the cursor
results = cursor.execute(q.SELEC_ALL).fetchall()

if __name__ =='__main__': 
    print(results[:5])