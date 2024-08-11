
import sqlite3
import que as q
import pandas as pd

#SELEC_ALL = 'SELECT character_id, name FROM charactercreator_character;'


# DB connect functin
def connect_to_db(db_name='rpg_db.sqlite3'):
    return sqlite3.connect(db_name)

def execute_q(conn, query):
    #construct the cursor
    curs = conn.cursor()
    #Execute the cuery
    curs.execute(query)
    #pull and return the result
    return curs.fetchall()


if __name__ =='__main__': 
   conn = connect_to_db()
   #print(execute_q(conn, q.SELEC_ALL)[:5])
   results = execute_q(conn, q.AVG_ITEM_WEIGHT_PER_CHARACTER)
   df = pd.DataFrame(results)
   df.columns = ['name', 'average_item_weight']
   df.to_csv('rgp_dp.csv', index = False)

