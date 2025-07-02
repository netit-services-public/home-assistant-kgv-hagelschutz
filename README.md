# Home Assistant Custom Integration: 
# Hagelschutz einfach automatisch

Diese Integration stellt einen Hagelarlam Sensor `sensor.hagelalarm` bereit, der regelmäßig das Hagelsignal von `meteo.netitservices.com` abruft.
Wichtig: Das Hagelsignal ist ausschliesslich für die Schweiz verfügbar. Um es empfangen zu können, muss vorab eine Registration für die
Teilnahme am kostenlosen Hagelalarm Signal Service bei der jeweiligen Gebäudeversicherung beantragt werden siehe auch: 

https://www.hagelschutz-einfach-automatisch.ch/eigentuemer-verwaltungen/produkt/ich-habe-interesse.html

Allgemeine Informationen zum Produkt "Hagelsschutz einfach automatisch" findes unter:

https://www.hagelschutz-einfach-automatisch.ch/eigentuemer-verwaltungen.html

Erklärvidieo:

https://youtu.be/4TQfq9t-z-M?si=srTs5QX9Dp4_-UdI  

## Home Assistant - Features

- 🧩 Sensor: `hailState` wird ausgelesen
- ⚙️ Konfiguration über UI (`device_id` + `hwtype_id`)
- 🔄 Automatische Aktualisierung (alle 2 Minuten)
- 🌐 Mehrsprachig: DE / EN / FR
- 🔐 Saubere Fehlerbehandlung
- 🛠 Zukunftssicher über Konstante konfigurierbare API-URL

## Installation

1. Repo klonen oder ZIP entpacken
2. Ordner `hagelschutz/` nach `config/custom_components/` kopieren
3. Home Assistant neu starten
4. Integration „Hagelschutz einfach automatisch“ über UI hinzufügen

## Lizenz

MIT License – siehe LICENSE-Datei.
