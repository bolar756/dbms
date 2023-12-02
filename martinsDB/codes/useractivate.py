import time,uuid,string,hashlib,getpass
from martinsbank import connection,cursor,bankDB
class useractivities(bankDB):
    """ welcome to agbabiaka bank"""
    characters=string.punctuation
    def __init__(self,userage=0, name=0,usergender=0,userid=0):
        super().__init__(userage, name,usergender,userid=0)
        startsession= time.ctime()
        sesssionId=uuid.uuid4()
        self.__name=name
        return None
    def useractivate(self):
        command= """CREATE TABLE IF NOT EXISTS details (name VARCHAR, password VARCHAR, time_update VARCHAR)"""
        cursor.execute(command)
        command= """CREATE TABLE IF NOT EXISTS ACTIONS(time VARCHAR, sessionid VARCHAR, purpose VARCHAR, outcome VARCHAR)"""
        cursor.execute(command)
        name = input("input your username ")
        trem=cursor.execute(f"""SELECT username FROM USER """)
        tr = cursor.fetchall()
        cursor.execute("SELECT name FROM details")
        ted= cursor.fetchall()
        for nae in ted: nae
        for nam in tr:tr
        if name in tr:  
             password = input(f'password to access your bank deposits {name} \t')
             password2 = input("confirm password \t")
             past=password.encode(encoding='utf-8')
             ced=hashlib.sha256(past)
             if password == password2:
                 if len(password) > 8:
                   for der in list(self.characters):
                      if der in list(password): 
                          pat="sucessful"
                          cursor.execute(f""" INSERT INTO ACTIONS  VALUES('{time.ctime()}', '{uuid.uuid4()}','account activation','{pat}')""")
                      else:
                          print("password has no characaters")
                 else: 
                    print("succesful account creation")   
                    cursor.execute(f"""INSERT INTO details VALUES ('{name}','{ced.hexdigest()}','{time.ctime()}')""")
             else:
                 print("password not matching") 
        elif name in nae:
            print("account activated previously")
            exit()           
        else:
            pat="failed"
            print("account does not exist")
            cursor.execute(f""" INSERT INTO ACTIONS  VALUES('{time.ctime()}', '{uuid.uuid4()}','account activation','{pat}')""")  
        connection.commit()                
        return ''
    def login(self):
       username = input("enter username\t ")
       def checkbalance():
          fact =(1)
          cursor.execute(f"SELECT amount FROM {username}")
          cerd=cursor.fetchall()
          for ist in cerd:           
            fact=ist+fact 
          return fact
       def deposit():
           command= f""" CREATE TABLE IF NOT EXISTS {username} (amount INTEGER , nin VARCHAR, date VARCHAR, sessionid VARCHAR )"""
           cursor.execute(command)
           amount = input("amount for deposit with # or $ dollar coming first")
           nin =input("enter reason for deposit")
           cursor.execute(f"INSERT INTO {username} VALUES ('{amount}', '{nin}', '{time.ctime()}', '{uuid.uuid4()}')")
           print("see you soon")
           return ''
       def withdraw():
          print("welcome {}".format(username))
          amount=int(input("how much do you wanna withdraw"))
          cursor.execute(f"""INSERT INTO {username} VALUES ('{amount}' ,'withdrawal', '{time.ctime()}', '{uuid.uuid4()}')""")
          print("see you soon")
          return ''
       def transfer():
          print("welcome mr/mrs/miss {}".format(username))
          amount = int(input("enter the amount to be transfered"))
          recipient=input("enter recepient account name")
          cursor.execute(f"SELECT name FROM details")
          ced= cursor.fetchall()
          for past in ced:past
          if recipient in past:
              command= f""" CREATE TABLE IF NOT EXISTS {recipient} (amount INTEGER , nin VARCHAR, date VARCHAR, sessionid VARCHAR )"""
              cursor.execute(command)
              amount = input("amount for deposit with # or $ dollar coming first")
              cursor.execute(f"INSERT INTO {username} VALUES ('{amount}', 'sent to  {recipient}', '{time.ctime()}', '{uuid.uuid4()}')")
              cursor.execute(f"INSERT INTO {recipient} VALUES ('{amount}', 'received from {username}', '{time.ctime()}', '{uuid.uuid4()}')")
              print("see you soon")
          else:
             print("recipient does not exist")
          connection.commit()      
          return ''
       password= input ("enter ur user password\t")
       pasa=password.encode(encoding='utf-8')
       ced=hashlib.sha256(pasa)
       pas = (ced.hexdigest())
       cursor.execute(f"""SELECT name FROM details """)
       tr = cursor.fetchall()
       cursor.execute(f"SELECT password FROM details")
       past = cursor.fetchall()
       for nam in tr:tr
       for pasr in past: pasr
       if username in nam:
             if pas in  pasr:
              print("sucessfuly signed in")
              print("if you want to deposit enter deposit, to transfer enter transfer ,to withdraw enter withdraw")
              action=input("enter what you want to do \t")
              if action == 'deposit':
                 print(deposit())
              elif action == 'check':
                print(checkbalance())
              elif action == 'withdraw':
                 print(withdraw())
              elif action == 'transfer':
                 print(transfer())  
              else:
                 print("this action does not exist")  
             else:
               print("password is incorrect")  
       else:
           print("username not registered with 🏦MARTIN BANKS")  
           cursor.execute(f""" INSERT INTO ACTIONS  VALUES('{time.ctime()}', '{uuid.uuid4()}','account signin','failed')""")
       connection.commit() 
       return ''
    