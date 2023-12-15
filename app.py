from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()  # Lädt die Umgebungsvariablen aus der .env-Datei

app = Flask(__name__)

greeting_message = os.environ.get("GREETING_MESSAGE", "Standardnachricht")

@app.route('/')
def home():
    if greeting_message == "Distance Learning 2 - Containers and Supply Chain Security":
        content = """
        <h1>Implementierung des Konfigurationsfaktors in Unserem Flask-Projekt</h1>
        <p><strong>Verwendung von Umgebungsvariablen:</strong> Anstatt Konfigurationswerte direkt im Code zu hinterlegen, nutzen wir Umgebungsvariablen. Dies bietet mehr Sicherheit und Flexibilität, da wir dadurch dieselbe Codebasis in unterschiedlichen Umgebungen (wie Entwicklung, Test, Produktion) mit variierenden Konfigurationen betreiben können. In unserem Flask-Projekt haben wir dies durch das Auslesen des Werts der Umgebungsvariablen GREETING_MESSAGE umgesetzt. Wenn diese Variable nicht definiert ist, verwenden wir als Standardwert "Standardnachricht".</p>
        <p><strong>Setzen von Umgebungsvariablen:</strong> In unserer lokalen Entwicklungsumgebung setzen wir Umgebungsvariablen entweder direkt oder nutzen eine .env-Datei. Für Produktionsumgebungen bevorzugen wir das Setzen dieser Variablen über Infrastruktur-Konfigurationen wie Docker, Kubernetes oder CI/CD-Pipelines, um eine sichere und angepasste Umgebung zu gewährleisten.</p>
        <p><strong>Berücksichtigung der Supply Chain Security:</strong> Wir legen großen Wert darauf, dass all unsere Abhängigkeiten, wie Flask und andere Python-Bibliotheken, aus sicheren und vertrauenswürdigen Quellen stammen. Die regelmäßige Durchführung von Sicherheitsüberprüfungen und das entsprechende Aktualisieren von Abhängigkeiten sind für uns essenziell, um die Sicherheit und Integrität unserer Anwendung zu gewährleisten.</p>
        """
    else:
        content = "<p>" + greeting_message + "</p>"

    return content

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)