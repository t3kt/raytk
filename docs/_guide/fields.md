---
layout: page
title: Fields
nav_order: 6
---

# Fields

Fields are operators that are similar to SDFs, but instead of producing hits on surfaces, they come up with either 1 or 4 numeric values (either a `float` or a `vec4`).

Other operators use fields to control behavior depending on where a point is in space.

For example, you can recreate what the [`twist`](/reference/filter/twist) operator does using a [`rotate`](/reference/filter/rotate) with a value field controlling the `Rotate` parameter, applying different amounts of rotation at different coordinates along the axis.


