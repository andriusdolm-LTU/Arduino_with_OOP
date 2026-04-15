import patch
from pyfirmata import Arduino
import time

class LED:
    def __init__(self, board, pin):
        self.pin = board.get_pin(f'd:{pin}:o')

    def on(self):
        self.pin.write(1)
        print("LED įjungtas!")

    def off(self):
        self.pin.write(0)
        print("LED išjungtas!")
    
    def time_on(self):
        while True:
            self.pin.write(1)
            time(1)
    

class Ismanus_Projektas:
    def __init__(self):
        self.board = Arduino('COM5') 
        self.raud_led = None
        self.zal_led = None
    
    def klausimai(self):
        spalva = input("Ar norite pajungti žalią, raudoną ar abu LED? (z/r/a)\n")
        if spalva == 'z':
            self.zal_led = LED(self.board, 13,)
        elif spalva == 'r':
            self.raud_led = LED(self.board, 12)
        elif spalva == 'a':
            self.zal_led = LED(self.board, 13)
            self.raud_led = LED(self.board, 12)
        funkcija = input("Ar norite kad LED mirgsetų ar ne? (t/n)\n")

        
    def vykdymas_spalva(self):
            if self.raud_led and self.zal_led:
                self.raud_led.on()
                self.zal_led.on()
            if self.raud_led and self.zal_led == None:
                self.raud_led.on()
            if self.zal_led and self.raud_led == None:
                self.zal_led.on()
            if not self.raud_led and not self.zal_led:
                print("nepasirinkata")
            input("užbaigti paspauskite Enter")
            if self.raud_led:
                self.raud_led.off()
            if self.zal_led:
                self.zal_led.off()
            self.board.exit()
    
    def 
            

if __name__ == "__main__":
    projektas = Ismanus_Projektas()
    projektas.klausimai()
    projektas.vykdymas_spalva()