import patch
from pyfirmata import Arduino, util
from nustatymai import Projekto_Nustatymai
from klausimai import uzduoti_klausimai
import time

class Tuscias_LED:
    def on(self): pass
    def off(self): pass
    

class LED:
    def __init__(self, board, pin, ryskumas = 1):
        self.pin = board.get_pin(f'd:{pin}:p')
        self.ryskumas = ryskumas

    def on(self):
        self.pin.write(self.ryskumas)

    def off(self):
        self.pin.write(0)

    def led_ryskumas(self,naujas_ryskumas):
        self.ryskumas = naujas_ryskumas
        self.pin.write(self.ryskumas)
    

class Ismanus_Projektas(Projekto_Nustatymai):
    def __init__(self):
        super().__init__()
        self.board = Arduino('COM5')
        self.mygtukas = self.board.get_pin('d:2:i') 
        self.potenciometras = self.board.get_pin('a:5:i')
        it = util.Iterator(self.board)
        it.start()
        self.zal_led = Tuscias_LED()
        self.gel_led = Tuscias_LED()
        self.raud_led = Tuscias_LED()
        
    def keitimas_led_busenos(self, busena):
        if busena:
            self.zal_led.on()
            self.gel_led.on()
            self.raud_led.on()
        else:
            self.zal_led.off()
            self.gel_led.off()
            self.raud_led.off()

    def laukimas(self, sekundes = 0.01):
        pabaiga = time.time() + sekundes
        while time.time() < pabaiga:
            if self.mygtukas.read() is True:
                return True
            time.sleep(0.005)
        return False

    def laukimas_su_potenciometru(self):
        pradzia = time.time()
        while True:
            if self.mygtukas.read() is True:
                return True
            potenciometro_reiksme = self.potenciometras.read()
            if potenciometro_reiksme is None:
                potenciometro_reiksmereiksme = 0.5
            limitas = potenciometro_reiksme * 10
            print(potenciometro_reiksme*10)
            praejo = time.time() - pradzia
            if praejo >= limitas:
                return False
            time.sleep(0.01)

    def konfiguruoti_led(self):
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
        if self.mirksejimas == 'n':
            if self.mygtuko_funkcija == '2':
                if self.potenciometro_ryskumas == 'n':
                    print("LED įjungti. Norint užbaigti paspauskite mygtuką.")
                    while True:
                        if self.mygtukas.read() is True:
                            break
                        self.keitimas_led_busenos(1)
                elif self.potenciometro_ryskumas == 't':
                    print("LED įjungti, keisti su potenciometru ryskumą. Norint užbaigti paspauskite mygtuką.")
                    while True:
                        if self.mygtukas.read() is True:
                            break
                        ryskumas = self.potenciometras.read()
                        self.zal_led.led_ryskumas(ryskumas)
                        self.gel_led.led_ryskumas(ryskumas)
                        self.raud_led.led_ryskumas(ryskumas)
                        time.sleep(0.01)

            elif self.mygtuko_funkcija == '1':
                print("Valdykite mygtuku. Užbaigti: CTRL + C")
                try:
                    while True:
                        if self.mygtukas.read() is True:
                            self.keitimas_led_busenos(1)
                        else:
                            self.keitimas_led_busenos(0)
                except KeyboardInterrupt:
                    pass
        elif self.mirksejimas == 't':
            if self.potenciometro_funkcija == '2':
                print(f"Mirksėjimas {self.laikas}sek. Norint užbaigti paspauskite mygtuką.")
                while True:
                    self.keitimas_led_busenos(1)
                    if self.laukimas(self.laikas/2):
                        break
                    self.keitimas_led_busenos(0)
                    if self.laukimas(self.laikas/2):
                        break
            elif self.potenciometro_funkcija == '1':
                print("Mirksėjimas (Potenciometras). Norint užbaigti paspauskite mygtuką.")
                while True:
                    if self.potenciometras.read() < 0.01:
                        self.keitimas_led_busenos(1)
                    self.keitimas_led_busenos(1)
                    if self.laukimas_su_potenciometru():
                        break
                    self.keitimas_led_busenos(0)
                    if self.laukimas_su_potenciometru():
                        break

    def baigimas(self):
        print("Išjungiami visi LED ir uždaroma jungtis")
        self.keitimas_led_busenos(0)
        self.board.exit()    

if __name__ == "__main__":
    projektas = Ismanus_Projektas()
    uzduoti_klausimai(projektas)
    projektas.konfiguruoti_led()
    projektas.vykdymas_led()
    projektas.baigimas()