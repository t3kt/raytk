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
    thumb: assets/images/reference/operators/sdf/amazingSurfaceSdf_thumb.png
  - keywords:
    - fractal
    name: apollonianSdf
    summary: Apollonian gasket fractal.
    thumb: assets/images/reference/operators/sdf/apollonianSdf_thumb.png
  - name: archSdf
    summary: Arch / doorway.
    thumb: assets/images/reference/operators/sdf/archSdf_thumb.png
  - keywords:
    - bezier
    - curve
    - line
    name: bezierSdf
    thumb: assets/images/reference/operators/sdf/bezierSdf_thumb.png
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
    thumb: assets/images/reference/operators/sdf/boxFrameSdf_thumb.png
  - keywords:
    - box
    - cube
    - rectangle
    - square
    name: boxSdf
    shortcuts:
    - box
    summary: SDF for a box, optionally infinite one one axis.
    thumb: assets/images/reference/operators/sdf/boxSdf_thumb.png
  - name: bunnySdf
    summary: SDF for a bunny.
    thumb: assets/images/reference/operators/sdf/bunnySdf_thumb.png
  - keywords:
    - capsule
    - line
    - points
    - segment
    name: capsuleSdf
    summary: A line or cylinder with rounded ends, between two points.
    thumb: assets/images/reference/operators/sdf/capsuleSdf_thumb.png
  - name: chainSdf
    summary: Chain made of links, with infinite length.
    thumb: assets/images/reference/operators/sdf/chainSdf_thumb.png
  - keywords:
    - box
    - chamfer
    - cube
    name: chamferBoxSdf
    summary: A box with cropped corners at 45 degree angles.
    thumb: assets/images/reference/operators/sdf/chamferBoxSdf_thumb.png
  - name: coneSdf
    summary: Defines a cone or capped cone shape.
    thumb: assets/images/reference/operators/sdf/coneSdf_thumb.png
  - name: crescentSdf
    summary: Rounded crescent shape.
    thumb: assets/images/reference/operators/sdf/crescentSdf_thumb.png
  - name: crossSdf
    summary: An SDF for a 3D cross along each axis, with either infinite or limited
      length.
    thumb: assets/images/reference/operators/sdf/crossSdf_thumb.png
  - name: cutSphereSdf
    summary: Sphere with part of it cut off, either solid or hollow.
    thumb: assets/images/reference/operators/sdf/cutSphereSdf_thumb.png
  - keywords:
    - column
    - cylinder
    - pipe
    name: cylinderSdf
    summary: Cylinder, either solid or a hollow tube.
    thumb: assets/images/reference/operators/sdf/cylinderSdf_thumb.png
  - name: discSdf
    summary: A flat disc facing the Y axis.
    thumb: assets/images/reference/operators/sdf/discSdf_thumb.png
  - name: dodecahedronFractalSdf
    thumb: assets/images/reference/operators/sdf/dodecahedronFractalSdf_thumb.png
  - keywords:
    - circle
    - ellipse
    - ellipsoid
    - oval
    - sphere
    name: ellipsoidSdf
    summary: Ellipsoid (sphere with different sizes on each axis).
    thumb: assets/images/reference/operators/sdf/ellipsoidSdf_thumb.png
  - keywords:
    - dodecahedron
    - icosahedron
    - octahedron
    - polyhedron
    name: generalizedPolyhedronSdf
    summary: Generates one of several different types of polyhedra.
    thumb: assets/images/reference/operators/sdf/generalizedPolyhedronSdf_thumb.png
  - keywords:
    - geodesic
    - polyhedron
    - spikes
    name: geodesicSdf
    summary: A geodesic polyhedron, optionally with a spike on each face.
    thumb: assets/images/reference/operators/sdf/geodesicSdf_thumb.png
  - keywords:
    - bars
    - grid
    name: gridSdf
    summary: An infinite grid shape, along two axes.
    thumb: assets/images/reference/operators/sdf/gridSdf_thumb.png
  - keywords:
    - gyroid
    - sine
    - wave
    name: gyroidSdf
    summary: Gyroid shape, which is an infinitely connected periodic surface.
    thumb: assets/images/reference/operators/sdf/gyroidSdf_thumb.png
  - name: headSdf
    summary: Human head SDF created by tdhooper.
    thumb: assets/images/reference/operators/sdf/headSdf_thumb.png
  - keywords:
    - coil
    - helix
    - spiral
    name: helixSdf
    summary: SDF for a helix (an elongated spiral).
    thumb: assets/images/reference/operators/sdf/helixSdf_thumb.png
  - name: hyperbolicParaboloidSdf
    thumb: assets/images/reference/operators/sdf/hyperbolicParaboloidSdf_thumb.png
  - name: jointSdf
    thumb: assets/images/reference/operators/sdf/jointSdf_thumb.png
  - keywords:
    - fractal
    - julia
    - quaternion
    name: juliaSdf
    thumb: assets/images/reference/operators/sdf/juliaSdf_thumb.png
  - name: kaliGeneratorSdf
    summary: Fractal SDF based on "Generators" by Kali (https://www.shadertoy.com/view/Xtf3Rn).
    thumb: assets/images/reference/operators/sdf/kaliGeneratorSdf_thumb.png
  - keywords:
    - fractal
    name: kleinianSdf
    status: beta
    thumb: assets/images/reference/operators/sdf/kleinianSdf_thumb.png
  - keywords:
    - grid
    name: latticeSdf
    thumb: assets/images/reference/operators/sdf/latticeSdf_thumb.png
  - name: lineSeriesSdf
    thumb: assets/images/reference/operators/sdf/lineSeriesSdf_thumb.png
  - keywords:
    - chain
    - link
    name: linkSdf
    summary: SDF for a chain link shape (an elongated loop).
    thumb: assets/images/reference/operators/sdf/linkSdf_thumb.png
  - keywords:
    - fractal
    - mandelbrot
    - mandelbulb
    name: mandelbulbSdf
    summary: Mandelbulb fractal.
    thumb: assets/images/reference/operators/sdf/mandelbulbSdf_thumb.png
  - keywords:
    - fractal
    name: mandelettuceSdf
    status: beta
    thumb: assets/images/reference/operators/sdf/mandelettuceSdf_thumb.png
  - keywords:
    - fractal
    name: mengerSpongeSdf
    summary: Menger sponge fractal, made of boxes with holes cut through each axis.
    thumb: assets/images/reference/operators/sdf/mengerSpongeSdf_thumb.png
  - keywords:
    - mobius
    - ring
    - twist
    name: mobiusRingSdf
    summary: SDF for a squared mobius ring, which is like a rectangular bar twisted
      and then bent into a ring.
    thumb: assets/images/reference/operators/sdf/mobiusRingSdf_thumb.png
  - keywords:
    - octahedron
    - polyhedron
    name: octahedronSdf
    summary: An octahedron, with its corners facing the axes.
    thumb: assets/images/reference/operators/sdf/octahedronSdf_thumb.png
  - name: petalSdf
    summary: A flower petal or leaf shape.
    thumb: assets/images/reference/operators/sdf/petalSdf_thumb.png
  - name: pistonSdf
    thumb: assets/images/reference/operators/sdf/pistonSdf_thumb.png
  - keywords:
    - floor
    - plane
    - sheet
    name: planeSdf
    summary: An infinite plane on the x, y, or z axis.
    thumb: assets/images/reference/operators/sdf/planeSdf_thumb.png
  - name: polyhedronSdf
    thumb: assets/images/reference/operators/sdf/polyhedronSdf_thumb.png
  - name: polytopeSdf
    status: beta
    summary: 4D polytope SDF.
    thumb: assets/images/reference/operators/sdf/polytopeSdf_thumb.png
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
    thumb: assets/images/reference/operators/sdf/prismSdf_thumb.png
  - name: pyramidSdf
    summary: A pyramid with four sides.
    thumb: assets/images/reference/operators/sdf/pyramidSdf_thumb.png
  - keywords:
    - plane
    - quad
    - rectangle
    - square
    name: quadSdf
    thumb: assets/images/reference/operators/sdf/quadSdf_thumb.png
  - name: ringsSdf
  - keywords:
    - line
    - path
    - points
    - segments
    name: segmentedLineSdf
    summary: Multi-segment line SDF.
    thumb: assets/images/reference/operators/sdf/segmentedLineSdf_thumb.png
  - keywords:
    - fractal
    name: sierpinskiIcosahedronSdf
    status: beta
    summary: Sierpinski Icosahedron Fractal SDF
    thumb: assets/images/reference/operators/sdf/sierpinskiIcosahedronSdf_thumb.png
  - keywords:
    - fractal
    name: sierpinskiOctahedralSpongeSdf
    status: beta
    summary: Sierpinski Octahedral Sponge Fractal SDF
    thumb: assets/images/reference/operators/sdf/sierpinskiOctahedralSpongeSdf_thumb.png
  - keywords:
    - cone
    - pie
    - slice
    - wedge
    name: solidAngleSdf
    summary: A conical slice of a sphere.
    thumb: assets/images/reference/operators/sdf/solidAngleSdf_thumb.png
  - name: sphereFbmSdf
    thumb: assets/images/reference/operators/sdf/sphereFbmSdf_thumb.png
  - name: sphereGridSdf
    status: beta
    thumb: assets/images/reference/operators/sdf/sphereGridSdf_thumb.png
  - name: sphereSdf
    shortcuts:
    - sph
    summary: SDF in 3D space for a uniform sphere.
    thumb: assets/images/reference/operators/sdf/sphereSdf_thumb.png
  - keywords:
    - coil
    - spiral
    - swirl
    name: spiralSdf
    summary: A tapering spiral squared tube.
    thumb: assets/images/reference/operators/sdf/spiralSdf_thumb.png
  - name: springSdf
    summary: A coiled spring shape.
    thumb: assets/images/reference/operators/sdf/springSdf_thumb.png
  - name: stackSdf
    status: beta
  - name: tetrahedronSdf
    summary: Tetrahedron shape.
    thumb: assets/images/reference/operators/sdf/tetrahedronSdf_thumb.png
  - name: torusGridSdf
    status: beta
    thumb: assets/images/reference/operators/sdf/torusGridSdf_thumb.png
  - keywords:
    - donut
    - ring
    - torus
    name: torusSdf
    summary: SDF for a torus.
    thumb: assets/images/reference/operators/sdf/torusSdf_thumb.png
  - name: trefoilKnotSdf
    status: beta
    summary: Trefoil knot SDF.
    thumb: assets/images/reference/operators/sdf/trefoilKnotSdf_thumb.png
  - name: truncatedPyramidSdf
    thumb: assets/images/reference/operators/sdf/truncatedPyramidSdf_thumb.png
  - name: vesicaSegmentSdf
    thumb: assets/images/reference/operators/sdf/vesicaSegmentSdf_thumb.png
  - moduleName: raytkAbstractions
    name: twistedRingsSdf
    status: beta
  summary: 'Signed distances functions which define geometry in 3D space, by calculating

    the distance from the surface of the shape at any given point.'

---

# Sdf Operators

Signed distances functions which define geometry in 3D space, by calculating
the distance from the surface of the shape at any given point.

These operators are how geometry is defined for raymarching, and they are
often the first operator in a chain that ends with a `raymarchRender3d`.
