import os

class Consloe:
    def clear():
        """
        Clears the console screen.
        
        This method uses the 'cls' command to clear the screen in Windows and 'clear' command to clear the screen in Unix-like systems.
        
        Usage example:
        >>> Console.clear()
        """
        os.system('cls' if os.name == 'nt' else 'clear')
