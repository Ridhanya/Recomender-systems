import requests
to_predict_dict = {'person_id':50}

url = 'http://127.0.0.1:8000'
r = requests.post(url,json=to_predict_dict); r.json()