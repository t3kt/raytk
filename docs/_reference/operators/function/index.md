---
layout: operatorCategory
title: Function Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/function/
cat:
  detail: 'They are similar to field operators, but rather than providing values based
    on positions in space, they take in and modify simple numeric values.


    For example, they can be used to control the curve used to smooth the blending
    region of a magnet operator, with either a sudden edge, or various types of smoothed
    transitions.'
  name: function
  operators:
  - name: addFn
  - name: almostIdentityFn
  - name: chopFn
  - name: crossFn
  - name: cubicPulseFn
  - name: easeFn
  - name: flipFn
    summary: Function that flips its input in one of several different modes.
  - name: gainFn
  - name: impulseFn
  - name: joinFn
  - name: modulateFn
  - name: multiplyFn
  - name: parabolaFn
  - name: pennerEasingFn
  - name: powerCurveFn
  - name: sincCurveFn
  - name: stepFn
  - name: waveFn
    summary: A function that uses a periodic wave, with the position as the parameter.
  summary: Function operators are an advanced type of operator used to control the
    behavior of other types of operators.

---

# Function Operators

Function operators are an advanced type of operator used to control the behavior of other types of operators.

They are similar to field operators, but rather than providing values based on positions in space, they take in and modify simple numeric values.

For example, they can be used to control the curve used to smooth the blending region of a magnet operator, with either a sudden edge, or various types of smoothed transitions.
