class OdradkovaniHorniDolni:

    """
    Třída pro  odřádkování 
    """

    def __init__(self):

        self._linka = "-----------------------------------------------------------------------------"
        self._konecny_text = "Pro pokračovní stiskněte libovolnou klávesu...\n"

    def horni(self) :
        return f"{self._linka}\n"

    def dolni(self) :
        return f"\n{self._linka}\n{self._konecny_text}"