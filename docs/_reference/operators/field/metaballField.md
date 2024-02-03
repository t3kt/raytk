---
layout: operator
title: metaballField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/metaballField
redirect_from:
  - /reference/opType/raytk.operators.field.metaballField/
op:
  category: field
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
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
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
    - float
    - vec2
    - vec3
    - vec4
    label: Center Field
    name: centerField
    returnTypes:
    - float
    - vec4
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
    - float
    - vec2
    - vec3
    - vec4
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    - vec4
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
    - float
    - vec2
    - vec3
    - vec4
    label: Weight Field
    name: weightField
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
    - float
    - vec2
    - vec3
    - vec4
    label: Exponent Field
    name: exponentField
    returnTypes:
    - float
    - vec4
  name: metaballField
  opType: raytk.operators.field.metaballField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Center position of the ball.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Radius of the ball on each axis. In 2D mode, only x and y are used. In
      1D only x is used.
  - label: Radius Scale
    name: Radiusscale
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Scales the radius on all axes.
  - label: Weight
    name: Weight
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The returned values are multiplied by this.
  - label: Exponent
    name: Exponent
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Controls the shape of the ball by applying exponential scaling to coordinates.
  summary: Metaball value field.
  thumb: assets/images/reference/operators/field/metaballField_thumb.png

---


Metaball value field.