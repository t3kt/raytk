---
layout: page
title: generalizedPolyhedronSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/generalizedPolyhedronSdf
---

# generalizedPolyhedronSdf



Generates one of several different types of polyhedra.

Based on ["Generalized Distance Functions"](http://people.tamu.edu/~ergun/research/implicitmodeling/papers/sm99.pdf) by Akleman and Chen.

* `Shape` - chooses between several different predefined types of polyhedra, or `Custom`, which uses the `Begin` and `End` parameters to generate different shapes.
* `Begin` - only used when the `Custom` shape. It's a bit hard to describe, so it's best to just experiment with it and see how it behaves.
* `End` - used along with `Begin`.
* `Translate` - shifts the center of the shape.
* `Radius` - the size of the shape.
* `Use Exponent` - enables the use of the `Exponent`, which controls the sharpness of the edges. When this is switched off, the shape will have sharp edges.
* `Exponent` - controls the sharpness or smoothness of the edges.
