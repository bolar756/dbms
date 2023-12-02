import string,getpass,hashlib,hmac,encodings,time
import time,uuid,string,hashlib,getpass
from martinsbank import connection,cursor,bankDB
xed=cursor.description
password='redetegege'
characters=string.punctuation
for der in list(characters):
  if der in list('est!@#r'):
   print(True)
  else:
    pass 
  
""""ved=getpass.getpass()
#print(ved)

street = 'Gürzenichstraße'
#print(street.casefold())
#red=ved.encode(encoding='utf-8', errors='strict')
#print(red)
#ced=hashlib.sha256(red)
#print(ced.hexdigest())

import base64
#encoded = base64.b64encode(ved)"""

def from_iterable(iterables):
    # chain.from_iterable(['ABC', 'DEF']) --> A B C D E F
    for its in iterables:
        n= sum(iterables)
        return n
red=[12,34,5,6,6]

#for i in range(12):
   #print(sum(range(2)))

def factorial(n):
   fact=1
   for ist in n:           
      fact=ist+fact
   return fact
def factoril(n):
    fact=1
    for i in range(2,n+1):
      fact=i*fact
    return fact   
print(sum(tuple(red)))      