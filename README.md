# smspva
Python wrapper for http://smspva.com

You can install this package using git or pip for example -

```
pip install smspva-api
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
