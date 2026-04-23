# Aplinkos ir elementų paruošimas (SETUP)

## 1. „pyFirmata“ instaliavimas į mikrokontrolerį  

a) Atidaryti **Arduino IDE**.  

b) Skiltyje ***Select Board*** pasirinkti savo mikrokontrolerį.  

c) Pasirinkti: ***File -> Examples -> Firmata -> StandardFirmata***.  

d) Atsidarius naujam langui pasitikrinti ar vis dar naudoja tinkamą mikrokontrolerį ir spausti ***Upload***.  

e) Jei viskas įsirašė, išjungti **Arduino IDE**.  


## 2. „pyFirmata“ instaliavimas į „Python“ aplinką  

a) Atsidaryti savo .py failą per **Visual Studio Code**.

b) terminale parašyti komandą `pip install pyfirmata` arba `py -m pip install pyfirmata`.  

## 3. Breadboard paruošimas

a) Prijungti LED prie pin 9, 10, 11

b) Prijungti mygtuką prie pin 2

c) Prijungti potenciometrą prie pin A5

## 4. Būtini failai, kuriuos reikia įsirašyti, kad veiktų projektas

1. [main.py](./main.py)

2. [klausimai.py](./klausimai.py)

3. [nustatymai.py](./nustatymai.py)

4. [patch.py](./patch.py)

