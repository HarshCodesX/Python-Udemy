class TeaCup():
    size = "medium"

    def describe(self):
        return f"A {self.size} cup of tea!"

cup = TeaCup()
print(cup.describe())
print(TeaCup.describe(cup))

cup_two = TeaCup()
cup_two.size = "Large"
print(TeaCup.describe(cup_two))
print(cup_two.describe())