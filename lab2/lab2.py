class student:
    def __init__(self, student_id, name, specialnost):
        self.student_id = student_id
        self.name = name
        self.specialnost = specialnost
        self.semesr = 1
        self.discipliny = {}

class discipliny:
    def __init__(self, name, kafedra, specialnost):
        self.name = name
        self.kafedra = kafedra
        self.specialnost = specialnost
        