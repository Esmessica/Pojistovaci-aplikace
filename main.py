from volba_moznosti import VolbaAkce
from uvitani_konzole import UvitaciText
from logika_volby_akce import LogikaProKonzole

cyklus = LogikaProKonzole()
uvitaci_text = UvitaciText()
volba_akce = VolbaAkce()


cyklus.on = True
while cyklus.on:

    """
    cyklus pro opakované dotazování volby v aplikaci
    """

    print(uvitaci_text)
    print(volba_akce)
    print("\n")
    cyklus.cyklus()
