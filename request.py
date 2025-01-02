import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'Maximum Wind Speed':19,'Maximum Temperature':17,'Minimum Temperature':14,'Average Temperature':16,'Average Wind Speed':18})

print(r.json())