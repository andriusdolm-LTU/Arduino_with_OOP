import patch
from pyfirmata import Arduino
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
        self.zal_led = Tuscias_LED()
        self.gel_led = Tuscias_LED()
        self.raud_led = Tuscias_LED()
        self._rezimas = None
        self._spalva = None
        self._mirksejimas = None
        self._laikas = None

    @property
    def rezimas(self):
        return self._rezimas
    
    @rezimas.setter
    def rezimas(self, value):
        if value in ['1', '2']:
            self._rezimas = value
        else:
            print("Neteisingai įvestas atsakymas arba nėra tokio pasirinkimo")
            self._rezimas = None
            time.sleep(2)
    
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

    def klausimai(self):
        while self.rezimas is None:
            self.rezimas= input("Ar norite žaisti ar tik paleisti LED? (1/2)\n")
        if self.rezimas == '2':
            while self.spalva is None:
                self.spalva = input("Ar norite pajungti žalią, geltoną, raudoną ar visus LED? (z/g/r/v)\n")
            while self.mirksejimas is None:
                self.mirksejimas = input("Ar norite kad LED mirgsėtų ar ne? (t/n)\n")
            if self.mirksejimas == 't':
                while self.laikas is None:
                    self.laikas = float(input("Kas kiek laiko norite, kad mirksėtų? (0.1s iki 10s)\n"))
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
        else:
            self.zaidimas()

    def vykdymas_led(self):
            if self.mirksejimas == 'n':
                self.zal_led.on()
                self.gel_led.on()
                self.raud_led.on()
                input("norint užbaigti paspauskite ENTER")
                self.zal_led.off()
                self.gel_led.off()
                self.raud_led.off()
            elif self.mirksejimas == 't':
                try:
                    print("norint užbaigti paspauskite CTRL+C")
                    while True:
                        self.zal_led.on()
                        self.gel_led.on()
                        self.raud_led.on()
                        time.sleep(self.laikas/2)
                        self.zal_led.off()
                        self.gel_led.off()
                        self.raud_led.off()
                        time.sleep(self.laikas/2)
                except KeyboardInterrupt:
                    pass
                self.baigimas()

    def zaidimas(self):
        try:
            print("norint užbaigti paspauskite CTRL+C")
            kryptis = 1
            while True:
                if kryptis % 2 == 1:
                    for i in [7,9,10,11,8,12]:
                        for j in [7,9,10,11,8,12]:
                            if j == i:
                                self.board.digital[j].write(1)
                            else:
                                self.board.digital[j].write(0)
                        time.sleep(0.2)
                    kryptis += 1
                else:
                    for i in [13,12,8,11,10,9]:
                        for j in [13,12,8,11,10,9]:
                            if j == i:
                                self.board.digital[j].write(1)
                            else:
                                self.board.digital[j].write(0)
                        time.sleep(0.2)
                    kryptis = 1
        except KeyboardInterrupt:
            pass
        self.baigimas()

    def baigimas(self):
        print("Išjungiami visi LED ir uždaroma jungtis")
        for i in range(7,14):
            self.board.digital[i].write(0)
        self.board.exit()    

if __name__ == "__main__":
    projektas = Ismanus_Projektas()
    projektas.klausimai()
    projektas.vykdymas_led()