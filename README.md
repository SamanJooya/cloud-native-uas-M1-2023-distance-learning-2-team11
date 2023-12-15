Implementierung des Konfigurationsfaktors in Unserem Flask-Projekt

Verwendung von Umgebungsvariablen:
Anstelle von direkt im Code hinterlegten Konfigurationswerten setzen wir auf die Nutzung von Umgebungsvariablen. Diese Methode bietet erhöhte Sicherheit und Flexibilität, da wir dadurch dieselbe Codebasis in unterschiedlichen Umgebungen (wie Entwicklung, Test und Produktion) mit variierenden Konfigurationen betreiben können. In unserem Flask-Projekt haben wir dies durch das Auslesen des Werts der Umgebungsvariablen GREETING_MESSAGE umgesetzt. Wenn diese Variable nicht definiert ist, verwenden wir als Standardwert "Standardnachricht".

Setzen von Umgebungsvariablen:
In unserer lokalen Entwicklungsumgebung setzen wir Umgebungsvariablen entweder direkt oder nutzen eine .env-Datei. Für Produktionsumgebungen bevorzugen wir das Setzen dieser Variablen über Infrastruktur-Konfigurationen wie Docker, Kubernetes oder CI/CD-Pipelines, um eine sichere und angepasste Umgebung zu gewährleisten.

Berücksichtigung der Supply Chain Security:
Wir legen großen Wert darauf, dass all unsere Abhängigkeiten, wie Flask und andere Python-Bibliotheken, aus sicheren und vertrauenswürdigen Quellen stammen. Die regelmäßige Durchführung von Sicherheitsüberprüfungen und das entsprechende Aktualisieren von Abhängigkeiten sind für uns essenziell, um die Sicherheit und Integrität unserer Anwendung zu gewährleisten.


Team 11 
Saman Jooya
Alexander Schottleitner