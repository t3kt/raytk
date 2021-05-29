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
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: coord_field_definition_in
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
    coordTypes:
    - float
    - vec2
    - vec3
    label: Inside Value Field
    name: inside_value_definition_in
    returnTypes:
    - vec4
    summary: Optional field that is used to produce the values for the "inside" part.
      If used, the `Inside Value` parameter will be ignored.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Outside Value Field
    name: outside_value_definition_in
    returnTypes:
    - vec4
    summary: Optional field that is used to produce the values for the "outside" part.
      If used, the `Outside Value` parameter will be ignored.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Blend Function
    name: blend_function_definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
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
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: Field that applies values based on a band/slice of an axis.

---


Field that applies values based on a band/slice of an axis.

For example, this can be used to have one color within Z = 0.3 to 0.5, and another color for all other coordinates.

See also the `slice` operator, which behaves similarly for SDF results.