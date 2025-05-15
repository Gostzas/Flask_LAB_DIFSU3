"""
Šitas failas nepriklauso Flask programai, jo paskirtis, užpildyti
tuščią db failą duomenimis.
"""

from app import app, db, Projektas, AtliktasDarbas

with app.app_context():
    db.create_all()

    # Projektai
    projektas1 = Projektas(pavadinimas="Ąžuolų slėnis", kaina=125000)
    projektas2 = Projektas(pavadinimas="Pušų parkas", kaina=135500)
    projektas3 = Projektas(pavadinimas="Ežero namai", kaina=189000)
    projektas4 = Projektas(pavadinimas="Vilnelės rezidencija", kaina=220000)
    projektas5 = Projektas(pavadinimas="Rasos aleja", kaina=143000)

    # Atlikti darbai – skirtingi kiekvienam projektui
    darbas1_1 = AtliktasDarbas(darbas="Geologiniai tyrimai", samata=1500, imone="GeoEkspertai")
    darbas1_1.projektas = projektas1
    darbas1_2 = AtliktasDarbas(darbas="Pamatų liejimas", samata=5200, imone="Statybų lyga")
    darbas1_2.projektas = projektas1
    darbas1_3 = AtliktasDarbas(darbas="Tvoros montavimas", samata=2400, imone="Tvorų meistrai")
    darbas1_3.projektas = projektas1

    darbas2_1 = AtliktasDarbas(darbas="Sklypo paruošimas", samata=1300, imone="Grunto darbininkai")
    darbas2_1.projektas = projektas2
    darbas2_2 = AtliktasDarbas(darbas="Monolitinio karkaso statyba", samata=8900, imone="Betonera")
    darbas2_2.projektas = projektas2
    darbas2_3 = AtliktasDarbas(darbas="Langų montavimas", samata=4100, imone="Stiklas ir Ko")
    darbas2_3.projektas = projektas2

    darbas3_1 = AtliktasDarbas(darbas="Elektros instaliacija", samata=3400, imone="Voltoma")
    darbas3_1.projektas = projektas3
    darbas3_2 = AtliktasDarbas(darbas="Grindų betonavimas", samata=2900, imone="GrindBetonas")
    darbas3_2.projektas = projektas3
    darbas3_3 = AtliktasDarbas(darbas="Vidaus sienų tinkavimas", samata=3700, imone="Tinka ir Dažo")
    darbas3_3.projektas = projektas3

    darbas4_1 = AtliktasDarbas(darbas="Stogo konstrukcija", samata=7600, imone="Stogas LT")
    darbas4_1.projektas = projektas4
    darbas4_2 = AtliktasDarbas(darbas="Ventiliacijos įrengimas", samata=2900, imone="Vėsa ir Trauka")
    darbas4_2.projektas = projektas4
    darbas4_3 = AtliktasDarbas(darbas="Laiptų montavimas", samata=3600, imone="Laiptininkai")
    darbas4_3.projektas = projektas4

    darbas5_1 = AtliktasDarbas(darbas="Fasado apdaila", samata=4800, imone="Fasadai ir Spalvos")
    darbas5_1.projektas = projektas5
    darbas5_2 = AtliktasDarbas(darbas="Grindų klojimas", samata=2500, imone="GrindLT")
    darbas5_2.projektas = projektas5
    darbas5_3 = AtliktasDarbas(darbas="Vandentiekio įrengimas", samata=3100, imone="AquaMontuotojai")
    darbas5_3.projektas = projektas5

    # Likę 25 projektai be darbų
    projektas6 = Projektas(pavadinimas="Saulėtekio dvaras", kaina=250000)
    projektas7 = Projektas(pavadinimas="Smėlio sodas", kaina=98000)
    projektas8 = Projektas(pavadinimas="Šilo kiemas", kaina=119000)
    projektas9 = Projektas(pavadinimas="Pajūrio kalvos", kaina=205000)
    projektas10 = Projektas(pavadinimas="Beržų krantas", kaina=178000)
    projektas11 = Projektas(pavadinimas="Kalnų slėnis", kaina=199000)
    projektas12 = Projektas(pavadinimas="Marių parkas", kaina=188000)
    projektas13 = Projektas(pavadinimas="Lauko namai", kaina=99000)
    projektas14 = Projektas(pavadinimas="Miško rezidencija", kaina=210000)
    projektas15 = Projektas(pavadinimas="Gintaro aleja", kaina=145000)
    projektas16 = Projektas(pavadinimas="Ąžuolų parkas", kaina=153000)
    projektas17 = Projektas(pavadinimas="Pušų dvaras", kaina=240000)
    projektas18 = Projektas(pavadinimas="Ežero sodas", kaina=105000)
    projektas19 = Projektas(pavadinimas="Vilnelės kiemas", kaina=128000)
    projektas20 = Projektas(pavadinimas="Rasos kalvos", kaina=172000)
    projektas21 = Projektas(pavadinimas="Saulėtekio krantas", kaina=198000)
    projektas22 = Projektas(pavadinimas="Smėlio slėnis", kaina=132000)
    projektas23 = Projektas(pavadinimas="Šilo parkas", kaina=141000)
    projektas24 = Projektas(pavadinimas="Pajūrio namai", kaina=215000)
    projektas25 = Projektas(pavadinimas="Beržų rezidencija", kaina=193000)
    projektas26 = Projektas(pavadinimas="Kalnų aleja", kaina=148000)
    projektas27 = Projektas(pavadinimas="Marių dvaras", kaina=235000)
    projektas28 = Projektas(pavadinimas="Lauko sodas", kaina=97000)
    projektas29 = Projektas(pavadinimas="Miško kiemas", kaina=118000)
    projektas30 = Projektas(pavadinimas="Gintaro kalvos", kaina=179000)

    # Įrašymas į DB
    db.session.add_all([
        projektas1, projektas2, projektas3, projektas4, projektas5,
        projektas6, projektas7, projektas8, projektas9, projektas10,
        projektas11, projektas12, projektas13, projektas14, projektas15,
        projektas16, projektas17, projektas18, projektas19, projektas20,
        projektas21, projektas22, projektas23, projektas24, projektas25,
        projektas26, projektas27, projektas28, projektas29, projektas30,])

    db.session.commit()
