---
layout: operator
title: polygonSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/polygonSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.polygonSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
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
    - vec2
    label: Sides Field
    name: sidesField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  name: polygonSdf2d
  opType: raytk.operators.sdf2d.polygonSdf2d
  parameters:
  - label: Shape
    menuOptions:
    - label: Pentagon
      name: pentagon
    - label: Hexagon
      name: hexagon
    - label: Octogon
      name: octogon
    - label: Custom
      name: custom
    name: Shape
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The distance from the center to each edge.
  - label: Sides
    name: Sides
    readOnlyHandling: baked
    regularHandling: runtime
  summary: SDF for several types of 2D polygons.
  thumb: assets/images/reference/operators/sdf2d/polygonSdf2d_thumb.png

---


SDF for several types of 2D polygons.