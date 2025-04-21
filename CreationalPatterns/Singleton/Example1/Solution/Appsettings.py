import threading

class Appsettings:
    _instance = None

    def __init__(self):
        if Appsettings._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._database = "jdbc:mysql://localhost:3306/mydatabase"
            self._username = "12345-ABCDE"
            Appsettings._instance = self
        
    def get_instance():
        if Appsettings._instance is None:
            Appsettings()
        return Appsettings._instance

    def get_database(self):
        return self._database

    def get_username(self):
        return self._username
    
if __name__ == "__main__":
    appsettings = Appsettings.get_instance()
    print(f"Database: {appsettings.get_database()}")
    print(f"Username: {appsettings.get_username()}")

    appsettinscopyg = Appsettings.get_instance()
    print(f"Database: {appsettinscopyg.get_database()}")
    print(f"Username: {appsettinscopyg.get_username()}")

    print(appsettings is appsettinscopyg)
    
    # In this code, if we have multiple threads trying to access the singleton instance at the same time,
    # we can have 2 objects created
    # this is not a thread safe implementation of Singleton
    



    # Cons of Singleton
    # 1. make testing difficult
    