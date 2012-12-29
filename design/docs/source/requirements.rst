==============
Anforderungen
==============




Ungeordnete Anforderungssammlung
--------------------------------

* Wie soll die Analyse gemacht werden? Wie soll der Zugriff über API und die Analyse im Hintergrund funktionieren?
* Gebühren und Künstler gehören zu einer Verwertungsgesellschaft, über die die Beträge abgerechnet werden.
	* Entsprechend können die Beträge von der C3S ausgeschüttet oder bspw. an die GEMA weitergegeben werden.
* Das erste Modul, das fertig werden muss, ist die Mitgliederverwaltung und die Song/Metadaten-Datenbank.
* Probleme mit Veranstalterregistrierung
	* Wenn der Club als Veranstalter registriert ist und der DJ die Playlist übermitteln soll
	* Veranstalter könnte einen DJ/Mitarbeiter zur Veranstaltung hinzufügen, sodass dieser die Playlist einreichen kann. Welcher Art ist dieser Person? Sie ist weder Mitglied noch Veranstalter.
	* Benutzerfreundliche Lösung funden, dass auch der DJ die Daten übermitteln kann. Generierung eines Codes, mit dem die Übermittlung möglich ist? Authorisierung des DJs?
	* Der Veranstalter könnte für eine Veranstaltung eine Liste von authorisierten Personen nennen, die Playlisten eintragen dürfen. Anschließend muss er die Eingaben bestätigen.
* Remixes
	* Beteiligung des Künstlers des verwendeten Werks
	* Remixes von Remixes? Rekursives Problem.
	* Zunächst solche Fälle nicht verwertbar machen, bis Regelung gefunden ist?
* Online-System für Abstimmungen durch die Mitglieder?
	* Wahlcomputer-Problem
	* Geheime und nachvollziehbare elektronische Wahl quasi unmöglich
	* Geheime Wahl aus Transparenzgründen ausschließen?
* Bestätigung der ordentlichen Mitgliedschaft durch Verwaltung bspw. nach Erhalt des unterschriebenen Vertrags
* Liederdatenbank
	* Bei Datenstrukturen an Discogs orientieren?
* Registrierung auch von GEMA-Mitgliedern und Urhebern, die keiner VG angehören
	* Datenschutzproblematik?
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
* Wie wird sichergestellt, dass Leute, die mitentwickeln, nicht auf alle Daten zugreifen können oder durch Erweiterungen des Codes Funktionen einbauen, die ihnen das erlaubt?
* Wie werden die Login-Daten zur Datenbank geheim gehalten, wenn der Code versioniert wird?
* Ein Account kann theoretisch alle Rollen einnehmen
* Zu speichernde Daten für Mitglieder
* Beitrittserklärung und Wahrnehmungsvertrag.
	* Mitgliedskonto muss freigeschaltet werden.
* Mitglieder oder deren Vertreter müssen Werke und Bearbeitungen anmelden können. Die Audiodatei soll hochgeladen werden können. Metadaten müssen eigegeben oder übertragen werden.
* Lizensierung: CC, keine, besondere; Verwertungsrecht in entsprechende abstrakte Teile zerlegen
* Bestimmten Accounts die Berechtigung geben, Werke zum eigenen Account hinzuzufügen? Verlage für Musiker?
* Möglichkeit zur Authorisierung von Verlagen oder Management zur Wahrnehmung der Rechte und Abrechnung, etc.
* Rechtevertreter müssen ihre Künstler managen können und alles für sie erledigen können.
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
	* 5 Minuten pro Werk (großzügig) macht 25.000.000 Minuten.
	* 10.584.000 Bytes pro Minute (WAVE) macht 250.000.000.000.000 (240 TB)
	* Selbst bei MP3 128 kbit (960 KB/Minute) sind es noch 22,3 TB.
* Bilder/Cover für Werke?
* Automatische Anbindung an Buchführung (GnuCash in Datenbank?)
* Es sollte bedacht werden, dass es in Zukunft mehr Verwertungsgesellschaften als C3S und GEMA geben kann und dass verschiedene Verwertungsgesellschaften unterschiedliche Nutzungsarten verwerten könnten.
* Mitglieder müssen Agenturen, Verlage oder Management als Vertreter erklären können, damit diese in ihrem Auftrag Anmeldung, Abrechnung, etc. vornehmen können.
* Verfolgbarkeit aller Änderungen pro Benutzer. So wird gut nachvollziehbar, wer welche Einträge gemacht hat. Beispielsweise könnte ein Verlag hunderte Benutzer haben, die bestimmte Dinge machen dürfen. Es ist weder realistisch noch verantwortbar, dass alle Mitarbeiter eines Verlags einen einzigen Account nutzen.
* Abwärtskompatibilität des Fingerprints?
* Backend sollte selbstständig gewissen Konsistenzprüfungen vornehmen, bspw. buchhalterisch, ob die Aufteilung gewisser Posten in der Summe auch einem erwarteten Wert entspricht.
* Automatische Einpflege von Playlists ist ein Modul, das außerhalb des Kernsystems existiert und die API benutzt.
* Nutzer sollen Vergütungshöhe für gewählte Nutzungsarten selbst vorgeben oder um Nachfrage im speziellen Fall bitten können.
* Sofortige Zahlung für einfache und einmalige Nutzung anbieten? Sofortüberweisung, Paypal, etc.
* Zugriff auf API für Webdienste, die Lizenzpflichtigkeit prüfen wollen (bspw. YouTube oder Facebook).
* Benutzerprofil mit Bild und Repertoire (ähnlich Discogs?).
* Lizenzpakete über API abfragen? Dafür müsste erst noch ein Format entworfen werden.
* Verwertungsauftrag an die C3S soll widerrufbar sein.
* Playlisten als Audioaufnahme einreichen? Das dürfte verdammt viel Traffic verursachen.
* Automatische Streamanalyse (gegen Aufschlag) durch C3S?

