import random

class Room:
    def __init__(self, number, riddle_set):
        self.number = number
        self.riddle_set = riddle_set
        self.solved = 0

    def enter(self):
        print(f"\n--- Raum {self.number + 1} ---")
        print("Du betrittst einen neuen Raum.")
        for riddle in self.riddle_set:
            if self.ask_riddle(riddle):
                self.solved += 1
            else:
                print("Das war leider falsch. Versuche es erneut.")
                if self.ask_riddle(riddle):
                    self.solved += 1
                else:
                    print("Auch beim zweiten Versuch... weiter geht's.")
        print(f"Du hast {self.solved} von 4 Rätseln in diesem Raum gelöst.")

    def ask_riddle(self, riddle):
        print("\nRätsel:")
        print(riddle["question"])
        answer = input("Deine Antwort: ").strip().lower()
        if answer == riddle["answer"]:
            print("Richtig!")
            return True
        else:
            print(f"Falsch! Die richtige Antwort wäre gewesen: {riddle['answer']}")
            return False

def intro():
    print("Willkommen zu ESCAPE: Das Rätsel-Anwesen!")
    print("Du erwachst in einem düsteren Flur. Eine Stimme flüstert:")
    print("\"Nur wer alle Räume meistert, findet den Ausgang...\"")
    input("\nDrücke Enter, um zu beginnen...")

def outro(solved_rooms):
    if solved_rooms == 9:
        print("\nDu öffnest die letzte Tür. Sonnenlicht blendet dich. Du bist frei!")
        print("Herzlichen Glückwunsch, du hast das Escape-Spiel gemeistert!")
    else:
        print("\nDu hast nicht alle Räume gemeistert, aber du bist dem Geheimnis näher gekommen.")
        print("Versuche es erneut, um das ganze Anwesen zu bezwingen!")

def get_riddles():
    riddles = [
        # Raum 1
        {"question": "Ich habe Schlüssel, aber keine Schlösser. Ich habe Platz, aber keinen Raum. Was bin ich?", "answer": "tastatur"},
        {"question": "Was wird beim Trocknen nass?", "answer": "handtuch"},
        {"question": "Wie viele Monate haben 28 Tage?", "answer": "alle"},
        {"question": "Was hat einen Kopf, eine aber keinen Körper?", "answer": "münze"},
        # Raum 2
        {"question": "Je mehr du wegnimmst, desto größer wird es. Was ist es?", "answer": "loch"},
        {"question": "Was lebt, wenn es gefüttert wird und stirbt, wenn man Wasser gibt?", "answer": "feuer"},
        {"question": "Welcher Tag kommt zweimal in einer Woche, einmal in einem Jahr und niemals in einem Monat?", "answer": "d"},
        {"question": "Was hat viele Zähne, aber beißt nie?", "answer": "kamm"},
        # Raum 3
        {"question": "Was hat eine Nachricht, aber keinen Briefträger?", "answer": "email"},
        {"question": "Was ist schwerer: Ein Kilo Federn oder ein Kilo Blei?", "answer": "gleich"},
        {"question": "Was gehört dir, aber wird öfter von anderen benutzt als von dir?", "answer": "name"},
        {"question": "Was kann man fangen, aber nicht werfen?", "answer": "erkältung"},
        # Raum 4
        {"question": "Ich bin immer hungrig, muss gefüttert werden, sterbe aber, wenn man mir Wasser gibt. Was bin ich?", "answer": "feuer"},
        {"question": "Was läuft, hat aber keine Beine?", "answer": "wasser"},
        {"question": "Was kann man nicht sehen, aber fühlen?", "answer": "wind"},
        {"question": "Was hat einen Ring, aber keinen Finger?", "answer": "telefon"},
        # Raum 5
        {"question": "Was ist am Anfang der Nacht und am Ende des Morgens?", "answer": "n"},
        {"question": "Was kann alles durchbrechen, aber niemals berühren?", "answer": "licht"},
        {"question": "Was ist voller Löcher, aber hält Wasser?", "answer": "schwamm"},
        {"question": "Wie nennt man einen Bär ohne Zähne?", "answer": "gummibärchen"},
        # Raum 6
        {"question": "Was ist immer vor dir, aber du kannst es nie erreichen?", "answer": "zukunft"},
        {"question": "Was steigt, aber fällt nie?", "answer": "alter"},
        {"question": "Was ist leicht wie eine Feder, selbst der stärkste Mensch kann es nicht lange halten?", "answer": "atem"},
        {"question": "Was beginnt mit E, endet mit E und enthält nur einen Buchstaben?", "answer": "umschlag"},
        # Raum 7
        {"question": "Was kann reisen um die Welt, bleibt aber immer in der Ecke?", "answer": "briefmarke"},
        {"question": "Was wird nicht nass, egal wie viel es regnet?", "answer": "schatten"},
        {"question": "Was hat einen Hals, aber keinen Kopf?", "answer": "flasche"},
        {"question": "Was kann man brechen, ohne es zu berühren?", "answer": "versprechen"},
        # Raum 8
        {"question": "Was hat Städte, aber keine Häuser; Wälder, aber keine Bäume; Flüsse, aber kein Wasser?", "answer": "karte"},
        {"question": "Was hat Flügel, aber kann nicht fliegen?", "answer": "flugzeug"},
        {"question": "Was kann man nicht sehen, hören oder anfassen, aber existiert trotzdem?", "answer": "zeit"},
        {"question": "Was kann man füllen, aber nicht leeren?", "answer": "zeit"},
        # Raum 9
        {"question": "Was ist unsichtbar, aber immer da, manchmal still, manchmal laut?", "answer": "luft"},
        {"question": "Was kann ein Kind machen, aber ein Erwachsener nicht zurückbekommen?", "answer": "kindheit"},
        {"question": "Was hat einen Anfang, aber kein Ende?", "answer": "kreis"},
        {"question": "Was kann wachsen, aber ist kein Lebewesen?", "answer": "kristall"}
    ]
    random.shuffle(riddles)
    return [riddles[i*4:(i+1)*4] for i in range(9)]

def main():
    intro()
    riddles_per_room = get_riddles()
    solved_rooms = 0
    story = [
        "Du findest eine Notiz: \"Jeder Raum ist eine Prüfung deines Verstandes.\"",
        "Ein leises Lachen ertönt. \"Gib nicht auf!\"",
        "Die Schatten werden länger, aber du hast keine Angst.",
        "Eine Tür knarrt. Dahinter verbirgt sich ein weiteres Geheimnis.",
        "Die Luft wird kühler. Nur noch ein paar Räume bis zur Freiheit.",
        "Ein Lichtstrahl dringt durch das Fenster. Hoffnung keimt auf.",
        "Du hörst Schritte hinter dir. Beeil dich!",
        "Der letzte Raum. Dein Herz schlägt schneller.",
        "Du siehst den Ausgang – fast geschafft!"
    ]
    for i in range(9):
        print("\n" + story[i])
        room = Room(i, riddles_per_room[i])
        room.enter()
        if room.solved >= 2:
            solved_rooms += 1
    outro(solved_rooms)

if __name__ == "__main__":
    main()