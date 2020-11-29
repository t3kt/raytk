---
layout: page
title: Operator Categories
nav_order: 3
has_children: true
has_toc: false
---

* [Camera](camera/) - Operators that are used in raymarching to determine which
direction rays should travel, effectively behaving as cameras.
* [Combine](combine/) - Operators that take two or more inputs and combine them into a single
output.
* [Convert](convert/) - Operators that convert between different types of coordinates and
return types (SDF, float/vector field, etc).
* [Custom](custom/) - 
* [Field](field/) - Float or vector fields, which provide values for the requested coordinates.
* [Filter](filter/) - Operators that take an input and modify it.
* [Function](function/) - 
* [Light](light/) - Operators that are used in raymarching to define the behavior of light, including
light sources and shadow behaviors.
* [Material](material/) - Material operators that are used by renderers to determine the
color of points on the surface of geometry.
* [Misc](misc/) - Assorted operators that don't fit into other categories.
* [Output](output/) - Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.
* [Post](post/) - 
* [Sdf](sdf/) - Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.
* [Sdf2d](sdf2d/) - Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.
* [Utility](utility/) - Advanced operators that change how ROP chains behave.