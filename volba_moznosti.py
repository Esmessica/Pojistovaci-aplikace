class VolbaAkce:

    """
    Třída pro vypsání možností v aplikaci
    """

    def __init__(self):

        """
        Nabídka akcí v aplikaci
        """

        self.__volba_akce_titulek = "\n\nVyberte si akci:\n"
        self.__volba_1 = "1 - Přidat nového pojištěného"
        self.__volba_2 = "2 - Vypsat všechny pojištěné"
        self.__volba_3 = "3 - Vyhledat pojistného"
        self.__volba_4 = "4 - Konec"

    def __str__(self):
        """
        Textová reprezentace nabídky akcí
        """
        return f"{self.__volba_akce_titulek}{self.__volba_1}\n{self.__volba_2}\n{self.__volba_3}\n{self.__volba_4}\n"


