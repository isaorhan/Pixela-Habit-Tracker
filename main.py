import requests
from datetime import datetime

USERNAME = "YOUR USERNAME"
TOKEN = "YOUR SELF GENERATED TOKEN"
GRAPH_ID = "YOUR GRAPH ID"

pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f'{pixela_endpoint}/{USERNAME}/graphs'

headers = {
    "X-USER-TOKEN": TOKEN
}

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
} 			

class CreateUser:
	def __init__(self,token: str,username: str,agreeTermsOfService: str,notMinor: str):
		self.token = token
		self.username = username
		self.agreeTermsOfService = agreeTermsOfService
		self.notMinor = notMinor
		user_params = {
			'token' : self.token,
			'username' : self.username,
			'agreeTermsOfService' : self.agreeTermsOfService,
			'notMinor' : self.notMinor
		}
		response = requests.post(url=pixela_endpoint, json=user_params)
		print(response.text)

class CreateGraph:
	def __init__(self,id:str,name:str,unit:str,typee:str,color:str):
		self.id = id
		self.name = name
		self.unit = unit
		self.typee = typee
		self.color = color

		graph_config = {
	    "id": self.id,
	    "name": self.name,	#Your graph name.
	    "unit": self.unit,  #Km,Hours,Kilos etc.
	    "type": self.typee, #Float,int etc.
	    "color": self.color #You need to write its japenese name like "shibafu (green), momiji (red), sora (blue), ichou (yellow), ajisai (purple) and kuro (black) are supported as color kind."
	    }
	    response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
		print(response.text)
	    
