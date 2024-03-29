import requests
import matplotlib.pyplot as plt
from flask import Flask, render_template_string

app = Flask(__name__)

data_store_url = "http://data-store:5000/data"

data_points = []

def fetch_data():
    response = requests.get(data_store_url)
    return response.json()

def update_data():
    global data_points
    data_points = fetch_data() #Pulls new data

@app.route('/')
def index():
    update_data()
    
    # Generate visualization using data_points
    plt.plot([dp['timestamp'] for dp in data_points], [dp['value'] for dp in data_points]) #These lines will edit data within the plot table
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Time Series Data Visualization')
    
    img_path = '/app/static/plot.png' #this will create an image and a path to access it
    plt.savefig(img_path)
    plt.close()
    
    return render_template_string('<img src="{{ img_path }}" alt="plot">') #this will render HTML template with string using the img_path we created before

if __name__ == '__main__': #Only runs server when script is run directly
    app.run(debug=True, host='0.0.0.0', port=80)