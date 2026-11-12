class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


hero1 = Hero(name="Артур", level=5, health=100, strength=20)
hero2 = Hero(name="Мерлин", level=8, health=80, strength=12)

print(f"Начальные характеристики {hero1.name}: здоровье = {hero1.health}, сила = {hero1.strength}")
hero1.greet()
hero1.attack()
hero1.rest()
print(f"После действий {hero1.name}: здоровье = {hero1.health}, сила = {hero1.strength}\n")

print(f"Начальные характеристики {hero2.name}: здоровье = {hero2.health}, сила = {hero2.strength}")
hero2.greet()
hero2.attack()
hero2.rest()
print(f"После действий {hero2.name}: здоровье = {hero2.health}, сила = {hero2.strength}")
