# Home Assistant Custom Integration: 
# Hagelschutz einfach automatisch

Diese Integration stellt einen Sensor `sensor.hagelalarm` bereit, der regelmäßig das Hagelsignal von `meteo.netitservices.com` abruft.

## Features

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
