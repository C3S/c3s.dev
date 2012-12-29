==============
Anforderungen
==============




Ungeordnete Anforderungssammlung
--------------------------------

* Wie soll die Analyse gemacht werden? Wie soll der Zugriff �ber API und die Analyse im Hintergrund funktionieren?
* Geb�hren und K�nstler geh�ren zu einer Verwertungsgesellschaft, �ber die die Betr�ge abgerechnet werden.
	* Entsprechend k�nnen die Betr�ge von der C3S ausgesch�ttet oder bspw. an die GEMA weitergegeben werden.
* Das erste Modul, das fertig werden muss, ist die Mitgliederverwaltung und die Song/Metadaten-Datenbank.
* Probleme mit Veranstalterregistrierung
	* Wenn der Club als Veranstalter registriert ist und der DJ die Playlist �bermitteln soll
	* Veranstalter k�nnte einen DJ/Mitarbeiter zur Veranstaltung hinzuf�gen, sodass dieser die Playlist einreichen kann. Welcher Art ist dieser Person? Sie ist weder Mitglied noch Veranstalter.
	* Benutzerfreundliche L�sung funden, dass auch der DJ die Daten �bermitteln kann. Generierung eines Codes, mit dem die �bermittlung m�glich ist? Authorisierung des DJs?
	* Der Veranstalter k�nnte f�r eine Veranstaltung eine Liste von authorisierten Personen nennen, die Playlisten eintragen d�rfen. Anschlie�end muss er die Eingaben best�tigen.
* Remixes
	* Beteiligung des K�nstlers des verwendeten Werks
	* Remixes von Remixes? Rekursives Problem.
	* Zun�chst solche F�lle nicht verwertbar machen, bis Regelung gefunden ist?
* Online-System f�r Abstimmungen durch die Mitglieder?
	* Wahlcomputer-Problem
	* Geheime und nachvollziehbare elektronische Wahl quasi unm�glich
	* Geheime Wahl aus Transparenzgr�nden ausschlie�en?
* Best�tigung der ordentlichen Mitgliedschaft durch Verwaltung bspw. nach Erhalt des unterschriebenen Vertrags
* Liederdatenbank
	* Bei Datenstrukturen an Discogs orientieren?
* Registrierung auch von GEMA-Mitgliedern und Urhebern, die keiner VG angeh�ren
	* Datenschutzproblematik?
* Standardformate f�r Teile des Systems?
* Was passiert, wenn ein Club oder Konzert keine detaillierte Liste einreichen kann, weil keine angefertigt wurde und sie nicht rekonstruierbar ist? H�herer Pauschalbetrag als Einzelabrechnung ergeben h�tte? W�rde dazu f�hren, dass der Veranstalter sich etwas ausdenkt.
* Verwertung von YouTube und �hnlichem bei Standard-Copyright ohne Creative Commons? Unterschiedliche Verg�tung f�r Wiedergabe bzw. Herunterladen?
* Sampling?
* Manuelles f�hren von Wiedergabelisten (auch mobil)
* Datenschutzprobleme und Datensicherheitsprobleme bei Mitgliederdaten!
* Einnahme von Spenden f�r K�nstler als freiwillige Zahlungen m�glich? Flattr? Paypal?
* Die einzelnen Systeme stellen APIs zur Verf�gung, die von verschiedenen Interfaces benutzt werden k�nnen: Web, App, Services, automatischer Transfer von SoundCloud wie sie es zu Flattr tun, etc.
* Mehrfach vorkommende K�nstlernamen k�nnten ein Problem bei der Zuordnung sein
	* IDs f�r K�nstler?
* Verfolgen, wann welche �nderungen wann und durch wen vorgenommen wurden
	* Mitgliederdaten wurden durch Mitglied/Verwaltung ver�ndert
	* Veranstaltungsort wurde vom Veranstalter ver�ndert
	* Veranstaltungsdaten wurde vom Veranstalter korrigiert
* Schutz gegen Missbrauch auch durch interne Leute (wie bspw. den Datenbankadministrator oder die Verwaltung)
* Registrierung von Werken, die von keiner VG verwertet werden sollen?
* K�nstler sollte die M�glichkeit haben, in einem speziellen Fall, der eigentlich der Abrechnung durch C3S unterliegen w�rde, dies auszuschlie�en. Beweis muss ggf. der C3S gegen�ber durch den Verwertenden erbracht werden, um VG-Vermutung zu entkr�ften, bspw. durch Vorlage eines Vertrags oder Einwilligungserkl�rung des K�nstlers.
	* Mustervertr�ge?
	* M�sste von fachkundigen Juristen erstellt werden
* Benutzer k�nnte Anfrage f�r geb�hrenfreie Nutzung stellen, die der K�nstler beantwortet.
* Das System muss gegen Missbrauch und DOS gesch�tzt werden
	* Nur eine bestimmte Anzahl an Anfragen pro Benutzer pro Zeitraum: gilt f�r Eintr�ge ebenso wie f�r Abfragen
* Das System muss geeignete Authorisierungsmethoden verwenden
	* Mitglieder d�rfen nur ihre eigenen Daten �ndern
	* Verwaltung darf alle Daten �ndern
	* Autorisierung vor der Funktionalit�t unabh�ngig gestalten
* Wie wird sichergestellt, dass Leute, die mitentwickeln, nicht auf alle Daten zugreifen k�nnen oder durch Erweiterungen des Codes Funktionen einbauen, die ihnen das erlaubt?
* Wie werden die Login-Daten zur Datenbank geheim gehalten, wenn der Code versioniert wird?
* Ein Account kann theoretisch alle Rollen einnehmen
* Zu speichernde Daten f�r Mitglieder
* Beitrittserkl�rung und Wahrnehmungsvertrag.
	* Mitgliedskonto muss freigeschaltet werden.
* Mitglieder oder deren Vertreter m�ssen Werke und Bearbeitungen anmelden k�nnen. Die Audiodatei soll hochgeladen werden k�nnen. Metadaten m�ssen eigegeben oder �bertragen werden.
* Lizensierung: CC, keine, besondere; Verwertungsrecht in entsprechende abstrakte Teile zerlegen
* Bestimmten Accounts die Berechtigung geben, Werke zum eigenen Account hinzuzuf�gen? Verlage f�r Musiker?
* M�glichkeit zur Authorisierung von Verlagen oder Management zur Wahrnehmung der Rechte und Abrechnung, etc.
* Rechtevertreter m�ssen ihre K�nstler managen k�nnen und alles f�r sie erledigen k�nnen.
* Historisierung von Daten muss mit deutschem Datenschutz vereinbar sein.
* Wie Komplex sollen Song-Metadaten dargestellt werden? Labels als String oder Objekte?
* Satzung sollte versioniert werden. Es muss gespeichert werden, welche Version der Satzung ein Mitglied akzeptiert hat.
* Acoustic Finerprinting
	* Acoustid (http://acoustid.org)
	* Code Chromaprint (http://acoustid.org/chromaprint)
	* http://en.wikipedia.org/wiki/Acoustic_fingerprint
	* http://wiki.musicbrainz.org/AudioFingerprint
* Anzahl der Werke im GEMA-Repertoire
	* 5 Millionen Werke von 1 Millionen Musikurhebern (http://www.gemazahler.de/gema-faq.html)
	* 5 Minuten pro Werk (gro�z�gig) macht 25.000.000 Minuten.
	* 10.584.000 Bytes pro Minute (WAVE) macht 250.000.000.000.000 (240 TB)
	* Selbst bei MP3 128 kbit (960 KB/Minute) sind es noch 22,3 TB.
* Bilder/Cover f�r Werke?
* Automatische Anbindung an Buchf�hrung (GnuCash in Datenbank?)
* Es sollte bedacht werden, dass es in Zukunft mehr Verwertungsgesellschaften als C3S und GEMA geben kann und dass verschiedene Verwertungsgesellschaften unterschiedliche Nutzungsarten verwerten k�nnten.
* Mitglieder m�ssen Agenturen, Verlage oder Management als Vertreter erkl�ren k�nnen, damit diese in ihrem Auftrag Anmeldung, Abrechnung, etc. vornehmen k�nnen.
* Verfolgbarkeit aller �nderungen pro Benutzer. So wird gut nachvollziehbar, wer welche Eintr�ge gemacht hat. Beispielsweise k�nnte ein Verlag hunderte Benutzer haben, die bestimmte Dinge machen d�rfen. Es ist weder realistisch noch verantwortbar, dass alle Mitarbeiter eines Verlags einen einzigen Account nutzen.
* Abw�rtskompatibilit�t des Fingerprints?
* Backend sollte selbstst�ndig gewissen Konsistenzpr�fungen vornehmen, bspw. buchhalterisch, ob die Aufteilung gewisser Posten in der Summe auch einem erwarteten Wert entspricht.
* Automatische Einpflege von Playlists ist ein Modul, das au�erhalb des Kernsystems existiert und die API benutzt.
* Nutzer sollen Verg�tungsh�he f�r gew�hlte Nutzungsarten selbst vorgeben oder um Nachfrage im speziellen Fall bitten k�nnen.
* Sofortige Zahlung f�r einfache und einmalige Nutzung anbieten? Sofort�berweisung, Paypal, etc.
* Zugriff auf API f�r Webdienste, die Lizenzpflichtigkeit pr�fen wollen (bspw. YouTube oder Facebook).
* Benutzerprofil mit Bild und Repertoire (�hnlich Discogs?).
* Lizenzpakete �ber API abfragen? Daf�r m�sste erst noch ein Format entworfen werden.
* Verwertungsauftrag an die C3S soll widerrufbar sein.
* Playlisten als Audioaufnahme einreichen? Das d�rfte verdammt viel Traffic verursachen.
* Automatische Streamanalyse (gegen Aufschlag) durch C3S?

