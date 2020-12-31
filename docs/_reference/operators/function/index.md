---
layout: operatorCategory
title: Function Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/function/
cat:
  name: function
  summary: |
    Function operators are an advanced type of operator used to control the behavior of other types of operators.
  detail: |
    They are similar to field operators, but rather than providing values based on positions in space, they take in and modify simple numeric values.
    
    For example, they can be used to control the curve used to smooth the blending region of a magnet operator, with either a sudden edge, or various types of smoothed transitions.
  operators:
    - op:
      name: addFn
    - op:
      name: almostIdentityFn
    - op:
      name: chopFn
    - op:
      name: crossFn
    - op:
      name: cubicPulseFn
    - op:
      name: easeFn
    - op:
      name: flipFn
      summary: Function that flips its input in one of several different modes.
    - op:
      name: gainFn
    - op:
      name: impulseFn
    - op:
      name: modulateFn
    - op:
      name: multiplyFn
    - op:
      name: parabolaFn
    - op:
      name: pennerEasingFn
    - op:
      name: powerCurveFn
    - op:
      name: sincCurveFn
    - op:
      name: stepFn
    - op:
      name: waveFn
      summary: A function that uses a periodic wave, with the position as the parameter.

---

# Function Operators

Function operators are an advanced type of operator used to control the behavior of other types of operators.

They are similar to field operators, but rather than providing values based on positions in space, they take in and modify simple numeric values.

For example, they can be used to control the curve used to smooth the blending region of a magnet operator, with either a sudden edge, or various types of smoothed transitions.
