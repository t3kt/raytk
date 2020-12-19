---
layout: page
title: Sdf Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/sdf/
---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.

* [`amazingSurfaceSdf`](amazingSurfaceSdf/) - 
* [`apollonianSdf`](apollonianSdf/) - 
* [`boxFrameSdf`](boxFrameSdf/) - SDF for the squared frame of the edges of a box.
* [`boxSdf`](boxSdf/) - SDF for a box, optionally infinite one one axis.
* [`capsuleSdf`](capsuleSdf/) - A cylinder with rounded ends, between two points.
* [`coneSdf`](coneSdf/) - Defines a cone or capped cone shape.
* [`crossSdf`](crossSdf/) - An SDF for a 3D cross of infinite length along each axis.
* [`cylinderSdf`](cylinderSdf/) - SDF for a cylinder along the Y axis, centered at the origin.
* [`discSdf`](discSdf/) - A flat disc facing the Y axis.
* [`dodecahedronFractalSdf`](dodecahedronFractalSdf/) -  *beta*{: .label .status-beta }
* [`generalizedPolyhedronSdf`](generalizedPolyhedronSdf/) - Generates one of several different types of polyhedra.
* [`geodesicSdf`](geodesicSdf/) - A geodesic polyhedron, optionally with a spike on each face.
* [`gridSdf`](gridSdf/) - An infinite grid shape, along two axes.
* [`gyroidSdf`](gyroidSdf/) - Gyroid shape, which is an infinitely connected periodic surface.
* [`juliaSdf`](juliaSdf/) - 
* [`kaliGeneratorSdf`](kaliGeneratorSdf/) - Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
* [`linkSdf`](linkSdf/) - SDF for a chain link shape (an elongated loop).
* [`mandelbulbSdf`](mandelbulbSdf/) - Mandelbulb fractal.
* [`mengerSpongeSdf`](mengerSpongeSdf/) - Menger sponge fractal, made of boxes with holes cut through each axis.
* [`mobiusRingSdf`](mobiusRingSdf/) - SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.
* [`octahedronSdf`](octahedronSdf/) - An octahedron, with its corners facing the axes.
* [`petalSdf`](petalSdf/) - A flower petal or leaf shape.
* [`planeSdf`](planeSdf/) - An infinite plane on the x, y, or z axis.
* [`prismSdf`](prismSdf/) - A prism shape, like a cylinder but with flat sides, along the z axis.
* [`pyramidSdf`](pyramidSdf/) - A pyramid with four sides.
* [`solidAngleSdf`](solidAngleSdf/) - A conical slice of a sphere.
* [`sphereSdf`](sphereSdf/) - SDF in 3D space for a uniform sphere.
* [`spiralSdf`](spiralSdf/) - A tapering spiral squared tube.
* [`tetrahedronSdf`](tetrahedronSdf/) - Tetrahedron shape.
* [`torusSdf`](torusSdf/) - SDF for a torus or partial torus with end caps.
