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
  - keywords:
    - bezier
    - curve
    - line
    name: bezierSdf
  - keywords:
    - box
    - cube
    - frame
    - rectangle
    - square
    name: boxFrameSdf
    shortcuts:
    - bfs
  - keywords:
    - box
    - cube
    - rectangle
    - square
    name: boxSdf
    shortcuts:
    - box
  - name: bunnySdf
  - keywords:
    - capsule
    - line
    - points
    - segment
    name: capsuleSdf
  - name: chainSdf
  - keywords:
    - box
    - chamfer
    - cube
    name: chamferBoxSdf
  - name: coneSdf
  - name: crescentSdf
  - name: crossSdf
  - name: cutSphereSdf
  - keywords:
    - column
    - cylinder
    - pipe
    name: cylinderSdf
  - name: discSdf
  - name: dodecahedronFractalSdf
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
  - keywords:
    - geodesic
    - polyhedron
    - spikes
    name: geodesicSdf
  - keywords:
    - bars
    - grid
    name: gridSdf
  - keywords:
    - gyroid
    - sine
    - wave
    name: gyroidSdf
  - name: headSdf
  - keywords:
    - coil
    - helix
    - spiral
    name: helixSdf
  - name: hyperbolicParaboloidSdf
  - name: jointSdf
  - keywords:
    - fractal
    - julia
    - quaternion
    name: juliaSdf
  - name: kaliGeneratorSdf
  - keywords:
    - grid
    name: latticeSdf
  - name: lineSeriesSdf
  - keywords:
    - chain
    - link
    name: linkSdf
  - keywords:
    - fractal
    - mandelbrot
    - mandelbulb
    name: mandelbulbSdf
  - name: mengerSpongeSdf
  - keywords:
    - mobius
    - ring
    - twist
    name: mobiusRingSdf
  - keywords:
    - octahedron
    - polyhedron
    name: octahedronSdf
  - name: petalSdf
  - name: pistonSdf
  - keywords:
    - floor
    - plane
    - sheet
    name: planeSdf
  - name: polyhedronSdf
  - keywords:
    - column
    - cylinder
    - hexagon
    - octagon
    - prism
    - square
    - triangle
    name: prismSdf
  - name: pyramidSdf
  - keywords:
    - plane
    - quad
    - rectangle
    - square
    name: quadSdf
  - name: ringsSdf
  - keywords:
    - line
    - path
    - points
    - segments
    name: segmentedLineSdf
  - keywords:
    - cone
    - pie
    - slice
    - wedge
    name: solidAngleSdf
  - name: sphereFbmSdf
  - name: sphereGridSdf
    status: beta
  - name: sphereSdf
    shortcuts:
    - sph
  - keywords:
    - coil
    - spiral
    - swirl
    name: spiralSdf
  - name: springSdf
  - name: stackSdf
    status: beta
  - name: tetrahedronSdf
  - name: torusGridSdf
    status: beta
  - keywords:
    - donut
    - ring
    - torus
    name: torusSdf
  - name: truncatedPyramidSdf
  - name: vesicaSegmentSdf
  summary: 'Signed distances functions which define geometry in 3D space, by calculating

    the distance from the surface of the shape at any given point.'

---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.
