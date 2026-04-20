import patch
from pyfirmata import Arduino, util
import time
class Tuscias_LED:
    def on(self): pass
    def off(self): pass
    

class LED:
    def __init__(self, board, pin):
        self.pin = board.get_pin(f'd:{pin}:o')

    def on(self):
        self.pin.write(1)

    def off(self):
        self.pin.write(0)
    

class Ismanus_Projektas:
    def __init__(self):
        self.board = Arduino('COM5')
        self.mygtukas = self.board.get_pin('d:2:i') 
        it = util.Iterator(self.board)
        it.start()
        self.zal_led = Tuscias_LED()
        self.gel_led = Tuscias_LED()
        self.raud_led = Tuscias_LED()
        self._spalva = None
        self._mirksejimas = None
        self._laikas = None
        self._mygtuko_funkcija = None
    
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
        sutvarkytas_value = value.lower().strip()
        leistinas = ['1', '2']
        if sutvarkytas_value in leistinas:
            self._mygtuko_funkcija = sutvarkytas_value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._mirksejimas = None
            time.sleep(2)

    def laukimas(self, sekundes = 0.01):
        pabaiga = time.time() + sekundes
        while time.time() < pabaiga:
            if self.mygtukas.read() is True:
                return True
            time.sleep(0.005)
        return False

    def klausimai(self):
        while self.spalva is None:
            self.spalva = input("Ar norite pajungti žalią, geltoną, raudoną ar visus tris LED? (z/g/r/v)\n")
        while self.mirksejimas is None:
            self.mirksejimas = input("Ar norite kad LED mirgsėtų ar ne? (t/n)\n")
        if self.mirksejimas == 't':
            while self.laikas is None:
                self.laikas = float(input("Kas kiek laiko norite, kad mirksėtų? (0.1s iki 10s)\n"))
        if self.mirksejimas == 'n':
            while self.mygtuko_funkcija is None:
                self.mygtuko_funkcija = input("Ar norite junginėti LED su mygtuku ar tik ijungti? (1/2)\n")
        if self.spalva == 'z':
            self.zal_led = LED(self.board, 11)
        if self.spalva == 'g':
            self.gel_led = LED(self.board, 10)
        elif self.spalva == 'r':
            self.raud_led = LED(self.board, 9)
        elif self.spalva == 'v':
            self.zal_led = LED(self.board, 11)
            self.gel_led = LED(self.board, 10)
            self.raud_led = LED(self.board, 9)

    def vykdymas_led(self):
            if self.mygtuko_funkcija == '2':
                while True:
                    if self.mygtukas.read() is True:
                        break
                    if self.mirksejimas == 'n':
                        print("Norint užbaigti paspauskite mygtuka")
                        self.zal_led.on()
                        self.gel_led.on()
                        self.raud_led.on()
                    elif self.mirksejimas == 't':
                        print("Norint užbaigti paspauskite mygtuka")
                        while True:
                            self.zal_led.on()
                            self.gel_led.on()
                            self.raud_led.on()
                            if self.laukimas(self.laikas/2):
                                break
                            self.zal_led.off()
                            self.gel_led.off()
                            self.raud_led.off()
                            if self.laukimas(self.laikas/2):
                                break
            elif self.mygtuko_funkcija == '1':
                try:
                    print("Norint užbaigti paspauskite CTRL + C")
                    while True:
                        if self.mygtukas.read() is True:
                            self.zal_led.on()
                            self.gel_led.on()
                            self.raud_led.on()
                        else:
                            self.zal_led.off()
                            self.gel_led.off()
                            self.raud_led.off()
                        time.sleep(0.01)
                except KeyboardInterrupt:
                    print("Išjungta")

    def baigimas(self):
        print("Išjungiami visi LED ir uždaroma jungtis")
        for i in range(7,14):
            self.board.digital[i].write(0)
        self.board.exit()    

if __name__ == "__main__":
    projektas = Ismanus_Projektas()
    projektas.klausimai()
    projektas.vykdymas_led()
    projektas.baigimas()