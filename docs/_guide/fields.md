---
layout: page
title: Fields
nav_order: 7
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

Operators like [`rotate`] use the provided field to decide how much rotation to apply at each position in space. The `rotate` asks the field what the values are for the current position and gets back either a single number of a set of 4 (a vector). If it's a single number, and the `rotate` is using the mode that spins around a single axis, that single number is applied to the rotation around the axis. If it's a vector and `rotate` is using the Euler XYZ mode, the first number is applied to X rotation, the second to Y, the third to Z, and the fourth is ignored.

## Position-Based Fields

The simplest case of a position-based field is [`positionField`]. It takes in the provided coordinates, and just returns them (along with an extra 0 to fill the vector).

The [`pointDistanceField`] is similar, but instead it returns the distance between the provided coordinates and some other point in space. Unlike `positionField`, it returns just a single value (the distance).

Most filters that are used for SDFs can also work for fields that use positions. If you had a `positionField` and you passed that through a  [`translate`] would return values that are offset by some distance.

[`rotate`]: /raytk/reference/operators/filter/rotate
[`positionField`]: /raytk/reference/operators/field/positionField
[`pointDistanceField`]: /raytk/reference/operators/field/pointDistanceField
[`translate`]: /raytk/reference/operators/filter/translate

## Non-Position Fields

While fields make use of the parameters that are passed to them, they don't necessarily have to. Some operators like [`lfoField`] ignore the provided coordinates and use other sources of data to produce values. In the case of `lfoField`, it uses the current time from either the global application time or from the associated timeline.

[`lfoField`]: /raytk/reference/operators/time/lfoField

## Ways That Coordinates are Passed to Fields

When an operator is using a field input, it provides some form of coordinates to that field. The most common case of this is to just pass along the position where that operator is being evaluated. In most (or all) cases where the field accepts the same type of coordinates as the operator that is using it, that same position is being passed along.

In other cases, an operator might accept a field that takes a different type of coordinates than what the operator uses. These operators will provide the field with some other type of value as the coordinates. Each operator that does this handles it differently. For example, if a field using 1D coordinates is passed into [`mobiusRingSdf`], it will give it the angle of the current point around the axis of the ring. This can be used with a [`waveField`] to vary the thickness of the ring with a sine wave that wraps around the ring's axis.

![mobiusRingSdf using angle as coordinate for thickness field](/raytk/assets/images/guide/fields-mobiusRingWaveCoords.png)

Operators that support these types of inputs will document which types of coordinates they support and what kind of values they use for each type.

[`mobiusRingSdf`]: /raytk/reference/operators/sdf/mobiusRingSdf
[`waveField`]: /raytk/reference/operators/field/waveField
