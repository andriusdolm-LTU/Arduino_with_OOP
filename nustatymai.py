import time

class Projekto_Nustatymai:
    def __init__(self):
        self._spalva = None
        self._mirksejimas = None
        self._potenciometro_funkcija = None
        self._laikas = None
        self._mygtuko_funkcija = None
        self._potenciometro_ryskumas = None

    @property
    def spalva(self):
        return self._spalva
    
    @spalva.setter
    def spalva(self, value):
        sutvarkyta_value = value.lower().strip()
        leistinas = ['z', 'g', 'r', 'v']
        if sutvarkyta_value in leistinas:
            self._spalva = sutvarkyta_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._spalva = None
            time.sleep(2)
    
    @property
    def mirksejimas(self):
        return self._mirksejimas
    
    @mirksejimas.setter
    def mirksejimas(self, value):
        sutvarkytas_value = value.lower().strip()
        leistinas = ['t', 'n']
        if sutvarkytas_value in leistinas:
            self._mirksejimas = sutvarkytas_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._mirksejimas = None
            time.sleep(2)

    @property
    def potenciometro_funkcija(self):
        return self._potenciometro_funkcija
    
    @potenciometro_funkcija.setter
    def potenciometro_funkcija(self, value):
        sutvarkytas_value = value.strip()
        leistinas = ['1', '2']
        if sutvarkytas_value in leistinas:
            self._potenciometro_funkcija = sutvarkytas_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._potenciometro_funkcija = None
            time.sleep(2)

    @property
    def laikas(self):
        return self._laikas
    
    @laikas.setter
    def laikas(self, value):
        if value >= 0.1 and value <=10:
            self._laikas = value
        else:
            print("Negalima pasirinkti tokio laiko")
            self._laikas = None
            time.sleep(2)

    @property
    def mygtuko_funkcija(self):
        return self._mygtuko_funkcija
    
    @mygtuko_funkcija.setter
    def mygtuko_funkcija(self, value):
        sutvarkytas_value = value.strip()
        leistinas = ['1', '2']
        if sutvarkytas_value in leistinas:
            self._mygtuko_funkcija = sutvarkytas_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._mygtuko_funkcija = None
            time.sleep(2)

    @property
    def potenciometro_ryskumas(self):
        return self._potenciometro_ryskumas
    
    @potenciometro_ryskumas.setter
    def potenciometro_ryskumas(self, value):
        sutvarkytas_value = value.lower().strip()
        leistinas = ['t', 'n']
        if sutvarkytas_value in leistinas:
            self._potenciometro_ryskumas = sutvarkytas_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._potenciometro_ryskumas = None
            time.sleep(2)