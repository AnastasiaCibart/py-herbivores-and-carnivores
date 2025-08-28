from __future__ import annotations


class Animal:
    alive: list[Animal] = []

    def _init_(self, name: str, health: int = 100) -> None:
        self.name = name
        self._health = health
        self.hidden = False
        Animal.alive.append(self)

    def _str_(self) -> str:
        return f"""
        {{
            \"Name\": {self.name},
            \"Health\": {self.health}, 
            \"Hidden\": {self.hidden}
        }}"""

    def _repr_(self) -> str:
        return str(self)

    def die(self) -> None:
        self.alive = list(filter(lambda x: x != self, self.alive))

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
    def bite(other: Herbivore) -> None:
        if isinstance(other, Herbivore):
            if not other.hidden:
                other.health -= 50
                if other.health <= 0:
                    other.die()
