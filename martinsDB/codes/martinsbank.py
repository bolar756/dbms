import sqlite3,time,uuid
connection=sqlite3.connect('martinsDB/bankserver/bank.db')
cursor=connection.cursor()

class bankDB:
    all=[]
    def __init__(self,userage:float, name:str,usergender:str,userid=0):
        self.userage=userage
        self.__name=name
        self.usergender=usergender
        self.userid=uuid.uuid4()
        #print(f"{self.name} user id {self.userid} created")
        print("checking...")
        bankDB.all.append(self)
        return None
    @property
    #basically sets class name to read-ONLY
    def name(self):
       return self.__name
    def user_init(self):
             commanddb= """ CREATE TABLE IF NOT EXISTS USER(username VARCHAR, usergender TEXT, userdob VARCHAR, userage INTEGER, userid VARCHAR)"""
             cursor.execute(commanddb)
             cursor.execute(f"""SELECT username FROM USER """)
             tr =cursor.fetchall()
             for nam in tr:tr 
             if self.name in nam:
                  print("username exists")
             else:     
              cursor.execute(f"""INSERT INTO USER VALUES( '{self.name}','{self.usergender}','{time.ctime()}','{self.userage}', '{self.userid}') """)
             connection.commit()
             return ''
    def __repr__(self) -> str:
         #self.all = f"'{self.__class__.__name__}'('{self.name}', '{self.__name}','{self.usergender})"
         return f"'{self.__class__.__name__}'('{self.name}', '{self.__name}','{self.usergender})"
    def __internet__(self):
        print("checking for internet connection")
        return ''

    @staticmethod       
    def is_integer(num):
       #we wil count the floats that are point zero
       #for i.e 5.0, 10.0
       if isinstance(num, float):
          #count out the floats that are point zero
          return num.is_integer()
       elif isinstance(num, int):
          return f'{num} is int'
       elif isinstance(num, complex):
          return f"num is  fucking{False}"
       else:
          return False 