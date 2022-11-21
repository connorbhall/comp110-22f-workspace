"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730465288"


class Simpy:
    """A utility class helpful for working with sequences of data."""
    values: list[float]

    def __init__(self, values: list[float]) -> None:
        """Constructor of the Simpy class."""
        self.values = values
    
    def __repr__(self) -> str:
        """Prints simpy in string form."""
        return f"Simpy({self.values})"

    def fill(self, floaty: float, inty: int) -> None:
        """Fill a simpy's values with specific floats."""
        self.values = []
        for _ in range(inty):
            self.values.append(floaty)
    
    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Creates a range like function."""
        assert step != 0.0
        self.values = []
        inty: float = start
        if step > 0.0:
            while inty < stop:
                self.values.append(inty)
                inty += step
        if step < 0.0:
            while inty > stop:
                self.values.append(inty)
                inty += step
    
    def sum(self) -> float:
        """Adds all parts of the simpy."""
        final: float = 0.0
        final = sum(self.values)
        return final
    
    def __add__(self, b: Union[Simpy, float]) -> Simpy:
        """Allows simpys to be added."""
        i: int = 0
        c: Simpy = Simpy([])
        if isinstance(b, Simpy):
            assert len(self.values) == len(b.values)
            while i < len(self.values):
                c.values.append(self.values[i] + b.values[i])
                i += 1
        if isinstance(b, float):
            while i < len(self.values):
                c.values.append(self.values[i] + b)
                i += 1
        return c
    
    def __pow__(self, b: Union[Simpy, float]) -> Simpy:
        """Allows Simpys to be raised to the power of other Simpys."""
        i: int = 0
        c: Simpy = Simpy([])
        if isinstance(b, Simpy):
            assert len(self.values) == len(b.values)
            while i < len(self.values):
                c.values.append(self.values[i] ** b.values[i])
                i += 1
        if isinstance(b, float):
            while i < len(self.values):
                c.values.append(self.values[i] ** b)
                i += 1
        return c
    
    def __eq__(self, b: Union[Simpy, float]) -> list[bool]:
        """Checks if each object of two simpys are equal."""
        c: list[bool] = []
        i: int = 0
        if isinstance(b, Simpy):
            assert len(self.values) == len(b.values)
            while i < len(self.values):
                if self.values[i] == b.values[i]:
                    c.append(True)
                else:
                    c.append(False)
                i += 1
        if isinstance(b, float):
            while i < len(self.values):
                if self.values[i] == b:
                    c.append(True)
                else:
                    c.append(False)
                i += 1
        return c
    
    def __gt__(self, b: Union[Simpy, float]) -> list[bool]:
        """Checks if a value of a simpy is greater than its corresponding simpy value."""
        c: list[bool] = []
        i: int = 0
        if isinstance(b, Simpy):
            assert len(self.values) == len(b.values)
            while i < len(self.values):
                if self.values[i] > b.values[i]:
                    c.append(True)
                else:
                    c.append(False)
                i += 1
        if isinstance(b, float):
            while i < len(self.values):
                if self.values[i] > b:
                    c.append(True)
                else:
                    c.append(False)
                i += 1
        return c

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """Allows subscription notation to be used for Simpys."""
        if isinstance(rhs, int):
            output: float = 0.0
            output = self.values[rhs]
            return output
        if isinstance(rhs, list):
            assert len(self.values) == len(rhs)
            i: int = 0
            new_simpy: Simpy = Simpy([])
            while i < len(self.values):
                if rhs[i] is True:
                    new_simpy.values.append(self.values[i])
                i += 1
            return new_simpy