def uzduoti_klausimai(projektas):
    while projektas.spalva is None:
        projektas.spalva = (
            input("Ar norite pajungti žalią, geltoną, " \
                  "raudoną ar visus tris LED? (z/g/r/v)\n")
        )
    while projektas.mirksejimas is None:
        projektas.mirksejimas = (
            input("Ar norite kad LED mirgsėtų ar ne? (t/n)\n")
        )
    if projektas.mirksejimas == 't':
        while projektas.potenciometro_funkcija is None:
            projektas.potenciometro_funkcija = (
                input("Ar norite naudoti potenciometrą " \
                      "mirksėjimui ar nustatyti? (1/2)\n")
            )
        if projektas.potenciometro_funkcija == '2':
            while projektas.laikas is None:
                    laikinas_laikas = (
                        input("Kas kiek laiko norite, " \
                                    "kad mirksėtų? (0.1s iki 10s)\n")
                    )
                    try:
                        skaicius = float(laikinas_laikas)
                        projektas.laikas = skaicius
                    except ValueError:
                        print("Neteisingai pasirinkas atsakymas.")

    if projektas.mirksejimas == 'n':
        while projektas.mygtuko_funkcija is None:
            projektas.mygtuko_funkcija = (
                input("Ar norite junginėti LED su mygtuku " \
                      "ar tik ijungti? (1/2)\n")
            )
        if projektas.mygtuko_funkcija == '2':
            while projektas. potenciometro_ryskumas is None:
                projektas.potenciometro_ryskumas = (
                    input("Ar nori valdyti LED ryškumą su " \
                          "potenciometru? (t/n)\n")
                )