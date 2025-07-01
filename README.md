# Hagelschutz Einfach Automatisch

Eine Home Assistant Custom Component zur Integration von Hagelsensor-Daten über die NetIT API.

## Einrichtung

1. Diese Komponente über HACS als benutzerdefiniertes Repository einbinden.
2. Nach der Installation Home Assistant neu starten.
3. Integration über die Benutzeroberfläche hinzufügen („Hagelschutz Einfach Automatisch“) und Device-ID eingeben.

## Sensor

Die Integration erstellt einen Sensor mit dem aktuellen Hagelstatus (`hailState`).

## Quelle

Datenquelle:
```
https://meteo.netitservices.com/api/v0/devices/<device_id>/poll?hwtypeId=188
```