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
  - name: amazingSurfaceSdf
  - name: apollonianSdf
  - name: archSdf
    status: beta
  - name: boxFrameSdf
    summary: SDF for the squared frame of the edges of a box.
  - name: boxSdf
    summary: SDF for a box, optionally infinite one one axis.
  - name: bunnySdf
    summary: SDF for a bunny.
  - name: capsuleSdf
    summary: A cylinder with rounded ends, between two points.
  - name: chainSdf
    status: beta
  - name: chamferBoxSdf
  - name: coneSdf
    summary: Defines a cone or capped cone shape.
  - name: crossSdf
    summary: An SDF for a 3D cross of infinite length along each axis.
  - name: cylinderSdf
    summary: SDF for a cylinder.
  - name: discSdf
    summary: A flat disc facing the Y axis.
  - name: dodecahedronFractalSdf
    status: beta
  - name: ellipsoidSdf
  - name: generalizedPolyhedronSdf
    summary: Generates one of several different types of polyhedra.
  - name: geodesicSdf
    summary: A geodesic polyhedron, optionally with a spike on each face.
  - name: gridSdf
    summary: An infinite grid shape, along two axes.
  - name: gyroidSdf
    status: beta
    summary: Gyroid shape, which is an infinitely connected periodic surface.
  - name: helixSdf
    summary: '## Parameters'
  - name: juliaSdf
    status: beta
  - name: kaliGeneratorSdf
    summary: Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
  - name: linkSdf
    summary: SDF for a chain link shape (an elongated loop).
  - name: mandelbulbSdf
    summary: Mandelbulb fractal.
  - name: mengerSpongeSdf
    summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  - name: mobiusRingSdf
    summary: SDF for a squared mobius ring, which is like a rectangular bar twisted
      and then bent into a ring.
  - name: octahedronSdf
    summary: An octahedron, with its corners facing the axes.
  - name: petalSdf
    summary: A flower petal or leaf shape.
  - name: planeSdf
    summary: An infinite plane on the x, y, or z axis.
  - name: prismSdf
    summary: A prism shape, like a cylinder but with flat sides, along the z axis.
  - name: pyramidSdf
    summary: A pyramid with four sides.
  - name: quadSdf
    status: beta
  - name: segmentedLineSdf
  - name: solidAngleSdf
    summary: A conical slice of a sphere.
  - name: sphereFbmSdf
  - name: sphereSdf
    summary: SDF in 3D space for a uniform sphere.
  - name: spiralSdf
    summary: A tapering spiral squared tube.
  - name: tetrahedronSdf
    summary: Tetrahedron shape.
  - name: torusSdf
    summary: SDF for a torus.
  summary: 'Signed distances functions which define geometry in 3D space, by calculating

    the distance from the surface of the shape at any given point.'

---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.
