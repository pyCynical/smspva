import requests,json

class smsPvaAPI():
	def __init__(self,API_KEY: str):
		self.base_url = "http://smspva.com/priemnik.php"
		self.API_KEY = API_KEY


	def is_json(self,obj):
		try:
			json_object = json.loads(obj)
		except ValueError as e:
			return False
		return True

	def get_balance(self, service):
		params = dict(metod="get_balance",service=service,apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_userinfo(self, service, _id=None,operator=None):
		params = dict(metod="get_balance",service=service,apikey=self.API_KEY) 
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_count(self, service, country=None):
		params = dict(metod="get_count_new",service=service,apikey=self.API_KEY,country=country)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_number(self, country, service):
		params = dict(metod="get_number",country=country,service=service,apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_ban(self, service, _id):
		params = dict(metod="ban", service=service, apikey=self.API_KEY, id=_id)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_sms(self, country, service, _id,sms=None):
		params = dict(metod="get_sms", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_denial(self, country, service, _id):
		params = dict(metod="denial", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_proverka(self, service, number):
		params = dict(metod="get_proverka", service=service, number=number, apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text

	def get_sim(self, service, _id):
		params = dict(metod="balance_sim", service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.base_url,params=params)
		return r.json() if self.is_json(r.text) else r.text


