from datetime import date

class Pojistenec:

    """
    Třída pro zápis údajů nových pojištěnců 
    """

    def __init__(self, jmeno_prijmeni= str,vek = str, 
                    telefonni_cislo = str):

        """
        Logika jednotlivých parametrů 

        """

        #logika jména a příjmení
        self._jmeno_prijmeni = jmeno_prijmeni
        self._jmeno, self._prijmeni = jmeno_prijmeni.split(" ")
        self._jmeno = self._jmeno.capitalize()
        self._prijmeni = self._prijmeni.capitalize()
        self._jmeno_a_prijmeni = f"{self._jmeno} {self._prijmeni}"

        #výpočet věku
        self._vek = vek
        den,mesic,rok = self._vek.split(".")
        aktualni_datum = date.today()
        datum_narozeni = date(int(rok),int(mesic), int(den))
        self._vek_uzivatele = aktualni_datum.year - datum_narozeni.year
        #telefonní číslo
        self._telefonni_cislo = telefonni_cislo

        #údaje pojištěnce
        self._udaje_pojisteneho = self._jmeno_a_prijmeni , self._vek_uzivatele,self._telefonni_cislo

        #oddělení textu linkou
        self._odradkovani_od_sekce = "-----------------------------------------------------------------------------\n"

    def __str__(self):

        """
        Textová forma třídy
        
        """
        return f"\n\n{self._odradkovani_od_sekce}Data pro pojištence:\t{self._jmeno} {self._prijmeni},\t{self._vek_uzivatele},\t{self._telefonni_cislo}\t byla uložena...\n"

