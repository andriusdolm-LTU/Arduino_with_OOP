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
        self.raud_led = Tuscias_LED()
        self.zal_led = Tuscias_LED()
        self._spalva = None
        self._mirksejimas = None
        self._laikas = None

    @property
    def spalva(self):
        return self._spalva
    
    @spalva.setter
    def spalva(self, value):
        sutvarkyta_value = value.lower().strip()
        leistinas = ['z', 'r', 'a']
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
        if value >= 1 and value <=10:
            self._laikas = value
        else:
            print("Negalima pasirinkti tokio laiko")
            self._laikas = None
            time.sleep(2)

    def klausimai(self):
        while self.spalva is None:
            self.spalva = input("Ar norite pajungti žalią, raudoną ar abu LED? (z/r/a)\n")
        while self.mirksejimas is None:
            self.mirksejimas = input("Ar norite kad LED mirgsėtų ar ne? (t/n)\n")
        if self.mirksejimas == 't':
            while self.laikas is None:
                self.laikas = float(input("Kas kiek laiko norite, kad mirksėtų? (1s iki 10s)\n"))
        if self.spalva == 'z':
            self.zal_led = LED(self.board, 13)
        elif self.spalva == 'r':
            self.raud_led = LED(self.board, 12)
        elif self.spalva == 'a':
            self.zal_led = LED(self.board, 13)
            self.raud_led = LED(self.board, 12)

        
    def vykdymas_led(self):
            if self.mirksejimas == 'n':
                self.raud_led.on()
                self.zal_led.on()
                input("norint užbaigti paspauskite ENTER")
                self.raud_led.off()
                self.zal_led.off()
            elif self.mirksejimas == 't':
                try:
                    print("norint užbaigti paspauskite CTRL+C")
                    while True:
                        self.raud_led.on()
                        self.zal_led.on()
                        time.sleep(self.laikas/2)
                        self.raud_led.off()
                        self.zal_led.off()
                        time.sleep(self.laikas/2)
                except KeyboardInterrupt:
                    pass
        
    def baigimas(self):
        print("Išjungiami visi LED ir uždaroma jungtis")
        self.raud_led.off()
        self.zal_led.off()
        self.board.exit()    

if __name__ == "__main__":
    projektas = Ismanus_Projektas()
    projektas.klausimai()
    projektas.vykdymas_led()
    projektas.baigimas()