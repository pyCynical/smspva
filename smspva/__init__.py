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
	
	def check_response(self, resp) -> dict:
		if resp.status_code != 200 or not is_json(resp.text):
			raise Error(f"There was some problem making the request more info:\nStatus Code: {resp.status_code}\nText: {resp.text}")
		return resp.json()

	def get_balance(self, service: str = None) -> dict:
		params = dict(metod="get_balance",service=service,apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_userinfo(self, service: str = None, _id: int = None, operator: str = None) -> dict:
		params = dict(metod="get_userinfo",service=service,apikey=self.API_KEY) 
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_count(self, service: str , country: str = None) -> dict:
		params = dict(metod="get_count_new",service=service,apikey=self.API_KEY,country=country)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_number(self, country: str, service: str = None) -> dict:
		params = dict(metod="get_number",country=country,service=service,apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_ban(self, service: str, _id: int) -> dict:
		params = dict(metod="ban", service=service, apikey=self.API_KEY, id=_id)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_sms(self, country: str, service: str, _id: int , sms: str = None) -> dict:
		params = dict(metod="get_sms", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_denial(self, country: str, service: str, _id: int) -> dict:
		params = dict(metod="denial", country=country, service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_proverka(self, service: str, number: str) -> dict:
		params = dict(metod="get_proverka", service=service, number=number, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)

	def get_sim(self, service: str, _id: int) -> dict:
		params = dict(metod="balance_sim", service=service, id=_id, apikey=self.API_KEY)
		r = requests.get(self.API_ENDPOINT,params=params)
		return self.check_response(r)
	def get_sms_message(self, country: str, service: str, _id: str) -> dict:
		getCurrentTime = lambda: int(round(time.time() * 1000))
		addTenToCurrent = getCurrentTime() + 600000
		while addTenToCurrent >= getCurrentTime():
			request = self.get_sms(country ,service ,_id)
			if (hasattr(request, "text") and request["text"] != None) or (hasattr(request, "sms") and request["sms"] != None):
				return request 
				break
			time.sleep(20)

