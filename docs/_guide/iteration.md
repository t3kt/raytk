---
layout: page
title: Iteration
nav_order: 8
---

# Iteration

Many ROPs effectively repeat the things passed into them multiple times. Iteration is a way for ROPs that feed into those to vary their behavior for different copies. The downstream operator that is repeating things passes "iteration" numbers upstream in the `Context` that is passed between ROPs, and it will vary those numbers for different copies.

Iteration is similar to the "copy stamp" feature in the TouchDesigner [Copy SOP], which evaluates its input chain multiple times and makes values available through the `fetchStamp()` function for parameter expressions.

## Operators That Provide Iteration

Various operators are able to provide iteration values to their inputs.

Some of them will actually run their input multiple times, with a different value each time (which is costly for performance). For example, [`radialClone`] creates multiple copies of its input and merges them together. It has an option to set the iteration values for each of those copies.

![radialClone iteration](/raytk/assets/images/guide/iteration-radialCloneIteration.png)

The other more common type of operator that provides iteration values don't actually run their input multiple times. Instead they decide what iteration value to use based on the position in space. These are much more efficient since they only run their input once. For example, [`modulo1D`] repeats space along an axis, which effectively makes an infinite number of "copies" of that shape. It has an option to pass along the index in that series as the iteration value, so the "copy" in the middle will use 0, the one to the right of that will use 1, and so on, and the one to the left uses -1, etc.

![modulo1D iteration](/raytk/assets/images/guide/iteration-modulo1dIteration.png)


[`modulo1D`]: /raytk/reference/operators/filter/modulo1D
[`radialClone`]: /raytk/reference/operators/filter/radialClone
[Copy SOP]: https://docs.derivative.ca/Copy_SOP
