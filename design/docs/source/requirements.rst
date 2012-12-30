==============
Anforderungen
==============


Accountverwaltung
-----------------

* Backend
	* Accounts unabhängig von der Rolle
	* Den Accounts verschiedene Rollen zuweisen (Mitglied/Verwaltung/Veranstalter/Mitarbeiter)
	* Zuweisung könnte aus rechtlichen Gründen nötig sein. Mitglieder müssen vermutlich Vertrag unterschrieben und Beitrag gezahlt haben. Müssen Veranstalter auch einen Vertrag unterschreiben?
* Daten
	* E-Mail-Adresse
	* Passwort
* Frontend
	* Accounts können ihr Passwort und die E-Mail-Adresse ändern
* Notizen
	* Ein Account kann theoretisch alle Rollen einnehmen. Eine Person kann gleichzeitig Künstler, Vertreter, Nutzer und Verwalter sein.


Mitgliederverwaltung
--------------------

* Welche Personen sind als Mitglieder registriert?
* Backend
	* Personen, Bands, Verlage? Bekommt Mitgliedsnummer und ist dadurch als Mitgliedsentität identifizierbar.
	* Kann ein Mitglied aus mehreren Accounts/Personen bestehen, bspw. bei einer Band? Könnten die Bandmitglieder auch einzelne C3S-Mitglieder sein?
* Daten
	* Name
	* Vorname
	* Straße
	* Hausnummer
	* Adresszusatz
	* PLZ
	* Ort
	* Land
	* Geburtsdatum
	* Geburtsort?
	* E-Mail-Adresse
	* Bankverbindung
	* Einzugsermächtigung?
	* Anzahl der gezeichneten Anteile
	* Telefonnummer?
	* Handynummer?
	* Version der akzeptierten Satzung
* Frontend
	* Mitglieder können ihre Daten ändern
	* Verwaltung kann Mitgliedsdaten ändern
	* Web/App/etc.
* Notizen
	* Satzung sollte versioniert werden. Es muss gespeichert werden, welche Version der Satzung ein Mitglied akzeptiert hat.
	* Mitglieder müssen Agenturen, Verlage oder Management als Vertreter erklären können, damit diese in ihrem Auftrag Anmeldung, Abrechnung, etc. vornehmen können.
	* Möglichkeit zur Authorisierung von Verlagen oder Management zur Wahrnehmung der Rechte und Abrechnung, etc.
* Fragen/Probleme
	* Registrierung auch von GEMA-Mitgliedern und Urhebern, die keiner VG angehören?
	* Datenschutzproblematik bei erhobenen Daten?
	* Benutzerprofil mit Bild und Repertoire (ähnlich Discogs)?

	
Vertreterverwaltung
-------------------

* Daten
	* Anzahl der gezeichneten Anteile (investierende Mitgliedschaft)
* Notizen
	* Rechtevertreter müssen ihre Künstler managen können und alles für sie erledigen können.


Repertoireverwaltung
--------------------

* Welche Lieder sind zur Vertretung durch die C3S registriert?
* Backend
	* Künstler
	* Lieder
		* Metadaten (an Discogs orientieren?)
			* Interpret?
			* Titel
			* Jahr
			* Stilrichtung
			* Urheber
			* Tags
			* Acoustic Finerprinting
				* Acoustid (http://acoustid.org)
				* Code Chromaprint (http://acoustid.org/chromaprint)
				* http://en.wikipedia.org/wiki/Acoustic_fingerprint
				* http://wiki.musicbrainz.org/AudioFingerprint
		* Lizenz (CC BY/SA/NC/ND, andere, keine)
		* Zuständige Verwertungsgesellschaft (C3S, GEMA, andere, keine)
		* Verwertungsarten (was soll welche VG wahrnehmen)
			* Airplay
			* Club/Kneipe
			* Film/Werbung
			* (an GEMA orientieren)
* Fontend
	* Künstler und Verwaltung können Repertoire eintragen
	* Datei-Upload (Alternative auch Link zur Audiodatei) und -analyse 
* Fragen/Probleme
	* Abwärtskompatibilität des Fingerprints?
	* Anzahl der Werke im GEMA-Repertoire
		* 5 Millionen Werke von 1 Millionen Musikurhebern (http://www.gemazahler.de/gema-faq.html)
		* 5 Minuten pro Werk (großzügig) macht 25.000.000 Minuten.
		* 10.584.000 Bytes pro Minute (WAVE) macht 250.000.000.000.000 (240 TB)
		* Selbst bei MP3 128 kbit (960 KB/Minute) sind es noch 22,3 TB.
	* Nutzer sollen Vergütungshöhe für gewählte Nutzungsarten selbst vorgeben oder um Nachfrage im speziellen Fall bitten können.
	* Durch die Lizenz kann bestimmt werden, dass einige Nutzungsarten bereits grundsätzlich erlaubt sind und daher nicht verwertet werden können. Bspw. erlaubt CC-BY die kommerzielle Wiedergabe und Sendung.
	* Bilder/Cover für Werke?


Nutzerverwaltung
----------------------

* Welche Nutzer/Veranstalter sind registriert?


Nutzungsumfeldverwaltung
------------------------

* Veranstalter legen Nutzungskontexte an
	* Radiosendung
	* Konzert
	* Kneipenmusik
	* DJ-Set im Club
	* Einbettung in einen Film
	* Spenden
	* Urheberrechtsabgaben auf Leermedien
	* Pauschalabgaben
	* etc.
* Daten zum Veranstaltungsort
	* Größe?
* Daten zur Veranstaltung selbst
	* Anzahl der Personen?
	* Dauer?


Nutzungsverwaltung
------------------
* Backend
	* Verwertungen
		* Abspielung analog/digital (Club, Kneipe, Radio, YouTube-Stream, Party)
			* Einreichen von Playlists durch Veranstalter/DJ?
		* Aufführung (Konzert, Videoeinbettung?)
		* Download, Filmeinbettung, Werbungseinbettung, Flattr, Spenden, etc.
	* Leermedien
	* Pauschale Beteiligungen/GEZ?
	* Spenden (Flattr/Paypal)?
	* Auch Übermittlung zur und von der GEMA
* Frontend
	* Übermittlung von Playlists
		* Automatische/Dateien
			* DJ-Software
			* Internet-Radio-Software
			* Übermittlung durch Services wie YouTube
		* Manuelle Eingabe
	* Identifizierung durch Fingerprinting
* Notizen
	* Sofortige Zahlung für einfache und einmalige Nutzung anbieten? Sofortüberweisung, Paypal, etc.
* Fragen/Probleme
	* Playlisten als Audioaufnahme einreichen? Das dürfte sehr viel Traffic verursachen.
	* Wenn der Club als Veranstalter registriert ist und der DJ die Playlist übermitteln soll
	* Veranstalter könnte einen DJ/Mitarbeiter zur Veranstaltung hinzufügen, sodass dieser die Playlist einreichen kann. Welcher Art ist dieser Person? Sie ist weder Mitglied noch Veranstalter.
	* Benutzerfreundliche Lösung funden, dass auch der DJ die Daten übermitteln kann. Generierung eines Codes, mit dem die Übermittlung möglich ist? Authorisierung des DJs?
	* Der Veranstalter könnte für eine Veranstaltung eine Liste von authorisierten Personen nennen, die Playlisten eintragen dürfen. Anschließend muss er die Eingaben bestätigen.

	
Verrechnungsverwaltung
----------------------
* Backend
	* Abrechnung inklusive aufeinander basierender Werke (wenn ein Lied auf einem anderen basiert, wird der ursprüngliche Künstler beteiligt)
	* Backend sollte selbstständig gewissen Konsistenzprüfungen vornehmen, bspw. buchhalterisch, ob die Aufteilung gewisser Posten in der Summe auch einem erwarteten Wert entspricht.
	* Was haben die Veranstalter verwertet?
	* Wie wird das von der Verwertung eingenommene Geld verteilt
	* ggf. Verrechnung über GEMA, wenn GEMA-Mitglied und nicht C3S
	* Automatische Anbindung an Buchführung (GnuCash in Datenbank?)
	* rechtliche Anforderungen an doppelte Buchführung müssen erfüllt werden
		* `Grundsätze ordnungsmäßiger Buchführung (GOB) <https://de.wikipedia.org/wiki/Grunds%C3%A4tze_ordnungsm%C3%A4%C3%9Figer_Buchf%C3%BChrung>`_
		* `§ 5 I EStG <http://www.gesetze-im-internet.de/estg/__5.html>`_
* Frontend
	* Für Verwaltung?


Abrechnungsverwaltung
---------------------
* Backend
	* Wie wird das Geld der Verwertung ausgeschüttet?
	* Einnahmen
	* Mitgliedsbeiträge
	* Überweisung? Wann wie ausgeführt?
* Frontend
	* Einsicht in Abrechnungen


Analysen
--------

* Mitglieder
	* Was wurde wann/wo gespielt und hat welche Einahmen generiert?
* Veranstalter
* Verwaltung
* API muss wahrscheinlich sehr speziell auf Analysen zugeschnitten sein, um konkrete Analysen zu unterstützen
* Benutzerdefinierte Auswertung der Daten ist aus Sicherheitsgründen keine gute Idee


Online-Abstimmungssystem?
-------------------------

* Online-System für Abstimmungen durch die Mitglieder?
	* Wahlcomputer-Problem
	* Geheime und nachvollziehbare elektronische Wahl quasi unmöglich
	* Geheime Wahl aus Transparenzgründen ausschließen?

	
API
---

* Lizenzpakete über API abfragen? Dafür müsste erst noch ein Format entworfen werden
* Zugriff auf API für Webdienste, die Lizenzpflichtigkeit prüfen wollen (bspw. YouTube oder Facebook)


Erweiterbarkeit
---------------


Allgemeine Fragen und Probleme
------------------------------

* Historisierung von Daten muss mit deutschem Datenschutz vereinbar sein.


Ungeordnete Anforderungssammlung
--------------------------------

* Gebühren und Künstler gehören zu einer Verwertungsgesellschaft, über die die Beträge abgerechnet werden.
	* Entsprechend können die Beträge von der C3S ausgeschüttet oder bspw. an die GEMA weitergegeben werden.
* Das erste Modul, das fertig werden muss, ist die Mitgliederverwaltung und die Song/Metadaten-Datenbank.
* Remixes
	* Beteiligung des Künstlers des verwendeten Werks
	* Remixes von Remixes? Rekursives Problem.
	* Zunächst solche Fälle nicht verwertbar machen, bis Regelung gefunden ist?
* Bestätigung der ordentlichen Mitgliedschaft durch Verwaltung bspw. nach Erhalt des unterschriebenen Vertrags
* Standardformate für Teile des Systems?
* Was passiert, wenn ein Club oder Konzert keine detaillierte Liste einreichen kann, weil keine angefertigt wurde und sie nicht rekonstruierbar ist? Höherer Pauschalbetrag als Einzelabrechnung ergeben hätte? Würde dazu führen, dass der Veranstalter sich etwas ausdenkt.
* Verwertung von YouTube und ähnlichem bei Standard-Copyright ohne Creative Commons? Unterschiedliche Vergütung für Wiedergabe bzw. Herunterladen?
* Sampling?
* Manuelles führen von Wiedergabelisten (auch mobil)
* Datenschutzprobleme und Datensicherheitsprobleme bei Mitgliederdaten!
* Einnahme von Spenden für Künstler als freiwillige Zahlungen möglich? Flattr? Paypal?
* Die einzelnen Systeme stellen APIs zur Verfügung, die von verschiedenen Interfaces benutzt werden können: Web, App, Services, automatischer Transfer von SoundCloud wie sie es zu Flattr tun, etc.
* Mehrfach vorkommende Künstlernamen könnten ein Problem bei der Zuordnung sein
	* IDs für Künstler?
* Verfolgen, wann welche Änderungen wann und durch wen vorgenommen wurden
	* Mitgliederdaten wurden durch Mitglied/Verwaltung verändert
	* Veranstaltungsort wurde vom Veranstalter verändert
	* Veranstaltungsdaten wurde vom Veranstalter korrigiert
* Schutz gegen Missbrauch auch durch interne Leute (wie bspw. den Datenbankadministrator oder die Verwaltung)
* Registrierung von Werken, die von keiner VG verwertet werden sollen?
* Künstler sollte die Möglichkeit haben, in einem speziellen Fall, der eigentlich der Abrechnung durch C3S unterliegen würde, dies auszuschließen. Beweis muss ggf. der C3S gegenüber durch den Verwertenden erbracht werden, um VG-Vermutung zu entkräften, bspw. durch Vorlage eines Vertrags oder Einwilligungserklärung des Künstlers.
	* Musterverträge?
	* Müsste von fachkundigen Juristen erstellt werden
* Benutzer könnte Anfrage für gebührenfreie Nutzung stellen, die der Künstler beantwortet.
* Das System muss gegen Missbrauch und DOS geschützt werden
	* Nur eine bestimmte Anzahl an Anfragen pro Benutzer pro Zeitraum: gilt für Einträge ebenso wie für Abfragen
* Das System muss geeignete Authorisierungsmethoden verwenden
	* Mitglieder dürfen nur ihre eigenen Daten ändern
	* Verwaltung darf alle Daten ändern
	* Autorisierung vor der Funktionalität unabhängig gestalten
* Beitrittserklärung und Wahrnehmungsvertrag.
	* Mitgliedskonto muss freigeschaltet werden.
* Mitglieder oder deren Vertreter müssen Werke und Bearbeitungen anmelden können. Die Audiodatei soll hochgeladen werden können. Metadaten müssen eigegeben oder übertragen werden.
* Lizensierung: CC, keine, besondere; Verwertungsrecht in entsprechende abstrakte Teile zerlegen
* Bestimmten Accounts die Berechtigung geben, Werke zum eigenen Account hinzuzufügen? Verlage für Musiker?
* Wie Komplex sollen Song-Metadaten dargestellt werden? Labels als String oder Objekte?
* Es sollte bedacht werden, dass es in Zukunft mehr Verwertungsgesellschaften als C3S und GEMA geben kann und dass verschiedene Verwertungsgesellschaften unterschiedliche Nutzungsarten verwerten könnten.
* Verfolgbarkeit aller Änderungen pro Benutzer. So wird gut nachvollziehbar, wer welche Einträge gemacht hat. Beispielsweise könnte ein Verlag hunderte Benutzer haben, die bestimmte Dinge machen dürfen. Es ist weder realistisch noch verantwortbar, dass alle Mitarbeiter eines Verlags einen einzigen Account nutzen.
* Automatische Einpflege von Playlists ist ein Modul, das außerhalb des Kernsystems existiert und die API benutzt.
* Verwertungsauftrag an die C3S soll widerrufbar sein.
* Entwicklung
	* Wie wird sichergestellt, dass Leute, die mitentwickeln, nicht auf alle Daten zugreifen können oder durch Erweiterungen des Codes Funktionen einbauen, die ihnen das erlaubt?
	* Wie werden die Login-Daten zur Datenbank geheim gehalten, wenn der Code versioniert wird?

