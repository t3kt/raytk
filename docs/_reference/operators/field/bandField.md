---
layout: operator
title: bandField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/bandField
redirect_from:
  - /reference/opType/raytk.operators.field.bandField/
op:
  category: field
  detail: 'For example, this can be used to have one color within Z = 0.3 to 0.5,
    and another color for all other coordinates.


    See also the `slice` operator, which behaves similarly for SDF results.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    summary: Optional float field that can be used as an alternative coordinate source
      (instead of using the `Axis` parameter).
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Inside Value Field
    name: insideValue
    returnTypes:
    - float
    - vec4
    summary: Optional field that is used to produce the values for the "inside" part.
      If used, the `Inside Value` parameter will be ignored.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Outside Value Field
    name: outsideValue
    returnTypes:
    - float
    - vec4
    summary: Optional field that is used to produce the values for the "outside" part.
      If used, the `Outside Value` parameter will be ignored.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    label: Blend Function
    name: blendFunction
    returnTypes:
    - float
    summary: Optional function used to control how `Blending` is applied.
  name: bandField
  opType: raytk.operators.field.bandField
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
  - label: Center
    name: Center
    summary: The center position along the axis of the "inside" part of the band.
  - label: Width
    name: Width
    summary: The width of the "inside" part of the band, along the axis.
  - label: Enable Blending
    name: Enableblending
    summary: Whether to smooth the transition between "inside" and "outside" vs a
      hard cutoff.
  - label: Blending
    name: Blending
    summary: 'The blending distance between "inside" and "outside". This applies to
      both borders of the "inside" area. '
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
    summary: Whether to produce a single float value or a vector with 4 parts.
  - label: Inside Value
    name: Insidevalue
    summary: The value used for the "inside" part. If `Return Type` is `Float`, only
      the first parameter will be used.
  - label: Outside Value
    name: Outsidevalue
    summary: The value used for the "outside" part. If `Return Type` is `Float`, only
      the first parameter will be used.
  - label: Enable Repeat
    name: Enablerepeat
  - label: Repeat Size
    name: Repeatsize
  - label: Repeat Shift
    name: Repeatshift
  summary: Field that applies values based on a band/slice of an axis.

---


Field that applies values based on a band/slice of an axis.

For example, this can be used to have one color within Z = 0.3 to 0.5, and another color for all other coordinates.

See also the `slice` operator, which behaves similarly for SDF results.