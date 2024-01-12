import requests
import time
import random
from datetime import datetime

data_store_url = "http://data-store:5000/data"

while True:
    timestamp = datetime.utcnow().isoformat()
    value = random.uniform(0, 100)
    
    payload = {"timestamp": timestamp, "value": value}
    requests.post(data_store_url, json=payload)
    
    time.sleep(5)  # Adjust the interval as needed