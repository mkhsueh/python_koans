#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    validateSides(a, b, c)        
    if a == b == c :
        return 'equilateral'
    elif a != b != c != a : 
        return 'scalene'
    else : 
        return 'isosceles'

def validateSides(a, b, c):
    sides = (a, b, c)
    if 0 in sides :
        raise TriangleError('sides cannot be of length 0')
    if not all(n > 0 for n in sides) :
        raise TriangleError('side cannot be of negative length')
    if sides[0] + sides[1] < sides[2] or sides[1] + sides[2] < sides[0] or sides[0] + sides[2] < sides[1] :
        raise TriangleError('invalid combination of side lengths')

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
