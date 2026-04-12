import patch
from pyfirmata import Arduino
import time

class LED:
    def __init__(self, board, pin):
        # Nustatome pin'ą kaip skaitmeninį išėjimą (output)
        self.pin = board.get_pin(f'd:{pin}:o')

    def on(self):
        self.pin.write(1)
        print("LED įjungtas!")

    def off(self):
        self.pin.write(0)
        print("LED išjungtas!")

class R3_Board:
    def __init__(self, port):
        print(f"Jungiamasi prie {port}...")
        self.board = Arduino(port) 
        self.led = LED(self.board, 8)

if __name__ == "__main__":
    # Sukuriame objektą (čia Arduino sumirksės 3 kartus)
    my_r3 = R3_Board('COM5')
    
    # Įjungiame LED
    my_r3.led.on()
    
    # Neleidžiame programai iškart užsidaryti
    # Jei programa baigiasi, ryšys nutrūksta ir LED užgęsta
    print("Pradedamas laiko skaičiavimas:")
    for sekunde in range(1, 11): # Ciklas nuo 1 iki 10
        time.sleep(1)            # Palaukiame 1 sekundę
        print(f"{sekunde} sek.")
    
    my_r3.led.off()
    print("Programa baigta.")