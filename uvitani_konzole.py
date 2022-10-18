class UvitaciText:
    """
    Třída pro hodní lištu aplikace
    """

    def __init__(self):
        """
        Název a linka v liště
        """
        self.__linka_konzole = "-----------------------------------------"
        self.__uvitaci_text_konzole = "\tEvidence pojištěných"


    def __str__(self):
        """
        Textová podoba lišty
        """
        return f"{self.__linka_konzole}\n {self.__uvitaci_text_konzole}\n{self.__linka_konzole}\n"
