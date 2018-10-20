import requests, json


def is_json(obj):
	try:
		json_object = json.loads(obj)
	except ValueError:
		return False
	return True


class smsPvaAPI():
	def __init__(self,API_KEY):
		self.API_ENDPOINT = "http://smspva.com/priemnik.php"
		self.API_KEY = API_KEY
	
	def check_response(self, resp):
		if resp.status_code != 200 or not is_json(resp.json()):
			return f"There was some problem making the request more info:\nStatus Code: {resp.status_code}\nText: {resp.text}"
		return resp.json()

	def get_balance(self, service):
		params = dict(metod="get_balance",service=service,apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_userinfo(self, service, _id=None,operator=None):
		params = dict(metod="get_userinfo",service=service,apikey=self.API_KEY) 
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_count(self, service, country=None):
		params = dict(metod="get_count_new",service=service,apikey=self.API_KEY,country=country)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_number(self, country, service):
		params = dict(metod="get_number",country=country,service=service,apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_ban(self, service, _id):
		params = dict(metod="ban", service=service, apikey=self.API_KEY, id=_id)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_sms(self, country, service, _id,sms=None):
		params = dict(metod="get_sms", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_denial(self, country, service, _id):
		params = dict(metod="denial", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_proverka(self, service, number):
		params = dict(metod="get_proverka", service=service, number=number, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)

	def get_sim(self, service, _id):
		params = dict(metod="balance_sim", service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return check_response(r)
