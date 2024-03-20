import subprocess
import time
import requests
from interface import app  # Import the Flask app from flask_app.py

# Start the Flask app
if __name__ == '__main__':
    flask_process = subprocess.Popen(['python', 'interface.py'])

    # Introduce a delay to allow the Flask app to start
    time.sleep(5)  # Adjust the delay time as needed

    # Make a request to the Flask app
    url = 'http://127.0.0.1:5000/events/countWords'
    response = requests.get(url)

    # Check response and print data if successful
    if response.status_code == 200:
        data = response.json()
        print(data)
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")

    # Terminate Flask app process after request is completed
    if flask_process:
        flask_process.terminate()