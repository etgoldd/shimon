from dataclasses import dataclass


@dataclass
class Vehicle:
    plate_number: str
    speed: int


@dataclass
class Truck(Vehicle):
    contents: str


@dataclass
class Car(Vehicle):
    pass
