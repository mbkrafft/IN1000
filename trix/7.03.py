class Student:

    def __init__(self, navn, quiz_score=0, antall_quizzer=0):
        self.navn = navn
        self.quiz_score = quiz_score
        self.antall_quizzer = antall_quizzer

    def legg_til_quiz_score(self, score):
        self.quiz_score += score
        self.antall_quizzer += 1

    def gjennomsnittlig_score(self):
        return self.quiz_score / self.antall_quizzer

    def skriv_ut(self):
        print(f"{self.navn} har tatt {self.antall_quizzer} quizzer, har en total score paa {self.quiz_score} og en snittscore paa {round(self.gjennomsnittlig_score(), 2)}")


# lager instanser av elever
elev1 = Student("Joakim")
elev2 = Student("Kristin")
elev3 = Student("Dag")

# legger til score for hver elev
elev1.legg_til_quiz_score(10)
elev1.legg_til_quiz_score(10)
elev1.legg_til_quiz_score(10)

elev2.legg_til_quiz_score(100)
elev2.legg_til_quiz_score(100)
elev2.legg_til_quiz_score(100)

elev3.legg_til_quiz_score(50)
elev3.legg_til_quiz_score(50)
elev3.legg_til_quiz_score(50)

# skriver ut hver elev sin informasjon
elev1.skriv_ut()
elev2.skriv_ut()
elev3.skriv_ut()
