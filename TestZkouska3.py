
class Osoba:
    def __init__(self, jmeno, věk) -> None:
        self.jmeno = jmeno
        self.věk = věk

    def __str__(self) -> str:
        return f"Osoba(jmeno={self.jmeno}, věk={self.vek})"

class Student(Osoba):
    def __init__(self, jmeno, věk, ročník) -> None:
        super().__init__(jmeno, věk)
        self.ročník = ročník

    def __str__(self) -> str:
        return f"Student {self.jmeno} studuje {self.ročník}. ročník"

class Učitel(Osoba):
    def __init__(self, jmeno, věk, obor) -> None:
        super().__init__(jmeno, věk)
        self.obor = obor

    def __str__(self) -> str:
        return f"Učitel {self.jmeno} učí obor {self.obor}"
if __name__ == "__main__":
    student1 = Student("Adam", 20, 2)
    student2 = Student("Eva", 19, 1)
    učitel = Učitel("Tomáš", 40, "IT")

    print(student1)
    print(student2)
    print(učitel)