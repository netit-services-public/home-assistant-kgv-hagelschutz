# Home Assistant Custom Integration:  
# Hagelschutz einfach automatisch

Diese Integration stellt einen Sensor `sensor.hagelalarm` bereit, der regelmäßig das Hagelsignal von [`meteo.netitservices.com`](https://meteo.netitservices.com) abruft.

> **Hinweis:**  
> Das Hagelsignal ist ausschließlich für die Schweiz verfügbar.  
> Vor der Nutzung ist eine Registrierung bei der Gebäudeversicherung erforderlich:  
> [Zur Anmeldung für den kostenlosen Hagelalarm-Service](https://www.hagelschutz-einfach-automatisch.ch/eigentuemer-verwaltungen/produkt/ich-habe-interesse.html)

Weitere Informationen zum Produkt **„Hagelschutz einfach automatisch“** findest du unter:   
https://www.hagelschutz-einfach-automatisch.ch/eigentuemer-verwaltungen.html

**Erklärvideo auf YouTube**:  
[https://youtu.be/4TQfq9t-z-M](https://youtu.be/4TQfq9t-z-M?si=srTs5QX9Dp4_-UdI)

---

## Features

- `hailState` Sensor zur Anzeige des aktuellen Hagelstatus
- Konfiguration über Home Assistant UI (`device_id` + optional `hwtype_id`)
- Automatische Aktualisierung alle 2 Minuten
- Mehrsprachigkeit: Deutsch / Englisch / Französisch
- Fehlerbehandlung bei API-Zugriff integriert
---

## Installation (via HACS empfohlen)

### Voraussetzungen

- Home Assistant Version ≥ 2025.6.0  
- [HACS (Home Assistant Community Store)](https://hacs.xyz) ist eingerichtet

### Schritt-für-Schritt:

1. **HACS öffnen → Integrationen**
2. Klicke auf `⋮` (oben rechts) → **Benutzerdefinierte Repositories**
   - Repository: `https://github.com/<DEIN-REPO>/hagelschutz`
   - Typ: **Integration**
3. Suche in HACS nach **Hagelschutz einfach automatisch** und installiere die Integration
4. **Home Assistant neu starten**
5. Gehe zu **Einstellungen → Geräte & Dienste → Integration hinzufügen**
   - Wähle **Hagelschutz einfach automatisch** aus der Liste
6. Trage `device_id` ein (Pflicht) + optional `hwtype_id`

---

## Manuelle Installation (nur für Entwickler)

1. ZIP herunterladen oder Repository klonen
2. Ordner `hagelschutz/` nach `config/custom_components/` kopieren
3. Home Assistant neu starten
4. Integration im UI wie oben hinzufügen

---

## Lizenz

MIT License – siehe [LICENSE](./LICENSE)
