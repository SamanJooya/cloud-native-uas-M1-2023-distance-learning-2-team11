from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Lädt die Umgebungsvariablen aus der .env-Datei

app = Flask(__name__)

greeting_message = os.environ.get("GREETING_MESSAGE", "Standardnachricht")

@app.route('/')
def home():
    return greeting_message

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)