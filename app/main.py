class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    def __str__(self) -> str:
        return (
            f"{{Name: {self.name}, "
            f"Health: {self.health}, Hidden: {self.hidden}}}"
        )

    def __repr__(self) -> str:
        return str(self)

    def die(self) -> None:
        print(Animal.alive)
        print("die")
        Animal.alive = list(
            filter(lambda x: x.name != self.name, Animal.alive)
        )
        print(Animal.alive)

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int) -> None:
        if value < 0:
            return self.die()
        self._health = value


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(other: "Herbivore") -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                if other.health <= 0:
                    other.die()


def main_function() -> None:
    lion = Carnivore("Simba")
    print(len(Animal.alive) == 1)
    print(isinstance(Animal.alive[0], Carnivore) is True)

    rabbit = Herbivore("Susan")
    rabbit.hide()
    print(rabbit.hidden is True)

    lion = Carnivore("Lion King")
    rabbit = Herbivore("Susan")
    print(rabbit.health == 100)
    lion.bite(rabbit)
    print(rabbit.health == 50)  # bited

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 50)  # lion cannot bite hidden rabbit

    rabbit.hide()
    lion.bite(rabbit)
    print(rabbit.health == 0)  # rabbit is dead

    print(rabbit in Animal.alive)  # False
    # there is no dead animals in Animal.alive


if __name__ == "__main__":
    main_function()
