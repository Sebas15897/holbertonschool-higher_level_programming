#!/usr/bin/python3
"""import"""
from models.base import Base


class Rectangle(Base):
      """docstring for class and super class"""
      def __init__(self, width, height, x=0, y=0, id=None):
            """instances"""
            super().__init__(id)
            self.width = width
            self.heigth = height
            self.x = x
            self.y = y

      @property
      def width(self):
"""width"""
                  return self._width
            @property
            def heigth(self):
                  """heigth"""
                  return self._heigth
            @property
            def x(self):
                  """x"""
                  return self._x
            @property
            def y(self):
                  """y"""
                  return self._y