# Pepper-VoiceHandler

Ein Beispiel, wie man Peppers `ASR` (`ALSpeechRecognition`) verwendet. Dies ist eine bereits vom Hersteller vortrainierte Spracherkennung für den Pepper. Man muss die Sprache auswählen und ein entsprechendes Vokabular, kann dann sobald ein Wort/Satz erkannt wurde, eine Fallunterscheidung machen und entscheiden, wie der Roboter damit umgehen soll. Wichtig anzumerken ist, dass auf dem Pepper nur ein einziges Programm, d.h. nicht mehrere parallel, ausgeführt werden können, die `ASR` nutzen. Dies bedeutet, dass wenn man z.B. das Programm direkt nachdem Hochfahren ausführbar macht, dass man kein weiteres Programm manuell starten kann, bevor man dieses nicht manuell beendet hat. Des Weiteren bedeutet dies, dass wenn man sehr verschiedene Spracheingaben umsetzen möchte, dass man all dies in einem zentralen Programm tun sollte, anstelle von mehreren.

Es wird die NAOqi-Version 2.5 verwendet!

## Funktionalität

Der Voice Handler (Voice Command Handler) kann folgendes nach Spracheingaben auslösen:

- Auf ca. 50 Fragen/Sätze reagieren, wie z.B. wie es dir geht, wer du bist usw. (Auch hier wir zum Teil `random` verwendet, damit er nicht immer gleich antwortet.)
- Kann per `random` eines von 10 Songs abspielen bzw. "singen".
- Kann per `random` eines von 4 Bildern im Tablet darstellen bzw. "malen".
- Kann per `random` eines von 4 Videos im Tablet abspielen.
- Kann per `random` einen von 10 vordefinierten Witze erzählen.
- Kann eine Lovestory erzählen mit Gesten.
- Kann per Spracheingabe einfache Rechenaufgaben lösen (Addition, Subtraktion, Multiplikation, Division, Exponentiation, Radikation).
- Kann im Tablet einen Taschenrechner darstellen.
- Kann im Tablet eine Digitaluhr darstellen (Das er die aktuelle Uhrzeit, den aktuellen Tag etc. durchsagt, soll noch hinzugefügt werden.).
- Kann im Tablet 8 verschiedene Spiele anbieten.
- Kann bei Spracheingaben auf vordefinierte Synonyme reagieren (Wird z.T. bei den 50 Fragen/Sätze angewandt. Man muss jedoch bedenken, dass der Entwickler die Synonyme festlegt und man sich nicht spontan bei Spracheingaben wahllos neue aussucht und ausprobiert.).
- Kann bei Spracheingaben aus Sätzen eine Zahl bzw. zwei Zahlen extrahieren (Wird bei den einfachen Rechenaufgaben angewandt.).
- Kann NAOqi-Applikationen starten und beenden, wenn richtig eingebunden.
- Kann Python-, Java-, oder C++-Applikationen über `subprocess.Popen` starten und über `os.kill` beenden.

### Weitere geplante Funktionalitäten

- Den Akkustand durchsagen.
- Den Akkustand auf dem Tablet grafisch darstellen.
- Eine einfache Steuerung des Peppers auf dem Tablet über JavaScript.
- Ein Smart Home System mittels openHAB bedienen (teilweise fertig).
- Einbindung von ChatGPT, um auf unbekannte, d.h. nicht vordefinierte, Spracheingaben zu reagieren (Grundgerüst erstellt).

Um andere Anwendungen zu starten, muss jeweils ein eigenes Python-Skript hinzugefügt werden. Um z.B. die gleichnamigen Anwendungen auf dem Tablet zu starten gibt es folgende Python-Dateien:

- `calculator.py` / Taschenrechner
- `clock.py` / Digitaluhr
- `connectfour.py` / 4 Gewinnt!
- `hangman.py` / Galgenmännchen
- `memory.py` / Memory
- `numberguessing.py` / Zahlenratespiel
- `quiz.py` / Quiz
- `rockpaperscissors.py` / Schere-Stein-Papier
- `tictactoe.py` / TicTacToe
- `wordpuzzle.py` / Wortpuzzle

## Entwicklungsstand

|Funktionalität|Stand|
|---|---|
|`Sprachsteuerung`|Vollständig, aber ungetestet|
|`calculator.py` / Taschenrechner|Vollständig
|`clock.py` / Digitaluhr|Vollständig|
|`connectfour.py` / 4 Gewinnt!|Schrift zu klein, Spielfeld kann man als blauen Strich erahnen|
|`hangman.py` / Galgenmännchen|Vollständig|
|`memory.py` / Memory|Spielkarten werden noch falsch dargestellt|
|`numberguessing.py` / Zahlenratespiel|Vollständig|
|`quiz.py` / Quiz|Frage und Antwortmöglichkeiten werden nicht eingeblendet|
|`rockpaperscissors.py` / Schere-Stein-Papier|Result wird nicht eingeblendet|
|`tictactoe.py` / TicTacToe|Es fehlt der 1-Spieler-Modus gegen den Computer, gegen einen 2. Spieler kann man spielen|
|`wordpuzzle.py` / Wortpuzzle|Es fehlt die Darstellung des zu erratenden Wortes|
|Random-Songs abspielen|Vollständig, aber ungetestet|
|Random-Bilder darstellen|Vollständig, aber ungetestet|
|Random-Videos abspielen|Vollständig, aber ungetestet|
|Random-Witze erzählen|Vollsändig, aber ungetestet|
|Lovestory erzählen|Vollständig, aber ungetestet|
|Rechenaufgaben per Spracheingabe lösen|Vollständig, aber ungetestet|
|Synonym-Erkennung|Vollständig|
|Zahlen aus Spracherkennung extrahieren|Vollständig|
|NAOqi-Applikationen starten/beenden|Vollständig|
|Python-Applikationen starten/beenden|Vollständig|
|Java-Applikationen starten/beenden|Vermutlich vollständig|
|C++-Applikationen starten/beenden|Vermutlich vollständig|
|Den Akkustand durchsagen|Geplant|
|Den Akkustand auf dem Tablet grafisch darstellen|Prototyp|
|Pepper-Controller (JS)|Prototyp|
|openHAB-Anbindung|Prototyp|
|ChatGPT-Anbindung|Geplant|

