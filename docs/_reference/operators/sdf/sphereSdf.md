---
layout: operator
title: sphereSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/sphereSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.sphereSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  name: sphereSdf
  opType: raytk.operators.sdf.sphereSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the sphere.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the sphere.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    - label: Spherical Polar
      name: sphericalpolar
    - label: Sphere
      name: sphere
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  shortcuts:
  - sph
  summary: SDF in 3D space for a uniform sphere.
  thumb: assets/images/reference/operators/sdf/sphereSdf_thumb.png

---


SDF in 3D space for a uniform sphere.