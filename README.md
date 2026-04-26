# Arduino valdymas su Python naudojant OOP  

Šis projektas naudoja **objektinį programavimą (OOP)**, kad per klausimus valdytų Arduino mikrokontrolerį ir jo komponentus (LED, mygtuką, potenciometrą) teisiogiai iš Python aplinkos.

## Naudojama  

- Python 3.x
- Biblioteka: `pyFirmata`
- Mikrokontroleris: Arduino Uno R3
- 3 - LED
- 1 - Potenciometras
- 1 - Mygtukas

## Surinkimas ir paleidimas  

1. Instrukcija: [Diegimo ir jungimo žingsniai](./SETUP.md)  

2. Paleidimas: `python OOP_Arduino.py`.  
*Svarbu: prieš paleidžiant komandą, įsitikinti, kad terminalas atidarytas toje vietoje, kur yra `OOP_Arduino.py` failas.*  

# Kodų implementacija

## 4 OOP pillars

- Polimorfizmas

Polimorfizmas šiame kode yra naudojamas ne daug. Vienas iš naudojimų yra su funkcija `on()`, kurios veikimas priklauso ar jau yra duomenys iš JSON failo, iš terminalo įvesčių ar iš numatytojo nuskaitymo.

- Abstrakcija

Abstrakcija naudojama keliose vietose. Viena iš jų yra su failu *nustatymai.py*, kadangi rašant *OOP_Arduino.py* faile norint gauti nustatymus prie kintamųjų mes iškviečiame klasę iš kito failo, bet mes nematome kas tam faile vyksta. Taip pat naudojama abstrakcija iškviečiant funkcijas `uzkrauti_nustatymus()` ir `issaugoti_nustatymus()`, kadangi mes nematome jų vidaus.

- Paveldėjimas

Iš šio kodo naudojamas paveldėjimas vieną kartą pagrindiniame faile, kad kodas nuskaitytų ir gautų duomenis iš klasės kuris yra kitame faile *nustaytmai.py*, naudojama eilutė `class Ismanus_Projektas(Projekto_Nustatymai):`. Taip pat pagrindinėje klasėje *Ismanus_Projektas* iškviečiame komandą `super().__init__()`, kad nustatytume klasės atributus iš *nustatymai.py*

- Enkapsuliacija

Šiame kode dažnai yra naudojama enkapsuliacija norint apsaugoti ir atrinkti teisingus atsakymus iš klausimų. Iš enkapsuliacijos susideta setters ir property funkcijos kurios neleidžia pesiekti svarbių kintamųjų iš išorės.

## Singleton

- Kodėl singleton

Šis kodas naudoja singleton (vienintelio objekto) šabloną. Nors tai yra pats paprasčiausias, šiam projektui jis yra pats svarbiausias kadangi galime prijungti tik vieną įrenginį su vienu COM (laidu) ir mes su singleton turim užtikrinti, kad tik vienas mikrokontroleris valdytų ir nebūtų perrašomi kintamieji.

- Kodėl ne kiti

Nors šablonų yra daug, kaip factory, builder, decorator ir t.t. Šablonas factory būtų reikalingas norint sukurti daug skirtingų LED, builder naudojamas sudėtingam objekto kūrimui. Nors funkcija `@property` yra iš dekoratoriaus, mes nenaudojame viso projekto šablono šiam darbui. 

## Kompozicija ir agregacija

- Kompozicija

Klasė `Ismanus_Projektas` yra glaudžiai susieta su failo *nustatymai.py* duomenimis. Programos veikimo metu projektas negali funkcionuoti be nustatymų objekto. Tai yra ryšys, kur pagrindinis objektas `Projektas` valdo savo sudedamąsias dalis `Nustatymus`.

- Agregacija

Šis principas pasireiškia per tai, kaip programa bendrauja su JSON failu. Nors programa naudoja *nustatymai.json* duomenis, pats failas egzistuoja nepriklausomai nuo to, ar programa yra paleista, ar ne. Taip pat, tie patys nustatymai galėtų būti sukurti ir nenaudojant JSON.

## PEP8 taisyklės

Šis kodas veikia pagal PEP8 taisykles, kaip indentacija, tuščios eilutes prieš ir po klasėmis ir metodais, import, tarpai tarp operacijų, vardų suteikimas, maksimalus eilutes ilgis, enkapsuliacijos. Išskyrus komentarus, tačiau kodas parašytas taip, kad klasės, objektai ir kintamieji būtų suprasti be komentarų.

## Testavimas

Kode yra naudojama testavimo funkcijos norint patikrinti ar visi kintamieji kurie atsiranda iš klausimų yra teisingai enkapsuliuoti. Taip pat atliktas testas patikrinti singleton veikimą ir LED būsenas.

<img width="2136" height="149" alt="Screenshot 2026-04-26 125249" src="https://github.com/user-attachments/assets/d4c778b9-ca58-4d76-bdce-b3cbfed504e6" />

## Failų išsaugojimas ir jų skaitymas

Metodas `uzkrauti_nustatymus()` yra iškviečiamas pradžioje veikimo, kad patikrinti ar failas *nustatymai.json* egzistuoja. Jei ne prasideda klausimai, o jei egzistuoja ir paleidžiamas jis nuskaito failo informacija ir priskirai juos kintamiesiems. Moetodas `issaugoti_nustatymus()` užtikrina, kad nustatyti duomenys atitiktų enkapsuliacija ir būtų išsaugotas i *nustatymai.json* failą.

# Rezultatai ir sunkumai

- Padaryta programa su OOP, kuri valdo Arduino mikrokontroleri ir jo valdyklius.
- Labiau įtvirtintos objektinio programavimo žinios.
- Išmokta, kaip sukurti, atidaryti ir iškviesti naujus failus.
- Išmokta, kaip iškviesti funkcijas naudojant `pyfimata` ir kaip pritaikyti šias funkcijas prie OOP.

Kadangi šis projektas nėra tik apie objektinį programavimą, buvo sunku išmokti ir susieti Arduino funkcijas su python kodu. Taip pat keičiant kodą atsirasdavo klaidų, kurias reikėdavo testuoti per naujo ar taisyti.

Šis projektas galėtų labai lengvai išsiplėsti į milžinišką projektą pridedant daugiau LED, daugiau sensorių ir kitų valdymo būtų. Taip pat galima būtų buve sukurti žaidimą, kuris paleistu visus LED iš eilės ir su mygtuku susdabdyti ant žalio LED.


## Atliko:  
Andrius Dolmantas, EF 25/2
