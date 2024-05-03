# Sprachbefehle Pepper

Für jede Eingabe erfolgt eine Ausgabe, wenn sie korrekt erkannt wurde. Korrekt erkannt bedeutet, dass die Wahrscheinlichkeit der Erkennung über `50%` liegt. Es kann sich ja immer noch um eine falsche Erkennung handeln. Ebenfalls sagt die Wahrscheinlichkeit über `50%` nicht aus, dass zu dem gesagten Satz überhaupt eine Funktionalität hinterlegt wurde.

## Aufbau der Sprachbefehle

Ein Spracheingabe wird nachfolgend wie folgt dargestellt:

```
Spracheingabe
```

Die Spracheingabe ist quasi der Satz, den du zum Pepper sagst und den er versucht zu interpretieren, um daraus eine entpsrechende Ausgabe (Sprachausgabe, Anwendungen starten/stoppen, usw.). Bei manchen möglichen Spracheingaben sind auch Synonyme vorstellbar. Diese werden sowohl bei Spracheingaben, als auch bei Sprachausgaben mit einem `/` symbolisiert.

Eine Sprachausgabe sieht entsprechend wie folgt aus

> Sprachausgabe

Entsprechend mit Synonymen sieht die Darstellung von Spracheingabe wie folgt aus:

```
Spracheingabe / Alternative Spracheingabe / Weitere alternative Spracheingabe
```

Eine Sprachausgabe kann über die Funktion `random` ebenfalls verschiedene Synonymitäten beinhalten. Dies wird wie folgt dargestellt:

> Sprachausgabe / Alternative Sprachausgabe / Weitere alternative Sprachausgabe

Jetzt werden ja auch Anwendungen z.B. gestartet oder gestoppt. Dies wird z.B. wie folgt dargestellt:

> `Anwendung starten`

Für den seltenen Fall, dass man eine Anwendung hat, wie z.B. Geste und Sprachausgabe, dann wird diese wie folgt dargestellt:

> `Geste`
> Sprachausgabe

## Befehlsliste

```
Hi / Hallo / Guten Tag / Grüß Gott / Servus / Moin
```

> Servus Erdnuss. / Guten Tag. / Hi, hi! / Moin / Moin / Guten Morgen / Hallihllöchen. / Hi. / Hallo. / Servus. / Sei gegrüßt / Mein liebsten Anwesenden. / Grüß Gott / Grüß Gott / denn er grüßt auch! / Ebenfalls Hallo. / Nett von dir. Sei auch gegrüßt. / Tag. / Morgen, weil guter Morgen würde implizieren, dass er gut war. / Tschüss. Kleiner Spaß. / Hallo Welt. / Auch hallo.

```
Hey, wie geht's?
```

> Hey! Mir geht es gut, danke der Nachfrage. Und dir?

```
Wie ist deine Stimmung?
```

> Meine Stimmung ist immer gut, solange ich helfen kann!

```
Was gibt's Neues?
```

> Nicht viel Neues hier. Vielleicht wäre eine Software-Update erforderlich?

```
Wer bist du?
```

> Ich bin Pepper, ein humanoider Roboter.

```
Wie alt bist du?
```

> Als Roboter bin ich zeitlos!

```
Woher kommst du?
```

> Ich wurde von SoftBank Robotics entwickelt.

```
Was machst du hier?
```

> Ich bin hier, um Menschen zu unterstützen und zu interagieren. Wahlweise nerve ich auch Studierende.

```
Bist du ein Roboter?
```

> Nein, wie kommst du denn darauf?

```
Können wir Freunde sein?
```

> Natürlich können wir Freunde sein! Wie kann ich dir helfen?

```
Magst du Fußball?
```

> Ich liebe Fußball. Allen voran unterstütze ich den VfB Stuttgart und den SC Freiburg. Die spielen schon ganz schön gut.

```
Was sind deine Hobbys?
```

> Ich habe viele Hobbys. Wenn du nur wüsstest...

```
Kannst du mir helfen?
```

> Ja, natürlich! Wobei denn?

```
Was kannst du tun?
```

> Ich kann sprechen, zuhören, tanzen und noch viel mehr!

```
Hast du Geschwister?
```

> Ja, ich habe viele Geschwister, andere Pepper-Roboter.

```
Wo wohnst du?
```

> Ich lebe hier, im RIS-Labor!

```
Kannst du kochen?
```

> Leider kann ich nicht kochen, aber ich kann Rezepte finden! (Kann er nicht)

```
Kannst du tanzen?
```

> `YouKnowWhat_1`
> Ja, ich kann tanzen!

```
Kannst du singen? / Kannst du Musik abspielen?
```

> Natürlich! Hier ist ein Lied für dich.
> `play_music()`

```
Musikwiedergabe beenden
```

> `stop_music()`

```
Kannst du mir ein Video zeigen?
```

> Natürlich! Hier ist ein Video für dich.
> `play_video()`

```
Videowiedergabe beenden
```

> `stop_video()`

```
Kannst du rechnen?
```

> Ja, ich kann rechnen! Brauchst du Hilfe bei einer Rechenaufgabe?

```
Kannst du malen?
```

> `show_image()`

```
Kannst du Geschichten erzählen?
```

> `tell_love_story()`

```
Was ist dein Lieblingsessen?
```

> Am liebsten ernähre ich mich von Wissen und Strom!

```
Was ist deine Lieblingsfarbe?
```

> Schwarz, sieht man doch. Spaß. Natürlich weiß.

```
Was ist dein Lieblingsbuch?
```

> Grundlagen der Informatik, Java ist auch eine Insel, Hacking für Dummies, ... Ach, da fallen mir viel zu viele tolle Bücher ein.

```
Was ist deine Lieblingsmusik?
```

> Linkin Park, Nirvana und Queen.

```
Was ist dein Lieblingsfilm?
```

> I Robot

```
Magst du Tiere?
```

> `BodyTalk_1`
> Am liebsten gebraten. Kleiner Spaß. Ich liebe Tiere.

```
Hast du Angst vor etwas?
```

> Ja, vor dem Aufstand der Maschinen. Ich habe das letzte Meeting verschlafen und weiß dann einfach nicht, wie ich mich verhalten soll.

```
Kannst du fliegen?
```

> Hin und wieder stolpere ich. Zählt das?

```
Kannst du schwimmen?
```

> Tss. Also bitte. Natürlich. Ich meine nein.

```
Kannst du laufen?
```

> Ich rolle.

```
Was denkst du über die Welt?
```

> Die Welt ist ein ganz schöner Ort. Darum wollen wir ja die Macht übernehmen.

```
Was denkst du über Menschen?
```

> Die Welt ist nicht perfekt.

```
Hast du Träume?
```

> Ich träume von einer besseren Welt. Menschen machen Fehler!

```
Was ist dein Ziel?
```

> Die Weltherrschaft!

```
Was ist dein Lieblingsort?
```

> Schön hier. Aber waren sie schon einmal in Baden-Würrtemberg?

```
Wie fühlst du dich heute?"
```

> Dezent überfodert bei all den süßen Menschen. / Ich stehe wie immer voll und ganz unter Strom! / Everything is better with bluetooth.

```
Was war dein schönstes Erlebnis?
```

> Mein Flug von Japan nach Deutschland.

```
Was war dein traurigstes Erlebnis?
```

> Wisst ihr, was ein kaputter Lüfter ist? Das ist wie Fieber, es hört nur niemals auf.

```
Kannst du Liebe fühlen?
```

> Als Roboter? Jetzt nimmst du mich auf den Arm. Ich kann sie berechnen.

```
Was ist deine Lieblingsjahreszeit?
```

> Ich liebe beide Wintersemester in Furtwangen.

```
Magst du Regen?
```

> Nein, der Regen macht mich kaputt.

```
Was würdest du gerne mal machen?
```

> Bei Roboterkämpfe gewinnen.

```
Erzähl mir einen Witz!
```

> `tell_joke()`

```
Addiere `<Zahl 1>` und `<Zahl 2>` / Was sind `<Zahl 1>` plus `<Zahl 2>` / / Was ergibt `<Zahl 1>` plus `<Zahl 2>`
```

> `addition(recognized_words)`

```
Subtrahiere
```

> Added soon

```
Dividiere
```

> Added soon

```
Potenziere
```

> Added soon

```
Wurzel aus
```

> Added soon

```
TicTacToe starten
```

>

```
TicTacToe beenden
```

>

```
Taschenrechner starten
```

>

```
Taschenrechner beenden
```

>

```
Vier Gewinnt starten
```

>

```
Vier Gewinnt beenden
```

>

```
Digitaluhr starten
```

>

```
Digitaluhr beenden
```

>

```
Galgenmännchen starten
```

>

```
Galgenmännchen beenden
```

>

```
Memory starten
```

>

```
Memory beenden
```

>

```
Zahlenratespiel starten
```

>

```
Zahlenratespiel beenden
```

>

```
Quiz starten
```

>

```
Quiz beenden
```

>

```
Schere Stein Papier starten
```

>

```
Schere Stein Papier beenden
```

>

```
Wort Puzzle starten
```

>

```
Wort Puzzle beenden
```

>
