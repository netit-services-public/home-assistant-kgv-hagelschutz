# home-assistant-kgv-hagelschutz
Automatisieren Sie Ihre Storensteuerung bei Hagelalarm – ganz ohne manuelle Wetterbeobachtung!
Diese Integration bindet das Hagelschutz-Signal der kantonalen Gebäudeversicherungen (Schweiz) direkt in Home Assistant ein.


Installation über HACS - Assistant Community Store ( HACS ) eine benutzerdefinierte Integration, die eine Benutzeroberfläche zum Verwalten benutzerdefinierter Elemente in Home Assistant bereitstellt.

Voraussetzung: HACS installiert?

1. Ist HACS bereits installiert?
	•	Wenn ja: Wechseln Sie im linken Menü zu HACS
	•	Wenn nein: Hier finden Sie die offizielle Anleitung zur HACS-Installation
    
   https://www.hacs.xyz/docs/use/configuration/basic/#setting-up-the-hacs-integration


2. Öffne HACS in Home Assistant  
3. Gehe zu **Integrationen → 3 Punkte → Benutzerdefiniertes Repository hinzufügen**  
4. Füge folgendes Repository ein:

   https://github.com/netit-services-public/home-assistant-kgv-hagelschutz

5. Wähle Typ: **Integration**
6. Nach dem Hinzufügen → Integration wie gewohnt installieren
7. Danach unter **„Integration hinzufügen“** aktivieren

## Konfiguration

Beim Einrichten geben Sie bitte folgende Werte an:

| Feld | Beschreibung |
|------|--------------|
| **Device ID** | Ihre persönliche 12-stellige Geräte-ID (von der KGV) |
| **hwtypeId**  | Optional (Standard: `188`, bei Home Assistant üblich) |

## Sensor

Die Integration erstellt eine Entität:  
`sensor.hagelalarm`

Mögliche Werte:

-`0` → Kein Hagel
-`1` → Hagelalarm
-`2` → Testalarm 

z. B. über meteo.netitservices.com oder über andere Möglichkeiten ( Link Informationen ) Ihrer Kantonalen Gebäudeversicherung

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.  
Nutzung auf eigene Verantwortung. Kein Anspruch auf Support oder Funktion in jeder Umgebung.

## Links

- Projektseite: [hagelschutz-einfach-automatisch.ch](https://hagelschutz-einfach-automatisch.ch/)
- Berner Gebäudeversicherung: [fachstelle-naturgefahren.ch](https://fachstelle-naturgefahren.ch/de/hagel/hagelschutz.html)

## Beitragende

Ein Projekt aus der Praxis – für die Praxis.  
Mit Unterstützung von [NetIT Services](https://www.netit-services.ch), basierend auf Kundenfeedback und realen Testinstallationen.
