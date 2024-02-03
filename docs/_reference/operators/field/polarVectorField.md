---
layout: operator
title: polarVectorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/polarVectorField
redirect_from:
  - /reference/opType/raytk.operators.field.polarVectorField/
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
    - vec2
    - vec3
    label: Theta Field
    name: thetaField
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
    - vec3
    label: Phi Field
    name: phiField
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
    - vec3
    label: Length Field
    name: lengthField
    returnTypes:
    - float
  name: polarVectorField
  opType: raytk.operators.field.polarVectorField
  parameters:
  - label: Theta Offset
    name: Thetaoffset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Phi Offset
    name: Phioffset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Length
    name: Length
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/field/polarVectorField_thumb.png

---
