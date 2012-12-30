Physikalisches Datenmodell
==========================


Ungeordnete Notizen
-------------------

* `Data Vault Modeling <https://en.wikipedia.org/wiki/Data_Vault_Modeling>`_ (DVM) ist ein in der Datenbankmodellierung verh�ltnism��ig neuartige Methode, die eine Reihe von Vorteilen gegen�ber anderen Praktiken hat. Insbesondere sind die Historisierung und Verfolgbarkeit von Daten ein wichtiger Aspekt. Weiterhin wird Wert auf Ladegeschwindigkeit und Erweiterbarkeit gelegt. Auf der anderen Seite f�hrt DVM zu einem hohen Grad an Normalisierung, was zwar bei der Beladung der Daten Vorteile hat, bei der Nutzung und Auslesung aber zu einem Resourcen-Mehraufwand f�hrt, um die normalisierten Daten wieder zusammenzuf�hren.
	* Mitglied mit Mitgliedsnummer als nat�rlichem Schl�ssel
	* Historisierung aller Daten
		* besonders bei Verrechnungspraxis sehr wichtig, dass bei �nderungen die neue Praxis verwendet wird
	* Eigenen Satelliten f�r Metadaten
		* Wer hat welchen Datensatz wann ver�ndert (Typ-2 eingef�gt)?

