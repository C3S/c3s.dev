Physikalisches Datenmodell
==========================


Ungeordnete Notizen
-------------------

* `Data Vault Modeling <https://en.wikipedia.org/wiki/Data_Vault_Modeling>`_ (DVM) ist ein in der Datenbankmodellierung verhältnismäßig neuartige Methode, die eine Reihe von Vorteilen gegenüber anderen Praktiken hat. Insbesondere sind die Historisierung und Verfolgbarkeit von Daten ein wichtiger Aspekt. Weiterhin wird Wert auf Ladegeschwindigkeit und Erweiterbarkeit gelegt. Auf der anderen Seite führt DVM zu einem hohen Grad an Normalisierung, was zwar bei der Beladung der Daten Vorteile hat, bei der Nutzung und Auslesung aber zu einem Resourcen-Mehraufwand führt, um die normalisierten Daten wieder zusammenzuführen.
	* Mitglied mit Mitgliedsnummer als natürlichem Schlüssel
	* Historisierung aller Daten
		* besonders bei Verrechnungspraxis sehr wichtig, dass bei Änderungen die neue Praxis verwendet wird
	* Eigenen Satelliten für Metadaten
		* Wer hat welchen Datensatz wann verändert (Typ-2 eingefügt)?

