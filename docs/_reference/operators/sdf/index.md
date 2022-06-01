---
layout: operatorCategory
title: Sdf Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/sdf/
cat:
  detail: 'These operators are how geometry is defined for raymarching, and they are

    often the first operator in a chain that ends with a `raymarchRender3d`.'
  name: sdf
  operators:
  - keywords:
    - fractal
    name: amazingSurfaceSdf
  - keywords:
    - apollonian
    - fractal
    name: apollonianSdf
  - name: archSdf
    status: beta
  - keywords:
    - bezier
    - curve
    - line
    name: bezierSdf
    status: beta
  - keywords:
    - box
    - cube
    - frame
    - rectangle
    - square
    name: boxFrameSdf
    shortcuts:
    - bfs
    summary: SDF for the squared frame of the edges of a box.
  - keywords:
    - box
    - cube
    - rectangle
    - square
    name: boxSdf
    shortcuts:
    - box
    summary: SDF for a box, optionally infinite one one axis.
  - name: bunnySdf
    summary: SDF for a bunny.
  - keywords:
    - capsule
    - line
    - points
    - segment
    name: capsuleSdf
    summary: A cylinder with rounded ends, between two points.
  - name: chainSdf
    status: beta
  - keywords:
    - box
    - chamfer
    - cube
    name: chamferBoxSdf
  - name: coneSdf
    summary: Defines a cone or capped cone shape.
  - name: crescentSdf
    status: beta
  - name: crossSdf
    summary: An SDF for a 3D cross of infinite length along each axis.
  - name: cutSphereSdf
    status: beta
  - keywords:
    - column
    - cylinder
    - pipe
    name: cylinderSdf
    summary: SDF for a cylinder.
  - name: discSdf
    summary: A flat disc facing the Y axis.
  - name: dodecahedronFractalSdf
    status: beta
  - keywords:
    - circle
    - ellipse
    - ellipsoid
    - oval
    - sphere
    name: ellipsoidSdf
  - keywords:
    - dodecahedron
    - icosahedron
    - octahedron
    - polyhedron
    name: generalizedPolyhedronSdf
    summary: Generates one of several different types of polyhedra.
  - keywords:
    - geodesic
    - polyhedron
    - spikes
    name: geodesicSdf
    summary: A geodesic polyhedron, optionally with a spike on each face.
  - keywords:
    - bars
    - grid
    name: gridSdf
    summary: An infinite grid shape, along two axes.
  - keywords:
    - gyroid
    - sine
    - wave
    name: gyroidSdf
    summary: Gyroid shape, which is an infinitely connected periodic surface.
  - name: headSdf
    status: beta
  - keywords:
    - coil
    - helix
    - spiral
    name: helixSdf
    summary: SDF for a helix (an elongated spiral).
  - name: jointSdf
    status: beta
  - keywords:
    - fractal
    - julia
    - quaternion
    name: juliaSdf
    status: beta
  - name: kaliGeneratorSdf
    summary: Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
  - name: latticeSdf
    status: beta
  - keywords:
    - chain
    - link
    name: linkSdf
    summary: SDF for a chain link shape (an elongated loop).
  - keywords:
    - fractal
    - mandelbrot
    - mandelbulb
    name: mandelbulbSdf
    summary: Mandelbulb fractal.
  - name: mengerSpongeSdf
    summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  - keywords:
    - mobius
    - ring
    - twist
    name: mobiusRingSdf
    summary: SDF for a squared mobius ring, which is like a rectangular bar twisted
      and then bent into a ring.
  - keywords:
    - octahedron
    - polyhedron
    name: octahedronSdf
    summary: An octahedron, with its corners facing the axes.
  - name: petalSdf
    summary: A flower petal or leaf shape.
  - keywords:
    - floor
    - plane
    - sheet
    name: planeSdf
    summary: An infinite plane on the x, y, or z axis.
  - name: polyhedronSdf
    status: beta
  - keywords:
    - column
    - cylinder
    - hexagon
    - octagon
    - prism
    - square
    - triangle
    name: prismSdf
    summary: A prism shape, like a cylinder but with flat sides, along the z axis.
  - name: pyramidSdf
    summary: A pyramid with four sides.
  - keywords:
    - plane
    - quad
    - rectangle
    - square
    name: quadSdf
    status: beta
  - keywords:
    - line
    - path
    - points
    - segments
    name: segmentedLineSdf
    summary: Multi-segment line SDF.
  - keywords:
    - cone
    - pie
    - slice
    - wedge
    name: solidAngleSdf
    summary: A conical slice of a sphere.
  - name: sphereFbmSdf
  - name: sphereSdf
    shortcuts:
    - sph
    summary: SDF in 3D space for a uniform sphere.
  - keywords:
    - coil
    - spiral
    - swirl
    name: spiralSdf
    summary: A tapering spiral squared tube.
  - name: tetrahedronSdf
    summary: Tetrahedron shape.
  - keywords:
    - donut
    - ring
    - torus
    name: torusSdf
    summary: SDF for a torus.
  summary: 'Signed distances functions which define geometry in 3D space, by calculating

    the distance from the surface of the shape at any given point.'

---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.
