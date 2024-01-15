---
layout: operator
title: onion
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/onion
redirect_from:
  - /reference/opType/raytk.operators.filter.onion/
op:
  category: filter
  detail: 'The shell is created centered on the surface, with half of the `Thickness`
    going toward the outside and the other half on the inside. This has the effect
    of increasing the size of the outside of the shape.


    Without somehow slicing through the shell, using things like `knife` or `slice`,
    you generally won''t be able to tell the difference between this and `round`,
    in that it will seem to just increase the size of the shape.


    See https://www.shadertoy.com/view/MlcBDj'
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
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
    label: Thickness Field
    name: thicknessField
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
    label: Iterations Field
    name: iterationsField
    returnTypes:
    - float
  keywords:
  - hollow
  - onion
  - shell
  name: onion
  opType: raytk.operators.filter.onion
  parameters:
  - label: Enable
    name: Enable
  - label: Thickness
    name: Thickness
    summary: Thickness of the shell, centered on the input surface.
  - label: Iterations
    name: Iterations
  - label: Side
    menuOptions:
    - label: Both
      name: both
    - label: Inside
      name: inside
    - label: Outside
      name: outside
    name: Side
  summary: Converts a solid SDF to a thin shell of the surface.
  thumb: assets/images/reference/operators/filter/onion_thumb.png

---


Converts a solid SDF to a thin shell of the surface.

The shell is created centered on the surface, with half of the `Thickness` going toward the outside and the other half on the inside. This has the effect of increasing the size of the outside of the shape.

Without somehow slicing through the shell, using things like `knife` or `slice`, you generally won't be able to tell the difference between this and `round`, in that it will seem to just increase the size of the shape.

See https://www.shadertoy.com/view/MlcBDj