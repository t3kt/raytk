---
layout: operator
title: vesicaSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/vesicaSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.vesicaSdf2d/
op:
  category: sdf2d
  detail: 'See [Wikipedia](https://en.wikipedia.org/wiki/Vesica_piscis) for details.

    See [ShaderToy](https://www.shadertoy.com/view/XtVfRW) for an example.'
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
    label: Distance Field
    name: distanceField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  name: vesicaSdf2d
  opType: raytk.operators.sdf2d.vesicaSdf2d
  parameters:
  - label: Radius
    name: Radius
    summary: The radius of each circle.
  - label: Distance
    name: Distance
    summary: The distance between the circles. Higher values will produce thinner
      shapes since the circles will overlap less. Lower values will produce rounder
      shapes, eventually reaching a full circle when the distance is 0.
  summary: SDF for a 2d vesica, which is a shape based on the overlap between two
    circles.
  thumb: assets/images/reference/operators/sdf2d/vesicaSdf2d_thumb.png

---


SDF for a 2d vesica, which is a shape based on the overlap between two circles.

See [Wikipedia](https://en.wikipedia.org/wiki/Vesica_piscis) for details.
See [ShaderToy](https://www.shadertoy.com/view/XtVfRW) for an example.