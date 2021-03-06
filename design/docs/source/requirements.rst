﻿============
Requirements
============

This document is a collection requirements for the IT system for the C3S.

It is currently being translation into English.


Possible Strategies
-------------------

* Get members and a repertoire
* Members and repertoire need to exist
* Electronic dance music might be an attractive target market segment for the C3S
	* Electronic dance music is played heavily in night clubs but not part of the mainstream
	* It is therefore underrepresented in flat-rate distribution of licencing fees
	* Night club owners contacted the C3S and signaled support for new and more detailed billing methods 
* Members should give the genre of their music with the registration in order to get an overview over the genres of all members
	* Music for computer games?
	* Club music?
	* Electronic/pop/classic?

	
Overview
--------

* **Account management**: provides abstract and role independent user accounts for the C3S system
* **Member management**: extends the account management by data for members which is needed for the repertoire management
* **Agent management**: agents are authorized by members to handle their interests
* **Repertoire management**: enables members (and their agents) to manage their repertoire
* **Licensee management**: Licensees role for accounts
* **Licence management**: describes the conditions of licences; prices for licensing according to usage type (radio broadcasting, concerts, dj sets, etc.) in usage scale (time, audience, etc.)
* **Licensing management**: describes the action of licencing itself of a work by a licencee in the context of the usage
* **Verrechnungsverwaltung**: stellt die Verrechnungslogik der konkreten Nutzungen dar; für eine Nutzung wird nach den Lizenzbestimmungen ein bestimmtes Entgeld fällig
* **Abrechnungsverwaltung**: die Abrechnung der konkreten Lizenzentgelte mit den Mitgliedern (Werkschaffenden/Lizenzgebern) bzw. Nutzern (Lizenznehmern)
	

Accountverwaltung
-----------------

* Zweck
	* Accounts/Logins werden unabhängig von der Rolle als technischer Zugang zum System verwaltet.
	* Durch OpenLdap werden die logins in verschiedenen Kontexten wiederverwendbar.
* Anwendungsfälle
	* Accounts registriert werden
	* Passwort und E-Mail-Adresse ändern
* Daten
	* E-Mail-Adresse
	* Passwort
	* Anzahl der gezeichneten Anteile (investierende Mitgliedschaft)
* Backend
	* Accounts unabhängig von der Rolle
	* Den Accounts verschiedene Rollen zuweisen (Mitglied/Verwaltung/Veranstalter/Mitarbeiter)
* Notizen
	* Zuweisung könnte aus rechtlichen Gründen nötig sein. Mitglieder müssen vermutlich Vertrag unterschrieben und Beitrag gezahlt haben. Müssen Veranstalter auch einen Vertrag unterschreiben?
	* Ein Account kann theoretisch alle Rollen einnehmen. Eine Person kann gleichzeitig Künstler, Vertreter, Nutzer und Verwalter sein.
	* Ein Account stellt den Zugang für eine natürliche Person zur Verfügung. Diese kann Anteile gezeichnet haben und unterschiedliche (oder keine) Rollen ausüben, wie Mitglied oder Lizenznehmer.


.. list-table:: c3sAccount: List of Attributes
   :widths: 20 20 50
   :header-rows: 1

   * - Name
     - Format
     - Purpose / Description
   * - c3sAccountId
     - String
     - account UUID / primary key (?)
   * - email
     - String
     - email for password recovery
   * - loginName
     - String or UUID ?
     - pseudonym or login name
   * - Password
     - String
     - persons password



Mitgliederverwaltung
--------------------

* Zweck
	* Mitgliedsspezifische Daten und Zusammenhänge werden verwaltet
* Anwendungsfälle
	* Mitgliedsdaten werden verwaltet
	* Mitglieder können ihre Daten ändern
	* Verwaltung kann Mitgliedsdaten ändern
* Daten
	* Mitgliedsnummer
	* Firma?
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
	* Telefonnummer?
	* Handynummer?
	* Version der akzeptierten Satzung
* Backend
	* Account bekommt die Rolle "Mitglied"
	* Personen, Bands, Verlage? Bekommt Mitgliedsnummer und ist dadurch als Mitgliedsentität identifizierbar
	* Kann ein Mitglied aus mehreren Accounts/Personen bestehen, bspw. bei einer Band? Könnten die Bandmitglieder auch einzelne C3S-Mitglieder sein?
* Notizen
	* Satzung sollte versioniert werden
	* Mitglieder müssen Agenturen, Verlage oder Management als Vertreter erklären können, damit diese in ihrem Auftrag Anmeldung, Abrechnung, etc. vornehmen können.
	* Möglichkeit zur Authorisierung von Verlagen oder Management zur Wahrnehmung der Rechte und Abrechnung, etc.
* Fragen/Probleme
	* Registrierung auch von GEMA-Mitgliedern und Urhebern, die keiner VG angehören? (definitiv ja, denn wir sind gesetzlich gehalten, auch menschen, die nicht mitglied der verwertungsgesellschaft sind, eine verwertung zu ermöglichen. fällt dann aber unter 'account'!?)
	* Datenschutzproblematik bei erhobenen Daten?
	* Benutzerprofil mit Bild und Repertoire (ähnlich Discogs)?


.. list-table:: c3sMember: List of Attributes
   :widths: 20 20 50
   :header-rows: 1

   * - Name
     - Format
     - Purpose / Description
   * - c3sId
     - String
     - member UUID / primary key (?)
   * - IsSCEMember
     - Boolean or Integer 
     - membership status related to c3s SCE; boolean iff binary, integer if multiple states possible; or link to special DB?
   * - MemberNumber
     - Integer
     - do we need this? might be more human readable than UUID
   * - Company
     - String or UUID ?
     - name of or reference to a company (or name thereof?)
   * - LastName
     - String
     - persons lastname
   * - FirstName
     - String
     - persons firstname
   * - Address0
     - AddressRecord
     - persons current address

   * - StreetName
     - String
     - persons street name
   * - StreetNumber
     - String
     - persons street number
   * - AddressContd
     - String
     - persons address continued
   * - PostCode
     - String
     - post code
   * - City
     - String
     - place person lives or receives mail
   * - Region
     - String
     - region of address (optional, some places need this)
   * - Country
     - String or Id?
     - country person is situated in

TODO: refactor out address records

	
Vertreterverwaltung
-------------------

* Zweck
	* Daten und Zusammenhänge der Rolle "Vertreter" werden verwaltet
	* Vertreter handeln im Namen von Mitgliedern und regeln in deren Auftrag entsprechende Belange
* Anwendungsfälle
	* Vertreten können sich registrieren und ihre Daten ändern
	* Vertreter können alle (?) Aktionen im Namen ihrer vertretenden Mitglieder durchführen
	* Verwaltung kann Vertreterdaten "korrigieren"
	* Ein Mitglied kann Vertreter für andere Mitglieder sein
* Daten
	* Adresse, etc.?
* Notizen
	* Rechtevertreter müssen ihre Künstler managen können und alles für sie erledigen können.


.. list-table:: c3sRepresentatives: List of Attributes
   :widths: 20 20 50
   :header-rows: 1

   * - Name
     - Format
     - Purpose / Description
   * - c3sRepresentativeId
     - String
     - member UUID / primary key (?)


Repertoireverwaltung
--------------------

.. note:: Werkeverwaltung vs. Lizenzmanagement


* Zweck
	* Zentrale Komponente des Systems
	* Enthält Metadaten, die registrierte Werke beschreiben
* Anwendungsfälle
	* Künstler und Verwaltung können Repertoire eintragen
	* Datei-Upload (Alternative auch Link zur Audiodatei) und -analyse?
	* Fingerprint automatisch erstellen?
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
* Fragen/Probleme
	* Abwärtskompatibilität des Fingerprints?
	* Archivierung der Werke nötig?
		* Anzahl der Werke im GEMA-Repertoire
			* 5 Millionen Werke von 1 Millionen Musikurhebern (http://www.gemazahler.de/gema-faq.html)
			* 5 Minuten pro Werk (großzügig) macht 25.000.000 Minuten.
			* 10.584.000 Bytes pro Minute (WAVE) macht 250.000.000.000.000 (240 TB)
			* Selbst bei MP3 128 kbit (960 KB/Minute) sind es noch 22,3 TB.
		* Archivierung ist höchst sicherheitskritisch, weil ein unbefugter Zugang zu den Daten fatale Folgen hätte. Die Werke müssen wahrscheinlich in CD-Qualität (verlustfrei komprimiert, bspw. FLAC) vorliegen. Sollte eine Sammlung dieser Dateien durch Unbefugte kopiert werden, würden hochqualitative Aufnahmen in großem Umfang kursieren.
	* Nutzer sollen Vergütungshöhe für gewählte Nutzungsarten selbst vorgeben oder um Nachfrage im speziellen Fall bitten können.
	* Durch die Lizenz kann bestimmt werden, dass einige Nutzungsarten bereits grundsätzlich erlaubt sind und daher nicht verwertet werden können. Bspw. erlaubt CC-BY die kommerzielle Wiedergabe und Sendung.
	* Bilder/Cover für Werke?


Lizenznehmerverwaltung
----------------------

* Zweck
	* Die Account-Rolle des Nutzers kann Nutzungsumfelder anlegen, in deren Zusamenhang Werke genutzt werden
* Anwendungsfälle
	* Ein Account bekommt die Rolle des Nutzers/Veranstalters und kann daraufhin 


Lizenzverwaltung
------------------------

* Zweck
	* Nutzer/Veranstalter legen Nutzungskontexte an
		* Radiosendung
		* Konzert
		* Kneipenmusik
		* DJ-Set im Club
		* Einbettung in einen Film
		* Spenden
		* Urheberrechtsabgaben auf Leermedien
		* Pauschalabgaben
		* etc.
* Sammlung von GEMA-Abrechnungsgrundlagen aller möglichen Tarife (zum Überblick)
	* Eintrittspreis
		* Eintrittspreis
		* Prozent der Einnahmen
		* Prozent vom Listenpreis
		* Prozentual
		* Prozentual Roheinnahmen (6 %)
		* Prozentual von Nettobeträgen der Senderechte
	* Publikum
		* Belegschaftsgröße (Anzahl Angestellte = Publikumsgröße)
		* Fassungsvermögen (Anzahl Personen)
		* Gemeindegröße (durchschnittliche Besucher des Hauptgottesdiensts)
		* Publikumsgröße (Anzahl Zuschauer)
		* Publikumsgröße (weitester Hörerkreis)
		* Sitzplätze (Anzahl)
	* Örtlichkeit
		* Anzahl Betriebsstätten
		* Anzahl Empfangsgeräte (10% Aufschlag je zusätzliches Gerät im Zimmer)
		* Anzahl Geräte
		* Anzahl Lautsprecher
		* Anzahl Lautsprecherwagen
		* Anzahl Monitore
		* Anzahl Sitzplätze
		* Anzahl Veranstaltungsplätze
		* Anzahl Zimmer
		* Art (allgemein/Gaststätten und ähnliche/Aufenthaltsräume, Warteräume u.ä. ohne Wirtschaftsbetrieb/Omnibusse)
		* Bereich (Sauna und Sport/Bistro)
		* maximale Anzahl Passagiere
		* Raumgröße (1 m² = 1,5 Personen im Publikum)
		* Raumgröße (im m²)
	* Nutzungsintensität
		* Anzahl Amtsleitungen
		* Anzahl angefangen Zugriffe (je. 10.000)
		* Anzahl Downloads
		* Anzahl Filmvorführungen
		* Anzahl Tage
		* Intensität der Interaktivität des Dienstes (hoch, mittel, niedrig)
		* Musikanteil des Diensts (25/50/75 %)
		* Nutzungszeit pro Monat (mehr als 16 Tage im Monat/weniger als 16 Tage im Monat)
		* Sendezeit (verhältnismäßig, 24/7 = 100%)
		* Spieldauer (Anzahl Sekunden)
	* Darbietungform
		* Anzahl ausübende Künstler (bis zu 9/mehr als 9)
	* Wiedergabemedium
		* Medium (Schallplatte, Musikkassette, Compact Disc, MiniDisc, Digital Compact Cassette)
		* Tonträgerart (Hörfunkwiedergabe/Musik auf Website/Original/Vervielfältigungsstück [gebrannt, MP3, Festplatte, etc.])
		* Tonträgerart (Hörfunkwiedergabe/Original/Vervielfältigungsstück [gebrannt, MP3, Festplatte, etc.])
		* Tonträgerart (Original/Vervielfältigungsstück [gebrannt, MP3, Festplatte, etc.])
* Sammlung von Jamendo-Abrechnungsgrundlagen
	* Jamendo Track (http://pro.jamendo.com/de/product/licensing/prices)
		* Internet
			* Anzahl Seiten (eine/mehrere)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Firma
			* Geografisch (national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Werbung
			* Geografisch (regional, national, internation, national & Internet, nur Internet)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Kurzfilm
			* Geografisch (regional, national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Film
			* Geografisch (national, international)
			* (Dauer nur unbegrenzt)
		* Dokumentarfilm
			* Geografisch (regional, national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Telefonwarteschleife
			* (pro 10 Titel unbegrenzt)
		* TV-Sendung & -Filme
			* Geografisch (regional, national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Darstellende Künste
			* Geografisch (regional, national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Videospiele
			* Wiedergabegerät (Software, Online-Videospiel, Konsole oder PC)
			* (Dauer nur unbegrenzt)
		* Audio
			* Verkauf (kostenlos, Verkauf)
			* (Dauer nur unbegrenzt)
			* (bis zu 45.000 Kopien)
		* Audio-Guide
			* Geografisch (national, international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Radio-Jingle
			* (Geografisch nur international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
		* Multisupport
			* (Geografisch nur international)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)
	* Jamendo Flow (http://pro.jamendo.com/de/product/background/prices)
		* Hintergrundmusik für Handelsflächen oder öffentliche Plätze
			* Gewerbliche Fläche (abhängig von m²)
			* Dauer (1 Jahr, 3 Jahre, unbegrenzt)





Lizensierungsverwaltung
------------------

* Zweck
	* Auflistung, welche Werke in welchem Nutzungsumfeld von welchem Nutzer genutzt wurden
* Anwendungsfälle
	* Übermittlung von Playlists
		* Automatische/Dateien
			* DJ-Software
			* Internet-Radio-Software
			* Übermittlung durch Services wie YouTube
		* Manuelle Eingabe
	* Identifizierung durch Fingerprinting
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

* Anwendungsfälle
	* Verwaltung kann Verrechnungsdetails administrieren
	* Regeln zur Berechnung des Vergütungsentgelds können geändert werden
* Backend
	* Abrechnung inklusive aufeinander basierender Werke (wenn ein Lied auf einem anderen basiert, wird der ursprüngliche Künstler beteiligt)
	* Backend sollte selbstständig gewissen Konsistenzprüfungen vornehmen, bspw. buchhalterisch, ob die Aufteilung gewisser Posten in der Summe auch einem erwarteten Wert entspricht.
	* Was haben die Veranstalter verwertet?
	* Wie wird das von der Verwertung eingenommene Geld verteilt
	* ggf. Verrechnung über GEMA, wenn GEMA-Mitglied und nicht C3S
	* rechtliche Anforderungen an doppelte Buchführung müssen erfüllt werden
		* `Grundsätze ordnungsmäßiger Buchführung (GOB) <https://de.wikipedia.org/wiki/Grunds%C3%A4tze_ordnungsm%C3%A4%C3%9Figer_Buchf%C3%BChrung>`_
		* `§ 5 I EStG <http://www.gesetze-im-internet.de/estg/__5.html>`_
	* Schnittstelle zu Buchhaltungssoftware: GnuCash? Professionelle?


Abrechnungsverwaltung
---------------------

* Anwendungsfälle
	* Einsicht in Abrechnungen
* Notizen/Fragen
	* Wie wird das Geld der Verwertung ausgeschüttet?
	* Einnahmen
	* Mitgliedsbeiträge
	* Überweisung? Wann wie ausgeführt?


Analysen
--------

* Zweck
	* Mitglieder, Nutzer und Verwaltung haben ein Interesse daran, gewisse Fakten über ihre Belange zu erfahren
	* Mitglieder interessieren sich dafür, welche ihrer Werke wann, wo und wie genutzt werden
* Anwendungsfälle
	* Mitglieder
		* Was wurde wann/wo gespielt und hat welche Einahmen generiert?
	* Veranstalter
	* Verwaltung
* Fragen/Notizen
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

* Todo


Allgemeine Fragen und Probleme
------------------------------

* Historisierung von Daten muss mit deutschem Datenschutz vereinbar sein.


Entwicklung
-----------

* Ein geeignetes Web-Application-Framework sollte eingesetzt. Am geeignetsten scheinen derzeit Ruby on Rails und Python.


Datenbankmodellierung
---------------------

* Datenbankprimärschlüssel müssen unabhängig von Identifizierungskennzeichen sein. Beispielsweise darf eine Mitgliedsnummer trotz ihrer Eindeutigkeit nicht als Primärschlüssel verwendet werden. Das ist unabhängig davon, wie wahrscheinlich es ist, dass sich Mitgliedsnummern jemals ändern. Ein Datenbankdesign sollte grundsätzlich unabhängig von äußeren Einflüssen dieser Art sein. Als Primärschlüssel dürfen ausschließlich Surrgatschlüssel (sequenzielle Nummern) verwendet werden.


Ungeordnete Anforderungssammlung
--------------------------------

* "Real-time Dashboard for your account"; slide 31: http://de.slideshare.net/wsenges/cc-global-summit-buenos
* Micropayments, Donations, Voluntary payments; slide 17: http://de.slideshare.net/wsenges/cc-global-summit-buenos
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
* Das System muss gegen Missbrauch und DDOS-Attacken (distributed denial of service) geschützt werden
	* Nur eine bestimmte Anzahl an Anfragen pro Benutzer (Netzwerkteilnehmer/IP-Adresse!?) pro Zeitraum: gilt für Einträge ebenso wie für Abfragen
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
* `DJ Monitor <http://www.djmonitor.com/>`_ als Box zur Analyse von DJ-Sets verwenden?
* Sollten bestimmte Account-Rollen ohne Freischaltung verfügbar sein, bspw. Nutzer? Mitglieder und Vertreter müssen auf jeden Fall freigeschaltet werden! Was bringt es dem einfachen Nutzer; was kann er tun und was will er von dem System?
* Analysen müssen nach gesetzlichen und ggf. anderen Maßstäben anonymisiert werden
* Infrastrukturelle Anforderungen: Der Systementwurf wird der Anforderung Rechnung tragen, dass Änderungen im System nachvollziehbar sein müssen und durch Änderungen keine Daten verloren gehen. Auf infrastruktureller Ebene müssen aber Backups der Datenbanken und Webservices vorgenommen werden und ggf. eine Redundanz für hohe Erreichbarkeit sichergestellt werden.
* Systemstruktur
	* Hardware: Server, Computergehäuse mit Elektronik, Prozessor, RAM, Festplatten, Netzwerkkarte
	* Betriebssystem: Dateisystem, Dateien, Datenbanken
	* Datenbank: Datenmodell, Tabellen
	* Benutzerzugriff: Zugangsverwaltung
	* API: Systemschnittstelle
	* Benutzeroberfläche: Website, GUI, App
* Payment providers: Markus has a contact with professional experience in working with various payment providers who does not want to be officially named
