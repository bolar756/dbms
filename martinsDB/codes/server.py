import time,uuid,string,hashlib,getpass; from useractivate import useractivities,connection,cursor,bankDB
import requests
class bankday(bankDB):
    def __init__(self, userage: float, name: str, usergender: str, userid=0):
        super().__init__(userage, name, usergender, userid)
        return None
    
print("welcome")

url = "https://fitness-calculator.p.rapidapi.com/dailycalorie"

querystring = {"age":"25","gender":"male","height":"180","weight":"70","activitylevel":"level_1"}

headers = {
	"X-RapidAPI-Key": "6993e4c2f3msh0b549f37f4f8d99p1ed0b8jsndd661170d5e9",
	"X-RapidAPI-Host": "fitness-calculator.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())