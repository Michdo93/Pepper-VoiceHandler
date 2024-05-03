class BeispielKlasse(object):
    def __init__(self):
        self.attr1_geantwortet = "Wert1"
        self.attr1_gefunden = True
        self.attr2_geantwortet = "Wert3"
        self.attr2_gefunden = False

    def suche_attr(self, wort):
        for attr_name, attr_value in self.__dict__.items():
            if wort in attr_name:
                if "_gefunden" in attr_name:
                    antwort_attr_name = attr_name.replace("_gefunden", "_geantwortet")
                    antwort_attr_value = getattr(self, antwort_attr_name)
                    if attr_value:
                        print(antwort_attr_value)

# Beispiel verwenden
objekt = BeispielKlasse()
objekt.suche_attr("gefunden")
