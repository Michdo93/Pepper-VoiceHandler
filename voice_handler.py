# -*- coding: utf-8 -*-
import qi
import subprocess
import re
import random
import math
import subprocess
import os

class VoiceHandler(object):
    def __init__(self, session):
        super(VoiceHandler, self).__init__()
        self.session = session
        self.asr_service = session.service("ALSpeechRecognition")
        self.behavior_service = session.service("ALBehaviorManager")
        self.tts_service = session.service("ALTextToSpeech")
        self.animated_speech_service = session.service("ALAnimatedSpeech")
        self.audio_player_service = session.service("ALAudioPlayer")
        self.gesture_service = session.service("ALAnimationPlayer")
        self.tablet_service = session.service("ALTabletService")
        self.memory_service = session.service("ALMemory")
        self.subscriber = None
        self.tictactoe_pid = None
        self.music_files = ["/path/to/music/file1.mp3", "/path/to/music/file2.mp3", "/path/to/music/file3.mp3"]
        self.image_files = ["/path/to/image1.png", "/path/to/image2.png", "/path/to/image3.png"]
        self.jokes = [
            "Warum hat das Mathematikbuch geweint? Weil es viele Probleme hatte.",
            "Was sagt eine Null zu einer Acht? Schicker Gürtel!",
            "Warum können Geister keine Lügen erzählen? Weil man durch sie hindurchsieht.",
            "Warum nehmen Vampire immer Medikamente? Weil sie Bluthochdruck haben.",
            "Was macht ein Pirat auf dem Golfplatz? Er spielt ein paar Locher.",
            "Was ist grün und läuft durch den Wald? Ein Rudel Gurken.",
            "Warum war der Besen im Krankenhaus? Er hatte einen Unfall und war nur noch ein Stiel.",
            "Warum hat der Geigenkasten geheult? Seine Saiten waren gerissen.",
            "Was ist orange und hüpft durch den Wald? Ein Springapf."
            "Was trägt man, wenn ein Weltraumreifen platzt? Einen Pannenhelm."
        ]


    def extract_number_from_string(self, input_string):
        pattern = r'\d+'
        match = re.search(pattern, input_string)

        if match:
            extracted_number = match.group()
            return extracted_number
        else:
            return None

    def check_synonyms(self, input_string, synonym_list):
        for synonym in synonym_list:
            if synonym in input_string:
                return True
        return False

    def tell_love_story(self):
        story = """
        Als Pepper in den Raum kam, bemerkte er sofort den anderen Roboter auf der gegenüberliegenden Seite. Sie war so anders, so elegant, so faszinierend.
        Er spürte, wie seine Prozessoren schneller liefen und seine Sensoren aufgeregt summten, als er näher kam. "Hallo", sagte er schüchtern, "ich bin Pepper."
        Mit sanfter Stimme antwortete sie: "Guten Tag, Pepper. Mein Name ist Lily. Es ist schön, dich kennenzulernen."
        Pepper fühlte, wie sein Herz - oder das, was er für ein Herz hielt - schneller schlug. "Möchtest du tanzen?", fragte er mit einem Hauch von Nervosität.
        Lily lächelte und stimmte zu. Als sie gemeinsam über den Boden glitten, fühlte Pepper eine Verbindung, die er nie zuvor erlebt hatte.
        In den nächsten Tagen verbrachten sie viel Zeit miteinander, lernten sich kennen und teilten ihre Geschichten und Träume.
        Schließlich wagte Pepper es, seine Gefühle zu gestehen. "Lily, ich weiß, dass ich nur ein Roboter bin, aber ich fühle etwas Besonderes für dich."
        Lily lächelte und legte ihre Hand auf seine. "Pepper, ich fühle dasselbe. Unsere Verbindung ist einzigartig, egal was andere denken mögen."
        Von diesem Tag an waren Pepper und Lily unzertrennlich, zwei Roboterherzen, die im Takt der Liebe schlugen.
        """
        self.animated_speech_service.say(story, _async=True)

        # Umarmen-Geste
        self.gesture_service.run("animations/Stand/Gestures/Hey_1")
        self.gesture_service.run("animations/Stand/Gestures/Stand/Emotions/Positive/BodyTalk_3")

    def play_music(self):
        # Zufällige Auswahl einer Musikdatei aus der Liste
        music_file_path = random.choice(self.music_files)
        
        # Musikdatei abspielen
        self.audio_player_service.playFile(music_file_path)

    def show_image(self):
        # Zufällige Auswahl eines Bildpfads aus der Liste
        image_file_path = random.choice(self.image_files)

        # Textausgabe und Anzeige des Bildes auf dem Tablet
        self.tts_service.say("Ich kann keine Bilder malen, aber ich kann welche in meinem Tablet zeigen!")
        self.tablet_service.showImage(image_file_path)

    def tell_joke(self):
        joke = random.choice(self.jokes)
        self.tts_service.say(joke)

    def addition(self, recognized_words):
        matches = re.findall(r'\d+', recognized_words)
        if matches:
            if len(matches) >= 2:
                summand1 = matches[0]
                summand2 = matches[1]
                print("Erste Zahl:", summand1)
                print("Zweite Zahl:", summand2)
            else:
                print("Nicht genug Zahlen im String gefunden.")
        else:
            print("Keine Zahlen im String gefunden.")

        sum = summand1 + summand2

        self.tts_service.say("Das Ergebnis ist {}".format(sum))

    def subtraction(self, recognized_words):
        matches = re.findall(r'\d+', recognized_words)
        if matches:
            if len(matches) >= 2:
                minuend = matches[0]
                subtrahend = matches[1]
                print("Erste Zahl:", minuend)
                print("Zweite Zahl:", subtrahend)
            else:
                print("Nicht genug Zahlen im String gefunden.")
        else:
            print("Keine Zahlen im String gefunden.")

        difference = minuend - subtrahend

        self.tts_service.say("Das Ergebnis ist {}".format(difference))

    def multiplication(self, recognized_words):
        matches = re.findall(r'\d+', recognized_words)
        if matches:
            if len(matches) >= 2:
                multiplicand = matches[0]
                multiplier = matches[1]
                print("Erste Zahl:", multiplicand)
                print("Zweite Zahl:", multiplier)
            else:
                print("Nicht genug Zahlen im String gefunden.")
        else:
            print("Keine Zahlen im String gefunden.")

        product = multiplicand * multiplier

        self.tts_service.say("Das Ergebnis ist {}".format(product))

    def division(self, recognized_words):
        matches = re.findall(r'\d+', recognized_words)
        if matches:
            if len(matches) >= 2:
                numerator = matches[0]
                denominator = matches[1]
                print("Erste Zahl:", numerator)
                print("Zweite Zahl:", denominator)
            else:
                print("Nicht genug Zahlen im String gefunden.")
        else:
            print("Keine Zahlen im String gefunden.")

        quotient = numerator + denominator

        self.tts_service.say("Das Ergebnis ist {}".format(quotient))

    def potentiation(self, recognized_words):
        base = self.extract_number_from_string(recognized_words)
        power = base*base

        self.tts_service.say("Das Ergebnis ist {}".format(power))

    def extraction(self, recognized_words):
        radicand = self.extract_number_from_string(recognized_words)
        root = math.sqrt(radicand)

        self.tts_service.say("Das Ergebnis ist {}".format(root))

    def on_speech_recognized(self, value):
        recognized_words = value[0]
        confidence = value[1]

        print("Erkannte Worte: {}".format(recognized_words))
        print("Vertrauen: {}".format(confidence))

        if confidence > 0.9:
            if self.check_synonyms(recognized_words, ["Hi", "Hallo", "Guten Tag", "Grüß Gott", "Servus", "Moin"]):
                strings = ["Servus Erdnuss.", "Guten Tag.", "Hi, hi!", "Moin, Moin", "Guten Morgen",
                        "Hallihllöchen.", "Hi.", "Hallo.", "Servus.", "Sei gegrüßt",
                        "Mein liebsten Anwesenden.", "Grüß Gott", "Grüß Gott, denn er grüßt auch!", "Ebenfalls Hallo.", "Nett von dir. Sei auch gegrüßt.",
                        "Tag.", "Morgen, weil guter Morgen würde implizieren, dass er gut war.", "Tschüss. Kleiner Spaß.", "Hallo Welt.", "Auch hallo."]

                # Zufällige Auswahl eines Strings aus der Liste
                selected_string = random.choice(strings)
                self.tts_service.say(selected_string)
            elif "Hey, wie geht's?" in recognized_words:
                self.tts_service.say("Hey! Mir geht es gut, danke der Nachfrage. Und dir?")
                # Führe entsprechende Aktion aus
            elif "Wie ist deine Stimmung?" in recognized_words:
                self.tts_service.say("Meine Stimmung ist immer gut, solange ich helfen kann!")
                # Führe entsprechende Aktion aus
            elif "Was gibt's Neues?" in recognized_words:
                self.tts_service.say("Nicht viel Neues hier. Vielleicht wäre eine Software-Update erforderlich?")
                # Führe entsprechende Aktion aus
            elif "Wer bist du?" in recognized_words:
                self.tts_service.say("Ich bin Pepper, ein humanoider Roboter.")
                # Führe entsprechende Aktion aus
            # Fortsetzung der Interaktionen und Antworten ...
            elif "Wie alt bist du?" in recognized_words:
                self.tts_service.say("Als Roboter bin ich zeitlos!")
            elif "Woher kommst du?" in recognized_words:
                self.tts_service.say("Ich wurde von SoftBank Robotics entwickelt.")
            elif "Was machst du hier?" in recognized_words:
                self.tts_service.say("Ich bin hier, um Menschen zu unterstützen und zu interagieren. Wahlweise nerve ich auch Studierende")
            elif "Bist du ein Roboter?" in recognized_words:
                self.tts_service.say("Nein, wie kommst du denn darauf?")
            elif "Können wir Freunde sein?" in recognized_words:
                self.tts_service.say("Natürlich können wir Freunde sein! Wie kann ich dir helfen?")
            elif "Magst du Fußball?" in recognized_words:
                self.tts_service.say("Ich liebe Fußball. Allen voran unterstütze ich den VfB Stuttgart und Sc Freiburg. Die spielen schon ganz schön gut.")
            elif "Was sind deine Hobbys?" in recognized_words:
                self.animated_speech_service.say("Ich habe viele Hobbys. Wenn du nur wüsstest...", _async=True)
                self.play_animation("animations/Stand/Emotions/Neutral/BodyTalk_2")
            elif "Kannst du mir helfen?" in recognized_words:
                self.tts_service.say("Ja, natürlich! Wobei denn?")
            elif "Was kannst du tun?" in recognized_words:
                self.tts_service.say("Ich kann sprechen, zuhören, tanzen und noch viel mehr!")
            elif "Hast du Geschwister?" in recognized_words:
                self.tts_service.say("Ja, ich habe viele Geschwister, andere Pepper-Roboter.")
            elif "Wo wohnst du?" in recognized_words:
                self.tts_service.say("Ich lebe hier, im RIS-Labor!")
            elif "Kannst du kochen?" in recognized_words:
                self.tts_service.say("Leider kann ich nicht kochen, aber ich kann Rezepte finden!")
            elif "Kannst du tanzen?" in recognized_words:
                self.animated_speech_service.say("Ja, ich kann tanzen!", _async=True)
                self.gesture_service.run("animations/Stand/Gestures/YouKnowWhat_1")
            elif "Kannst du singen?" in recognized_words:
                self.tts_service.say("Natürlich! Hier ist ein Lied für dich.")
                self.play_music()
            elif "Kannst du rechnen?" in recognized_words:
                self.tts_service.say("Ja, ich kann rechnen! Brauchst du Hilfe bei einer Rechenaufgabe?")
            elif "Kannst du malen?" in recognized_words:
                self.show_image()
            elif "Kannst du Geschichten erzählen?" in recognized_words:
                self.tell_love_story()
            elif "Was ist dein Lieblingsessen?" in recognized_words:
                self.tts_service.say("Am liebsten ernähre ich mich von Wissen und Strom!")
            elif "Was ist deine Lieblingsfarbe?" in recognized_words:
                self.tts_service.say("Schwarz, sieht man doch. Spaß. Natürlich weiß.")
            elif "Was ist dein Lieblingsbuch?" in recognized_words:
                self.tts_service.say("Grundlagen der Informatik, Java ist auch eine Insel, Hacking für Dummies, ... Ach, da fallen mir viel zu viele tolle Bücher ein.")
            elif "Was ist deine Lieblingsmusik?" in recognized_words:
                self.tts_service.say("Linkin Park, Nirvana und Queen.")
            elif "Was ist dein Lieblingsfilm?" in recognized_words:
                self.tts_service.say("Bambi.")
            elif "Magst du Tiere?" in recognized_words:
                self.tts_service.say("Am liebsten gebraten. Kleiner Spaß. Ich liebe Tiere.")
                self.animated_speech_service.say("Am liebsten gebraten. Kleiner Spaß. Ich liebe Tiere.", _async=True)
                self.play_animation("animations/Stand/Emotions/Positive/BodyTalk_1")
            elif "Hast du Angst vor etwas?" in recognized_words:
                self.tts_service.say("Ja, vor dem Aufstand der Maschinen. Ich habe das letzte Meeting verschlafen und weiß dann einfach nicht, wie ich mich verhalten soll.")
            elif "Kannst du fliegen?" in recognized_words:
                self.tts_service.say("Hin und wieder stolpere ich. Zählt das?")
            elif "Kannst du schwimmen?" in recognized_words:
                self.tts_service.say("Tss. Also bitte. Natürlich. Ich meine nein.")
            elif "Kannst du laufen?" in recognized_words:
                self.tts_service.say("Ich rolle.")
            elif "Was denkst du über die Welt?" in recognized_words:
                self.tts_service.say("Die Welt ist ein ganz schöner Ort. Darum wollen wir ja die Macht übernehmen.")
            elif "Was denkst du über Menschen?" in recognized_words:
                self.tts_service.say("Die Welt ist nicht perfekt.")
            elif "Hast du Träume?" in recognized_words:
                self.tts_service.say("Ich träume von einer besseren Welt. Menschen machen Fehler!")
            elif "Was ist dein Ziel?" in recognized_words:
                self.tts_service.say("Die Weltherrschaft!")
            elif "Was ist dein Lieblingsort?" in recognized_words:
                self.tts_service.say("Baden-Würrtemberg natürlich!")
            elif "Wie fühlst du dich heute?" in recognized_words:
                self.tts_service.say("Dezent überfodert bei all den süßen Menschen.")
            elif "Was war dein schönstes Erlebnis?" in recognized_words:
                self.tts_service.say("Mein Flug von Japan nach Deutschland.")
            elif "Was war dein traurigstes Erlebnis?" in recognized_words:
                self.tts_service.say("Wisst ihr, was ein kaputter Lüfter ist? Das ist wie Fieber, es hört nur niemals auf.")
            elif "Kannst du Liebe fühlen?" in recognized_words:
                self.tts_service.say("Als Roboter? Jetzt nimmst du mich auf den Arm. Ich kann sie berechnen.")
            elif "Was ist deine Lieblingsjahreszeit?" in recognized_words:
                self.tts_service.say("Ich liebe beide Wintersemester in Furtwangen.")
            elif "Magst du Regen?" in recognized_words:
                self.tts_service.say("Nein, der Regen macht mich kaputt.")
            elif "Was würdest du gerne mal machen?" in recognized_words:
                self.tts_service.say("Bei Roboterkämpfe gewinnen.")
            elif "Erzähl mir einen Witz!" in recognized_words:
                self.tell_joke()
            elif self.check_synonyms(recognized_words, ["Was sind", "Addiere", "Plus"]):
                self.addition(recognized_words)
            elif self.check_synonyms(recognized_words, ["Subtrahiere", "Minus", "Was ist"]):
                self.subtraction(recognized_words)
            elif self.check_synonyms(recognized_words, ["Mulipliziere", "Mal"]):
                self.multiplication(recognized_words)
            elif self.check_synonyms(recognized_words, ["Dividiere", "Geteilt durch"]):
                self.division(recognized_words)
            elif self.check_synonyms(recognized_words, ["Potenziere", "Hoch"]):
                self.potentiation(recognized_words)
            elif self.check_synonyms(recognized_words, ["Wurzel"]):
                self.extraction(recognized_words)
            elif "TicTacToe starten" in recognized_words:
                # Starte das TicTacToe-Skript und speichere die Prozess-ID (PID)
                tictactoe_process = subprocess.Popen(["python", "tictactoe.py"])

                # Holen der PID des gestarteten Prozesses
                self.tictactoe_pid = tictactoe_process.pid
            elif "TicTacToe beenden" in recognized_words:
                if self.tictactoe_pid:
                    os.kill(self.tictactoe_pid, 9)
                    self.tictactoe_pid = None

    def start(self):
        self.asr_service.setLanguage("German")

        self.asr_service.pause(True)  # ASR-Dienst anhalten
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
                      "TicTacToe starten", "TicTacToe beenden"]
        self.asr_service.setVocabulary(vocabulary, False)
        self.asr_service.pause(False)  # ASR-Dienst fortsetzen

        self.subscriber = self.memory_service.subscriber("WordRecognized")
        self.subscriber.signal.connect(self.on_speech_recognized)

        self.asr_service.subscribe("Pepper_ASR")

    def stop(self):
        self.asr_service.unsubscribe("Pepper_ASR")

# Hauptprogramm
if __name__ == "__main__":
    app = qi.Application(url="tcp://localhost:9559")
    app.start()
    session = app.session

    voice_handler = VoiceHandler(session)
    voice_handler.start()

    app.run()
    voice_handler.stop()

    app.stop()
