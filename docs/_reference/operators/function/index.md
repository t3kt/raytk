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
    summary: Adds the returned values produced by all of the connected input functions.
  - name: almostIdentityFn
    summary: A mapping function that can change a value only when it's zero or very
      close to it, where it replaces the value with a small constant.
  - name: chopFn
    summary: Function that looks up values in a CHOP.
  - name: colorPaletteFn
    status: beta
  - name: crossFn
    summary: Cross-fades between two input functions, either based on a parameter
      or on a third function.
  - name: cubicPulseFn
  - name: easeFn
  - name: extendFn
    status: beta
    summary: Defines the behavior of a function outside the normal expected range
      of coordinates.
  - name: flipFn
    summary: Function that flips its input in one of several different modes.
  - name: gainFn
    summary: A function that expands the sides of the coordinate range and compresses
      the center.
  - name: impulseFn
    summary: Impulse functions that are useful as trigger patterns or animation envelopes.
  - name: joinFn
    summary: Joins functions end on end.
  - name: modulateFn
  - name: multiplyFn
    summary: Multiplies the returned values produced by all of the connected input
      functions.
  - name: parabolaFn
  - name: pennerEasingFn
    summary: Robert Penner's collection of easing functions.
  - name: powerCurveFn
  - name: sincCurveFn
  - name: stepFn
    summary: A function that changes from zero to one at a cutoff point.
  - name: waveFn
    summary: A function that uses a periodic wave, with the position as the parameter.
  summary: Function operators are an advanced type of operator used to control the
    behavior of other types of operators.

---

# Function Operators

Function operators are an advanced type of operator used to control the behavior of other types of operators.

They are similar to field operators, but rather than providing values based on positions in space, they take in and modify simple numeric values.

For example, they can be used to control the curve used to smooth the blending region of a magnet operator, with either a sudden edge, or various types of smoothed transitions.
