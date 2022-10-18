from pojistenec import Pojistenec
from evidence import EvidencePojistenychOsob
from odradkovani_horni_dolni import  OdradkovaniHorniDolni
from zakonceni_volby import Clear
 
class LogikaProKonzole:
    """
    Třída pro logiku cyklu v konzolové aplikaci
    """
    def cyklus(self):
        self.on = True
        # metoda pro použití do cyklu v main souboru + logika volby

        evidence = EvidencePojistenychOsob()
        odradkovani = OdradkovaniHorniDolni()
        
        zakonceni = Clear()

        __ciselna_volba_akce = int(input("Zvolte číslo akce: "))

        if __ciselna_volba_akce == 1:

            pojisteny = Pojistenec(input("\nZadejte jméno a příjmení:\t"), input("\nZadejte datum narození pojištěnce ve formátu DD.MM.YYYY:\t"), input("\nZadejte telefonní číslo:\t"))
            print(pojisteny)
            evidence.evidence.append(pojisteny._udaje_pojisteneho) 
            print(odradkovani.dolni())
            #clear obrazovky
            zakonceni.cls()

        elif __ciselna_volba_akce == 2:

            print("\nVýpis pojištěných osob:")
            print(odradkovani.horni())
            for jmeno, vek, tel_cislo in evidence.evidence:
                print(f"Jméno:  {jmeno}\t Věk:  {vek}\tTelefonní číslo:  {tel_cislo}")
                print("\n")
            print(odradkovani.dolni())
            
            #clear obrazovky
            zakonceni.cls()

        elif __ciselna_volba_akce == 3:

            print("\nVyhledání pojištěnce")
            print(odradkovani.horni())
            jmeno_prijmeni_before = input("Zadejte jméno a příjmení pojištěnce:\t")
            print("\n", odradkovani.horni())
            jmeno_pro_vyhledavani, prijmeni_pro_vyhledavani = jmeno_prijmeni_before.split(" ")
            jmeno_pro_vyhledavani = jmeno_pro_vyhledavani.capitalize()
            prijmeni_pro_vyhledavani = prijmeni_pro_vyhledavani.capitalize()
            jmeno_prijmeni_pro_vyhledani = f"{jmeno_pro_vyhledavani} {prijmeni_pro_vyhledavani}"
            for jmeno_prijmeni, vek, tel_cislo in evidence.evidence:
                if jmeno_prijmeni == jmeno_prijmeni_pro_vyhledani:
                        print(f"Jméno:  {jmeno_prijmeni} \t Věk:  {vek}\tTelefonní číslo:  {tel_cislo}")
                        print("\n")
                        break
                elif jmeno_prijmeni_pro_vyhledani not in evidence.evidence:
                        print("Jméno není v databázi evidováno.")
                        break
                        
            print(odradkovani.dolni())
            
            #vypracovat vyhledání pojištěné osoby
            zakonceni.cls()

        elif __ciselna_volba_akce == 4:

            self.on = False
            print("\nAplikace ukončena...")
            print("\n")

        else:
            print("Neplatná volba akce!") 
            print("\n")