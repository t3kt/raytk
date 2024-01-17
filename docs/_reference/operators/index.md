---
layout: page
title: Operators
nav_order: 3
has_children: true
has_toc: false
permalink: /reference/operators/
---

# Operator Categories
* [Camera](camera/) - Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.
* [Combine](combine/) - Operators that take two or more inputs and combine them into a single
output.
* [Convert](convert/) - Operators that convert between different types of coordinates and
return types (SDF, float/vector field, etc).
* [Custom](custom/) - Custom operators can be used to write custom GLSL code and run it in the context of a RayTK scene.
* [Field](field/) - Float or vector fields, which provide values for the requested coordinates.
* [Filter](filter/) - Operators that take an input and modify it.
* [Function](function/) - Function operators are an advanced type of operator used to control the behavior of other types of operators.
* [Geo](geo/) - 
* [Light](light/) - Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.
* [Material](material/) - Material operators that are used by renderers to determine the
color of points on the surface of geometry.
* [Output](output/) - Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.
* [Particles](particles/) - 
* [Pattern](pattern/) - 2D pattern generators, which can be used for things like textures.
Pattern operators are essentially a sub-category of field operators that focus
on producing value or color patterns using 2D coordinates.

* [Post](post/) - 
* [Sdf](sdf/) - Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.
* [Sdf2d](sdf2d/) - Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.
* [Time](time/) - Operators that do time-based calculations.
* [Utility](utility/) - Advanced operators that change how ROP chains behave.