import pytest
from nustatymai import Projekto_Nustatymai


@pytest.fixture
def nustatymai():
    return Projekto_Nustatymai()

def test_spalva_setter_teisinga(nustatymai):
    nustatymai.spalva = " Z "
    assert nustatymai.spalva == "z"
    nustatymai.spalva = " G "
    assert nustatymai.spalva == "g"
    nustatymai.spalva = " R "
    assert nustatymai.spalva == "r"
    nustatymai.spalva = " V "
    assert nustatymai.spalva == "v"

def test_spalva_setter_klaidinga(nustatymai):
    nustatymai.spalva = "mėlyna"
    assert nustatymai. spalva is None
    nustatymai.spalva = "geltona"
    assert nustatymai. spalva is None
    nustatymai.spalva = "raudona"
    assert nustatymai. spalva is None
    nustatymai.spalva = "visi"
    assert nustatymai. spalva is None

def test_mirksejimas_setter_teisinga(nustatymai):
    nustatymai.mirksejimas = " T "
    assert nustatymai.mirksejimas == "t"
    nustatymai.mirksejimas = " N "
    assert nustatymai.mirksejimas == "n"

def test_mirksejimas_setter_klaidinga(nustatymai):
    nustatymai.mirksejimas = " Taip "
    assert nustatymai.mirksejimas is None
    nustatymai.mirksejimas = " Ne "
    assert nustatymai.mirksejimas is None

def test_potenciometro_funkcija_setter_teisinga(nustatymai):
    nustatymai.potenciometro_funkcija = " 1 "
    assert nustatymai.potenciometro_funkcija == "1"
    nustatymai.potenciometro_funkcija = " 2 "
    assert nustatymai.potenciometro_funkcija == "2"

def test_potenciometro_funkcija_setter_klaidinga(nustatymai):
    nustatymai.potenciometro_funkcija = " Taip "
    assert nustatymai.potenciometro_funkcija is None
    nustatymai.potenciometro_funkcija = " Ne "
    assert nustatymai.potenciometro_funkcija is None

def test_laikas_setter_teisingos_reiksmes(nustatymai):
    nustatymai.laikas = 0.1
    assert nustatymai.laikas == 0.1
    nustatymai.laikas = 10
    assert nustatymai.laikas == 10

def test_laikas_setter_klaidingos_reiksmes(nustatymai):
    nustatymai.laikas = 0.05
    assert nustatymai.laikas is None
    nustatymai.laikas = 11
    assert nustatymai.laikas is None
    
def test_mygtuko_setter_teisinga(nustatymai):
    nustatymai.mygtuko_funkcija = " 1 "
    assert nustatymai.mygtuko_funkcija == "1"
    nustatymai.mygtuko_funkcija = " 2 "
    assert nustatymai.mygtuko_funkcija == "2"

def test_mygtuko_setter_klaidinga(nustatymai):
    nustatymai.mygtuko_funkcija = " Taip "
    assert nustatymai.mygtuko_funkcija is None
    nustatymai.mygtuko_funkcija = " Ne "
    assert nustatymai.mygtuko_funkcija is None

def test_potenciometro_ryskumas_setter_teisinga(nustatymai):
    nustatymai.potenciometro_ryskumas = " T "
    assert nustatymai.potenciometro_ryskumas == "t"
    nustatymai.potenciometro_ryskumas = " N "
    assert nustatymai.potenciometro_ryskumas == "n"

def test_potenciometro_ryskumas_setter_klaidinga(nustatymai):
    nustatymai.potenciometro_ryskumas = " Taip "
    assert nustatymai.potenciometro_ryskumas is None
    nustatymai.potenciometro_ryskumas = " Ne "
    assert nustatymai.potenciometro_ryskumas is None
    
def test_pasirinkimas_duomenu_teisinga(nustatymai):
    nustatymai.mygtuko_funkcija = " 1 "
    assert nustatymai.mygtuko_funkcija == "1"
    nustatymai.mygtuko_funkcija = " 2 "
    assert nustatymai.mygtuko_funkcija == "2"

def test_pasirinkimas_duomenu_klaidinga(nustatymai):
    nustatymai.mygtuko_funkcija = " Taip "
    assert nustatymai.mygtuko_funkcija is None
    nustatymai.mygtuko_funkcija = " Ne "
    assert nustatymai.mygtuko_funkcija is None