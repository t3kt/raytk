---
layout: page
title: Fields
nav_order: 6
---

# Fields

Fields are operators that are similar to SDFs, but instead of producing hits on surfaces, they come up with either 1 or 4 numeric values (either a `float` or a `vec4`).

Other operators use fields to control behavior depending on where a point is in space.

For example, you can recreate what the [`twist`](/raytk/reference/operators/filter/twist) operator does using a [`rotate`](/raytk/reference/operators/filter/rotate) with a value field controlling the `Rotate` parameter, applying different amounts of rotation at different coordinates along the axis.

![Rotate and axisDistanceField as twist](/raytk/assets/images/guide/fields-rotateAsTwist.png)

## Field Types

There are two different kinds of data that a field can produce:
* `Float`: a single numeric value.
* `Vector`: 4 numeric values.

ROPs that use fields may support one or both of those types.

## How Fields are Used by ROPs

Operators like [`rotate`](/raytk/reference/operators/filter/rotate) use the provided field to decide how much rotation to apply at each position in space. The `rotate` asks the field what the values are for the current position and gets back either a single number of a set of 4 (a vector). If it's a single number, and the `rotate` is using the mode that spins around a single axis, that single number is applied to the rotation around the axis. If it's a vector and `rotate` is using the Euler XYZ mode, the first number is applied to X rotation, the second to Y, the third to Z, and the fourth is ignored.
