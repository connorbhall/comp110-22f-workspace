"""The model classes maintain the state and logic of the simulation."""

from __future__ import annotations
from random import random
from exercises.ex09 import constants
from math import sin, cos, pi, sqrt


__author__ = "730465288"


class Point:
    """A model of a 2-d cartesian coordinate Point."""
    x: float
    y: float

    def __init__(self, x: float, y: float):
        """Construct a point with x, y coordinates."""
        self.x = x
        self.y = y

    def add(self, other: Point) -> Point:
        """Add two Point objects together and return a new Point."""
        x: float = self.x + other.x
        y: float = self.y + other.y
        return Point(x, y)
    
    def distance(self, other: Point) -> float:
        """Calculates the distance between two cells."""
        d: float = 0.0
        d = sqrt(((other.x - self.x) ** 2) + ((other.y - self.y) ** 2))
        return d 


class Cell:
    """An individual subject in the simulation."""
    location: Point
    direction: Point
    sickness: int 

    def __init__(self, location: Point, direction: Point, sickness: int = constants.VULNERABLE):
        """Construct a cell with its location and direction."""
        self.location = location
        self.direction = direction
        self.sickness = sickness

    # Part 1) Define a method named `tick` with no parameters.
    # Its purpose is to reassign the object's location attribute
    # the result of adding the self object's location with its
    # direction. Hint: Look at the add method.
    def tick(self) -> None:
        """Describes what happens for each tick of a cell."""
        self.location = self.location.add(self.direction)
        if self.is_infected() is True:
            self.sickness += 1
        if self.sickness > constants.RECOVERY_PERIOD:
            self.immunize()
        
    def color(self) -> str:
        """Return the color representation of a cell."""
        if self.is_vulnerable():
            return "gray"
        if self.is_infected():
            return "lime"
        if self.is_immune():
            return "orange"

    def contract_disease(self) -> None:
        """Infects a cell."""
        self.sickness = constants.INFECTED

    def is_vulnerable(self) -> bool:
        """Checks if a cell is vulnerable."""
        if self.sickness == constants.VULNERABLE:
            return True
        else:
            return False
    
    def is_infected(self) -> bool:
        """Checks if a cell is infected."""
        if self.sickness >= constants.INFECTED:
            return True
        else:
            return False
    
    def contact_with(self, other: Cell) -> None:
        """Infects vulnerable cells if they come in contact with infected cell."""
        if self.is_infected():
            if other.is_vulnerable():
                other.contract_disease()
        if self.is_vulnerable():
            if other.is_infected():
                self.contract_disease()
        if other.is_vulnerable():
            if self.is_infected():
                other.contract_disease()
        if other.is_infected():
            if self.is_vulnerable():
                self.contract_disease()

    def immunize(self) -> None:
        """Immunizes a cell."""
        self.sickness = constants.IMMUNE
    
    def is_immune(self) -> bool:
        """Checks if a cell is immune."""
        if self.sickness == constants.IMMUNE:
            return True
        else:
            return False


class Model:
    """The state of the simulation."""

    population: list[Cell]
    time: int = 0

    def __init__(self, cells: int, speed: float, count: int, immune_cells: int = 0):
        """Initialize the cells with random locations and directions."""
        self.population = []
        if count >= cells:
            raise ValueError("Too many of the cell objects begin infected.")
        if count <= 0:
            raise ValueError("Some number of the cell objects must begin infected.")
        if immune_cells >= cells:
            raise ValueError("Too many of the cell objects begin immune.")
        if immune_cells < 0:
            raise ValueError("There can't be negative immune cells.")
        for _ in range(count):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.INFECTED
            self.population.append(cell)
        for _ in range(immune_cells):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.IMMUNE
            self.population.append(cell)
        for _ in range(cells - (count + immune_cells)):
            start_location: Point = self.random_location()
            start_direction: Point = self.random_direction(speed)
            cell: Cell = Cell(start_location, start_direction)
            cell.sickness = constants.VULNERABLE
            self.population.append(cell)
    
    def tick(self) -> None:
        """Update the state of the simulation by one time step."""
        self.time += 1
        for cell in self.population:
            cell.tick()
            self.enforce_bounds(cell)
        self.check_contacts()

    def random_location(self) -> Point:
        """Generate a random location."""
        start_x: float = random() * constants.BOUNDS_WIDTH - constants.MAX_X
        start_y: float = random() * constants.BOUNDS_HEIGHT - constants.MAX_Y
        return Point(start_x, start_y)

    def random_direction(self, speed: float) -> Point:
        """Generate a 'point' used as a directional vector."""
        random_angle: float = 2.0 * pi * random()
        direction_x: float = cos(random_angle) * speed
        direction_y: float = sin(random_angle) * speed
        return Point(direction_x, direction_y)

    def enforce_bounds(self, cell: Cell) -> None:
        """Cause a cell to 'bounce' if it goes out of bounds."""
        if cell.location.x > constants.MAX_X:
            cell.location.x = constants.MAX_X
            cell.direction.x *= -1.0
        if cell.location.x < constants.MIN_X:
            cell.location.x = constants.MIN_X
            cell.direction.x *= -1.0
        if cell.location.y > constants.MAX_Y:
            cell.location.y = constants.MAX_Y
            cell.direction.y *= -1.0
        if cell.location.y < constants.MIN_Y:
            cell.location.y = constants.MIN_Y
            cell.direction.y *= -1.0

    def check_contacts(self) -> None:
        """Checks if two cells are close enough to contact each other."""
        i: int = 0
        cell_1: Cell
        cell_2: Cell
        for c in range(0, len(self.population)):
            cell_1 = self.population[c]
            i += 1
            for j in range(i, len(self.population)):
                cell_2 = self.population[j]
                if cell_1.location.distance(cell_2.location) < constants.CELL_RADIUS:
                    if cell_1.is_immune() is False and cell_2.is_immune() is False:
                        cell_1.contact_with(cell_2)
    
    def is_complete(self) -> bool:
        """Method to indicate when the simulation is complete."""
        for cell in self.population:
            if cell.is_infected():
                return False
        else:
            return True