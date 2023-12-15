Implementierung des Konfigurationsfaktors in Ihrem Flask-Projekt
Verwendung von Umgebungsvariablen:
Anstatt Konfigurationswerte direkt im Code zu hinterlegen, nutzen Sie Umgebungsvariablen. Dies bietet mehr Sicherheit und Flexibilität, da Sie dieselbe Codebasis in unterschiedlichen Umgebungen (wie Entwicklung, Test, Produktion) mit verschiedenen Konfigurationen betreiben können. In Ihrem Flask-Projekt haben Sie dies umgesetzt, indem Sie den Wert der Umgebungsvariablen GREETING_MESSAGE auslesen. Falls diese Variable nicht definiert ist, wird als Standardwert "Standardnachricht" verwendet.

Setzen der Umgebungsvariablen
In der lokalen Entwicklungsumgebung können Sie Umgebungsvariablen direkt setzen oder eine .env-Datei verwenden. In Produktionsumgebungen ist es besser, diese Variablen über die Infrastruktur-Konfiguration, wie Docker, Kubernetes oder CI/CD-Pipelines, zu setzen.

Berücksichtigung der Supply Chain Security
Verwendung vertrauenswürdiger Abhängigkeiten:
Achten Sie darauf, dass alle Ihre Abhängigkeiten, wie Flask und andere Python-Bibliotheken, aus sicheren und vertrauenswürdigen Quellen stammen. Führen Sie regelmäßig Sicherheitsüberprüfungen durch und aktualisieren Sie Ihre Abhängigkeiten entsprechend.

Team 11 
Saman Jooya
Alexander Schottleitner