# smspva
Python wrapper for http://smspva.com
Docs http://smspva.com/new_theme_api.html

You can install this package using git or pip for example -

```
pip install smspva
```
OR

 ```
 git clone git@github.com:pyCynical/smspva
 python setup.py
 ```
 
 Use like this - 
 ```python
from smspva import *
sms_pva = smsPvaAPI(API_KEY)
print(sms_pva.get_balance("opt4"))
```
Available Methods: 

```
get_balance(service)
:param service: Service name from the service list
def get_userinfo(self, service: str = None, _id: int = None, operator: str = None)
get_userinfo(service,_id, operator)
:param service: Optional parameter to include Service name from the service list
:param _id: Optional parameter to include request ID
:param operator: (Additional parameter can be omitted) Beeline_RU, MTS_RU, Megafon_RU, Beeline_KZ, Tele2_KZ, Activ_KZ, Altel_KZ, Lifecell_UA, Kyivstar_UA, Vodafone_UA

get_count(service,country)
:param service: Service name from the service list 
:param country: Optional but you can include the country code

get_number(country, service)
:param country: Country code from country list
:param service: Service name from the service list

get_ban(service, _id)
:param service: Service name from the service list
:param _id: Request ID 

get_sms(country, service, _id, sms)
:param country: Country code from country list 
:param service: Service from service list 
:param _id: Request ID
:param sms: Optional - If you want to get re-SMS without closing the order (Code Refinement), then just on the method get_sms add additional parameter sms=sms

get_denial(country,service,_id)
:param country: Country code from country list 
:param service: Service from service list 
:param _id: Request ID 

get_proverka(service, number)
:param service: Service from service list 
:param number: Number 

get_sim(service _id)
:param service: Service from service list 
:param _id: Request ID 

```