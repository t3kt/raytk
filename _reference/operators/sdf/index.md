---
layout: page
title: Sdf Operators
parent: Operator Categories
has_children: true
has_toc: false
---

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.

* [`amazingSurfaceSdf`](amazingSurfaceSdf/) - 
* [`apollonianSdf`](apollonianSdf/) - 
* [`boxFrameSdf`](boxFrameSdf/) - SDF for the squared frame of the edges of a box.
* [`boxSdf`](boxSdf/) - SDF for a box, optionally infinite one one axis.

* [`capsuleSdf`](capsuleSdf/) - 
* [`coneSdf`](coneSdf/) - Defines a cone or capped cone shape.
* [`crossSdf`](crossSdf/) - An SDF for a 3D cross of infinite length along each axis.
* [`cylinderSdf`](cylinderSdf/) - SDF for a cylinder along the Y axis, centered at the origin.
* [`discSdf`](discSdf/) - A flat disc facing the Y axis.
* [`dodecahedronFractalSdf`](dodecahedronFractalSdf/) - 
* [`generalizedPolyhedronSdf`](generalizedPolyhedronSdf/) - Generates one of several different types of polyhedra.
* [`geodesicSdf`](geodesicSdf/) - 
* [`gridSdf`](gridSdf/) - An infinite grid shape, along two axes.
* [`gyroidSdf`](gyroidSdf/) - 
* [`juliaSdf`](juliaSdf/) - 
* [`kaliGeneratorSdf`](kaliGeneratorSdf/) - Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
* [`linkSdf`](linkSdf/) - SDF for a chain link shape (an elongated loop).
* [`mandelbulbSdf`](mandelbulbSdf/) - 
* [`mengerSpongeSdf`](mengerSpongeSdf/) - 
* [`mobiusRingSdf`](mobiusRingSdf/) - SDF for a squared mobius ring.
* [`octahedronSdf`](octahedronSdf/) - An octahedron, with its corners facing the axes.
* [`petalSdf`](petalSdf/) - 
* [`planeSdf`](planeSdf/) - An infinite plane on the x, y, or z axis.
* [`prismSdf`](prismSdf/) - 
* [`pyramidSdf`](pyramidSdf/) - 
* [`sierpinskiTetrahedronSdf`](sierpinskiTetrahedronSdf/) - 
* [`solidAngleSdf`](solidAngleSdf/) - 
* [`sphereSdf`](sphereSdf/) - SDF in 3D space for a uniform sphere.

* [`spiralSdf`](spiralSdf/) - 
* [`tetrahedronSdf`](tetrahedronSdf/) - 
* [`torusSdf`](torusSdf/) - SDF for a torus or partial torus with end caps.
