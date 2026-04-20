import patch
from pyfirmata import Arduino, util
from nustatymai import Projekto_Nustatymai
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
    

class Ismanus_Projektas(Projekto_Nustatymai):
    def __init__(self):
        self.board = Arduino('COM5')
        self.mygtukas = self.board.get_pin('d:2:i') 
        self.potenciometras = self.board.get_pin('a:5:i')
        it = util.Iterator(self.board)
        it.start()
        self.zal_led = Tuscias_LED()
        self.gel_led = Tuscias_LED()
        self.raud_led = Tuscias_LED()
        
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


    def klausimai(self):
        while self.spalva is None:
            self.spalva = input("Ar norite pajungti žalią, geltoną, raudoną ar visus tris LED? (z/g/r/v)\n")
        while self.mirksejimas is None:
            self.mirksejimas = input("Ar norite kad LED mirgsėtų ar ne? (t/n)\n")
        if self.mirksejimas == 't':
            while self.potenciometro_funkcija is None:
                self.potenciometro_funkcija = input("Ar norite naudoti potenciometrą mirksėjimui ar ne? (1/2)\n")
            if self.potenciometro_funkcija == '2':
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
                print("Norint užbaigti paspauskite mygtuka")
                while True:
                    if self.mygtukas.read() is True:
                        break
                    self.zal_led.on()
                    self.gel_led.on()
                    self.raud_led.on()
                    time.sleep(0.001)
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
            if self.potenciometro_funkcija == '2':
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
            elif self.potenciometro_funkcija == '1':
                print("Norint užbaigti paspauskite mygtuka")
                while True:
                    if self.mygtukas.read() is True:
                        break
                    potenciometro_reiksme = self.potenciometras.read()
                    while potenciometro_reiksme < 0.005:
                        potenciometro_reiksme = self.potenciometras.read()
                        self.zal_led.off()
                        self.gel_led.off()
                        self.raud_led.off()
                    self.zal_led.on()
                    self.gel_led.on()
                    self.raud_led.on()
                    if self.laukimas_su_potenciometru():
                        break
                    self.zal_led.off()
                    self.gel_led.off()
                    self.raud_led.off()
                    if self.laukimas_su_potenciometru():
                        break
                    time.sleep(0.01)


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