---
layout: page
title: Iteration
nav_order: 8
---

# Iteration

Many ROPs effectively repeat the things passed into them multiple times. Iteration is a way for ROPs that feed into those to vary their behavior for different copies. The downstream operator that is repeating things passes "iteration" numbers upstream in the `Context` that is passed between ROPs, and it will vary those numbers for different copies.

Iteration is similar to the "copy stamp" feature in the TouchDesigner [Copy SOP], which evaluates its input chain multiple times and makes values available through the `fetchStamp()` function for parameter expressions.

[Copy SOP]: https://docs.derivative.ca/Copy_SOP

## Operators That Provide Iteration

Various operators are able to provide iteration values to their inputs.

Some of them will actually run their input multiple times, with a different value each time (which is costly for performance). For example, [`radialClone`] creates multiple copies of its input and merges them together. It has an option to set the iteration values for each of those copies.

![radialClone iteration](/raytk/assets/images/guide/iteration-radialClone-series.png)

The other more common type of operator that provides iteration values don't actually run their input multiple times. Instead they decide what iteration value to use based on the position in space. These are much more efficient since they only run their input once. For example, [`modulo1D`] repeats space along an axis, which effectively makes an infinite number of "copies" of that shape. It has an option to pass along the index in that series as the iteration value, so the "copy" in the middle will use 0, the one to the right of that will use 1, and so on, and the one to the left uses -1, etc.

![modulo1D iteration](/raytk/assets/images/guide/iteration-modulo1D-series.png)

`modulo1D` also has an option to produce alternating 0 and 1 as its iteration values.

![modulo1D iteration](/raytk/assets/images/guide/iteration-modulo1D-toggle.png)

[`modulo1D`]: /raytk/reference/operators/filter/modulo1D
[`radialClone`]: /raytk/reference/operators/filter/radialClone

## Operators That Consume Iteration

There are several operators that can make use of the iteration values that are passed to them from downstream ops.

The simplest of these is the [`iterationField`], which is a [field] operator that returns either the whole iteration `vec4` or a single part of the iteration (x/y/z/w). It can be used as an input to control the behavior of other ops, such as [`translate`], which has the effect of applying a different amount of translation for each iteration. In that case, it also may need a [`floatToVector`] to convert from a single iteration value to the vector that `translate` expects.

![modulo1D iteration](/raytk/assets/images/guide/iteration-modulo1D-translate.png)

![modulo1D iteration](/raytk/assets/images/guide/iteration-modulo1D-translate-network.png)

The [`iterationSwitch`] operator takes two SDF inputs, and toggles between them based on the iteration value. It has options for how it handles values outside the 0 to 1 range (either clamping or toggling back and forth).

![modulo1D iteration](/raytk/assets/images/guide/iteration-iterationSwitch.png)


[field]: /raytk/guide/fields
[`floatToVector`]: /raytk/reference/operators/convert/floatToVector
[`iterationField`]: /raytk/reference/operators/field/iterationField
[`iterationSwitch`]: /raytk/reference/operators/combine/iterationSwitch
[`translate`]: /raytk/reference/operators/filter/translate
