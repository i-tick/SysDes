from abc import ABC, abstractmethod

class Teachable(ABC):
    @abstractmethod
    def teach(self):
        pass


class Professor(Teachable):
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")


class University:
    def __init__(self, university_name,professors=None):
        self.university_name = university_name
        self.professors = professors if professors is not None else []

    def show_professors(self):
        print(f"Professors at {self.university_name}:")
        for professor in self.professors:
            professor.teach()


# Example Usage
if __name__ == "__main__":
    prof1 = Professor("Dr. Adams", "Physics")
    prof2 = Professor("Dr. Lee", "Chemistry")
    professors = [prof1, prof2]
    
    university = University("MIT",professors=professors)
    
    
    university.show_professors()