import requests
import time
import random
from datetime import datetime

data_store_url = "http://data-store:5000/data"

while True:
    timestamp = datetime.utcnow().isoformat() #creates a datetime in UTC and puts in in ISO format (YYYY-MM-DDTHH:MM:SS)
    value = random.uniform(0, 100) #This creates a variable, value, that will hold a random floating point number between 0 and 100
    
    payload = {"timestamp": timestamp, "value": value} #This creates a dictionary named payload with data that can be sent in a JSON string
    requests.post(data_store_url, json=payload) #This uses the library "requests" to the data_store_url with payload dictionary
    
    time.sleep(3)  #Creates a timer to refresh data