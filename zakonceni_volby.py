import os

class Clear:

    """
    Třída pro vyčištění obrazovky
    """
    
    def cls(self):

        """
        Metoda pro vyčištění obrazovky konzole a inputu na konci volby
        """

        input()
        return os.system('cls' if os.name=='nt' else 'clear')
