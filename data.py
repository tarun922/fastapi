
import hashlib
import secrets

import sqlite3
class Data:
    def __init__(self):
        self.db=sqlite3.connect("data.db")
        self.cur=self.db.cursor()
        self.cur.execute('''create table if not exists data(name varchar(30) not null unique ,key blob not null ,credit int not null );''')
        print("intitlised")

    def get_data(self):
        self.cur.execute("select * from data ;")
        data=self.cur.fetchall()
        data=list(data)
        print(data)
        return {"data":data}

    def get_credit(self, name ):

        self.cur.execute(f"select credit from data where name = '{name}'")
        data=self.cur.fetchall()[0][0]
        print(data)

        return {"credit":data}

    def get_key(self, name ):

        self.cur.execute(f"select key from data where name = '{name}'")
        data=self.cur.fetchall()[0][0]
        print(data)

        return {"key":data}
    def get_user(self, key):
        try:
            self.cur.execute(f"select name from data where key = '{key}'")
            data=self.cur.fetchall()[0][0]
            print(data)

            return {"user":data}
        except:
            return {"error":"not"}

    def set_user(self , name ):
        key=secrets.token_bytes(32)
        hash_object = hashlib.sha256(key)
        hex_dig = hash_object.hexdigest()
        credits=1000
        try :
            self.cur.execute(
            "INSERT INTO data (name, key, credit) VALUES (?, ?, ?)",
            (name, hex_dig, credits)
        )
            self.db.commit()
            return {"name":name,"key":hex_dig , "credits":credits , "message":"ur acc created succesfullyyy make sure to copy the key it won't show again'"}
        except:
            print("alread haii re user ......")
            return {"erreor":"user phele se hai bhai ...."}
    def update_credits(self ,name , addd=0 , sub=0 ):
        try :
            self.cur.execute(f"select credit from data where name ='{name}'")
            cd=self.cur.fetchall()[0][0]
            print(cd)
            mv=addd-sub
            cd=cd+mv
            self.cur.execute(f"update data set credit ={cd} where name = '{name}'")

            self.db.commit()
            print(cd)
            return {"status":"credit updated succesfull " , "new_credit":cd}
        except:
            print("user not exist ")
            return {"error":"user not found "}







 
