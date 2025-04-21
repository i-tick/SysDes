class Appsettings:
    def __init__(self):
        self.database = "localhost"
        self.username = "root"
    def get_database(self):
        return self.database
    def get_username(self):
        return self.username
    
if __name__ == "__main__":
    appsettings = Appsettings()
    print(f"Database: {appsettings.get_database()}")
    print(f"Username: {appsettings.get_username()}")

    appsettinscopyg = Appsettings()
    print(f"Database: {appsettinscopyg.get_database()}")
    print(f"Username: {appsettinscopyg.get_username()}")

    print(appsettings is appsettinscopyg)
    # prints false
    # because we are creating new instance of Appsettings class
    # every time we call Appsettings()
    # this is not a singleton pattern


    # No sharing of resources
    # New obj creation is costly
    # No need of new obj as no attribute is present in the class/ or changing