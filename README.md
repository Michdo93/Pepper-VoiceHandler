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
|`Sprachsteuerung`|Vollständig, aber nicht ausführlich getestet. Es wird mit einer Wahrscheinlichkeit von 50% gearbeitet, was oft noch nicht einmal erreicht wird und teilweise auch zu falschen Eingaben führt.|
|`calculator.py` / Taschenrechner|Vollständig
|`clock.py` / Digitaluhr|Vollständig|
|`connectfour.py` / 4 Gewinnt!|Vollständig|
|`hangman.py` / Galgenmännchen|Vollständig|
|`memory.py` / Memory|Vollständig|
|`numberguessing.py` / Zahlenratespiel|Vollständig|
|`quiz.py` / Quiz|Vollständig|
|`rockpaperscissors.py` / Schere-Stein-Papier|Vollständig|
|`tictactoe.py` / TicTacToe|Vollständig|
|`wordpuzzle.py` / Wortpuzzle|Vollständig|
|Tanzen|Vollständig|
|Random-Songs abspielen / Singen|Vollständig|
|Random-Bilder darstellen / Malen|Vollständig, aber ungetestet|
|Random-Videos abspielen|Vollständig, aber ungetestet|
|Random-Witze erzählen|Vollsändig|
|Lovestory erzählen|Vollständig, aber ungetestet (bricht glaube ich ab, weil Story zu lang).|
|Rechenaufgaben per Spracheingabe lösen|Vollständig, aber wird durch Spracherkennung nicht richtig erkannt|
|Synonym-Erkennung|Vollständig, aber wird glaube ich nicht richtig durch die Spracherkennung eingesetzt|
|Zahlen aus Spracherkennung extrahieren|Vollständig, aber wird durch Spracherkennung nicht richtig erkannt|
|NAOqi-Applikationen starten/beenden|Vollständig|
|Python-Applikationen starten/beenden|Vollständig|
|Java-Applikationen starten/beenden|Vermutlich vollständig|
|C++-Applikationen starten/beenden|Vermutlich vollständig|
|Den Akkustand durchsagen|Geplant|
|Den Akkustand auf dem Tablet grafisch darstellen|Prototyp|
|Pepper-Controller (JS)|Prototyp|
|openHAB-Anbindung|Prototyp|
|ChatGPT-Anbindung|Geplant|

## Code erweitern

### Spracheingabe

Um die Spracheingabe zu erweitern, muss als nächstes folgendes Vokabular in der `pepper.py` erweitert werden:

```
        vocabulary = ["Hi", "Hallo", "Guten Tag", "Grüß Gott", "Servus", "Moin", "Hey, wie geht's?",
                      "Wie ist deine Stimmung?", "Was gibt's Neues?", "Wer bist du?",
                      "Wie alt bist du?", "Woher kommst du?", "Was machst du hier?", "Bist du ein Roboter?",
                      "Können wir Freunde sein?", "Magst du Fußball?", "Was sind deine Hobbys?", "Kannst du mir helfen?",
                      "Was kannst du tun?", "Hast du Geschwister?", "Wo wohnst du?", "Kannst du kochen?", "Kannst du tanzen?",
                      "Kannst du singen?", "Kannst du rechnen?", "Kannst du malen?", "Kannst du Geschichten erzählen?",
                      "Was ist dein Lieblingsessen?", "Was ist deine Lieblingsfarbe?", "Was ist dein Lieblingsbuch?",
                      "Was ist deine Lieblingsmusik?", "Was ist dein Lieblingsfilm?", "Magst du Tiere?", "Hast du Angst vor etwas?",
                      "Kannst du fliegen?", "Kannst du schwimmen?", "Kannst du laufen?", "Was denkst du über die Welt?",
                      "Was denkst du über Menschen?", "Hast du Träume?", "Was ist dein Ziel?", "Was ist dein Lieblingsort?",
                      "Wie fühlst du dich heute?", "Was war dein schönstes Erlebnis?", "Was war dein traurigstes Erlebnis?",
                      "Kannst du Liebe fühlen?", "Was ist deine Lieblingsjahreszeit?", "Magst du Regen?", "Was würdest du gerne mal machen?", "Erzähl mir einen Witz!",
                      "Was ergibt", "Was sind", "Addiere", "Plus", "Subtrahiere", "Minus", "Multipliziere", "Mal", "Dividiere", "Geteilt durch", "Potenziere", "Hoch", "Wurzel aus",
                      "TicTacToe starten", "TicTacToe beenden",
                      "Vier Gewinnt starten", "Vier Gewinnt beenden",
                      "Digitaluhr starten", "Digitaluhr beenden",
                      "Galgenmännchen starten", "Galgenmännchen beenden",
                      "Memory starten", "Memory beenden",
                      "Zahlenratespiel starten", "Zahlenratespiel beenden",
                      "Quiz starten", "Quiz beenden",
                      "Schere Stein Papier starten", "Schere Stein Papier beenden",
                      "Wort Puzzle starten", "Wort Puzzle beenden",
                      "Taschenrechner starten", "Taschenrechner beenden",
                      "Kannst du mir ein Video zeigen?", "Videowiedergabe beenden", "Kannst du Musik abspielen?", "Musikwiedergabe beenden"
                      ]
```

Eine Schwierigkeit besteht darin, dass Wörter auch aneinander gruppiert werden müssen und nicht zu viele einzeln sein dürfen, weil er sonst Sätze leichter miteinander verwechselt. Auf der anderen Seite müssen einige Vokabeln zwecks "Synonimität" eher einzeln bleiben.

Die Änderung am Vokabular bedingt einen Neustart des Peppers!

Anschließend muss die Überprüfung, welcher Satz gesagt werden soll erweitert werden:

```
elif "meine neue Spracheingabe" in recognized_words:
    # todo
```

In `# todo` muss natürlich die entsprechende Funktionalität hinzugefügt werden. Dies kann selbstverständlich von Sprachausgaben, bis hin zum Starten von Anwendungen, Bewegungen usw. alles sein.

Wenn man mit Synonyme arbeiten möchte, sieht dies wie folgt aus:

```
elif self.check_synonyms(recognized_words, ["Hi", "Hallo", "Guten Tag", "Grüß Gott", "Servus", "Moin"]):
    # todo
```

Ich habe einfach mal ein Beispiel für paar Synoyme gegeben. Diese wären allerdings bereits vorhanden. Die Synoyme werden als `list` übergeben.

Wenn man z.B. eine oder mehrere Zahlen aus einer Spracheingabe extrahieren möchte, empfiehlt es sich z.B. eine Funktion hierfür zu schreiben, und neben den Zahlen im Vokabular auch ein Wort festzulegen, welches definitiv in dem genannten Satz vorkommen muss! Ein Beispiel für zwei Zahlen findet man in den Funktionen `addition`, `substraction`, `multiplication` und `division`. Ein Beispiel für eine Zahl findet man in den Funktionen `potentiation` und `extraction`.

















