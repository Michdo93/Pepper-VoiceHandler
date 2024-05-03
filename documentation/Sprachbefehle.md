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
