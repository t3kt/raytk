---
layout: operatorCategory
title: Sdf Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/sdf/
cat:
  name: sdf
  summary: |
    Signed distances functions which define geometry in 3D space, by calculating
    the distance from the surface of the shape at any given point.
  detail: |
    These operators are how geometry is defined for raymarching, and they are
    often the first operator in a chain that ends with a `raymarchRender3d`.
  operators:
    - op:
      name: amazingSurfaceSdf
    - op:
      name: apollonianSdf
    - op:
      name: boxFrameSdf
      summary: SDF for the squared frame of the edges of a box.
    - op:
      name: boxSdf
      summary: SDF for a box, optionally infinite one one axis.
    - op:
      name: capsuleSdf
      summary: A cylinder with rounded ends, between two points.
    - op:
      name: coneSdf
      summary: Defines a cone or capped cone shape.
    - op:
      name: crossSdf
      summary: An SDF for a 3D cross of infinite length along each axis.
    - op:
      name: cylinderSdf
      summary: SDF for a cylinder along the Y axis, centered at the origin.
    - op:
      name: discSdf
      summary: A flat disc facing the Y axis.
    - op:
      name: dodecahedronFractalSdf
      status: beta
    - op:
      name: generalizedPolyhedronSdf
      summary: Generates one of several different types of polyhedra.
    - op:
      name: geodesicSdf
      summary: A geodesic polyhedron, optionally with a spike on each face.
    - op:
      name: gridSdf
      summary: An infinite grid shape, along two axes.
    - op:
      name: gyroidSdf
      summary: Gyroid shape, which is an infinitely connected periodic surface.
    - op:
      name: juliaSdf
    - op:
      name: kaliGeneratorSdf
      summary: Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
    - op:
      name: linkSdf
      summary: SDF for a chain link shape (an elongated loop).
    - op:
      name: mandelbulbSdf
      summary: Mandelbulb fractal.
    - op:
      name: mengerSpongeSdf
      summary: Menger sponge fractal, made of boxes with holes cut through each axis.
    - op:
      name: mobiusRingSdf
      summary: SDF for a squared mobius ring, which is like a rectangular bar twisted and then bent into a ring.
    - op:
      name: octahedronSdf
      summary: An octahedron, with its corners facing the axes.
    - op:
      name: petalSdf
      summary: A flower petal or leaf shape.
    - op:
      name: planeSdf
      summary: An infinite plane on the x, y, or z axis.
    - op:
      name: prismSdf
      summary: A prism shape, like a cylinder but with flat sides, along the z axis.
    - op:
      name: pyramidSdf
      summary: A pyramid with four sides.
    - op:
      name: solidAngleSdf
      summary: A conical slice of a sphere.
    - op:
      name: sphereSdf
      summary: SDF in 3D space for a uniform sphere.
    - op:
      name: spiralSdf
      summary: A tapering spiral squared tube.
    - op:
      name: tetrahedronSdf
      summary: Tetrahedron shape.
    - op:
      name: torusSdf
      summary: SDF for a torus or partial torus with end caps.

---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.
