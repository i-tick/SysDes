from threading import Lock
from threading import Thread

class Appsettings:
    _instances = {}
    _lock: Lock = Lock()


    
    def __init__(self):
        if self in Appsettings._instances:
            raise Exception("This class is a singleton!")
        else:
            self._database = "jdbc:mysql://localhost:3306/mydatabase"
            self._username = "12345-ABCDE"
        
    def get_instance():

        # Double checked locking is used to prevent the overhead of acquiring the
        # lock every time the Singleton is called. The first check is done
        # without acquiring the lock, and only if the instance is not created yet,
        # the lock is acquired and the instance is created. This way, the lock is
        # only acquired when the instance is created, which is a rare event.
        if Appsettings not in Appsettings._instances:
            with Appsettings._lock:
                # The first thread to acquire the lock, reaches this conditional,
                # goes inside and creates the Singleton instance. Once it leaves the
                # lock block, a thread that might have been waiting for the lock
                # release may then enter this section. But since the Singleton field
                # is already initialized, the thread won't create a new object.
                if Appsettings not in Appsettings._instances:
                    print("Creating new instance")
                    instance = Appsettings()
                    Appsettings._instances[Appsettings] = instance
        return Appsettings._instances[Appsettings]

    def get_database(self):
        return self._database

    def get_username(self):
        return self._username
    
if __name__ == "__main__":
    def access_singleton():
        appsettings = Appsettings.get_instance()
        print(f"Database: {appsettings.get_database()}")
        print(f"Username: {appsettings.get_username()}")
        print()
        return appsettings

    thread1_result = []
    thread2_result = []

    def thread1_task():
        thread1_result.append(access_singleton())

    def thread2_task():
        thread2_result.append(access_singleton())

    thread1 = Thread(target=thread1_task)
    thread2 = Thread(target=thread2_task)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Thread 1 returned instance: {thread1_result[0]}")
    print(f"Thread 2 returned instance: {thread2_result[0]}")
    print(f"Are both instances the same? {thread1_result[0] is thread2_result[0]}")

    

    # print(f"Database: {appsettings.get_database()}")
    # print(f"Username: {appsettings.get_username()}")

    # print(f"Database: {appsettinscopyg.get_database()}")
    # print(f"Username: {appsettinscopyg.get_username()}")

    # print(appsettings is appsettinscopyg) # true
    
    # In this code, if we have multiple threads trying to access the singleton instance at the same time,
    # we can use a lock to ensure that only one thread can create the instance at a time.
    # This is done by using the threading.Lock() object to synchronize access to the singleton instance.
    # This ensures that only one thread can create the instance at a time, preventing multiple instances from being created.
    # This is a thread-safe implementation of Singleton.