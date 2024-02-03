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
    summary: Optional float field that can be used as an alternative coordinate source
      (instead of using the `Axis` parameter).
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
    label: Inside Value Field
    name: insideValue
    returnTypes:
    - float
    - vec4
    summary: Optional field that is used to produce the values for the "inside" part.
      If used, the `Inside Value` parameter will be ignored.
    supportedVariableInputs:
    - coordField
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
    label: Outside Value Field
    name: outsideValue
    returnTypes:
    - float
    - vec4
    summary: Optional field that is used to produce the values for the "outside" part.
      If used, the `Outside Value` parameter will be ignored.
    supportedVariableInputs:
    - coordField
    - insideValue
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
    summary: Optional function used to control how `Blending` is applied.
    supportedVariableInputs:
    - coordField
    - insideValue
    - outsideValue
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
    label: Width Field
    name: widthField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - insideValue
    - outsideValue
    - centerField
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
    label: Blend Amount Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - insideValue
    - outsideValue
    - centerField
    - widthField
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
    label: Blend Function
    name: blendFunction
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - insideValue
    - outsideValue
    - centerField
    - widthField
    - blendingField
  name: bandField
  opType: raytk.operators.field.bandField
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
    readOnlyHandling: constant
    regularHandling: constant
  - label: Center
    name: Center
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The center position along the axis of the "inside" part of the band.
  - label: Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The width of the "inside" part of the band, along the axis.
  - label: Enable Blending
    name: Enableblending
    readOnlyHandling: constant
    regularHandling: constant
    summary: Whether to smooth the transition between "inside" and "outside" vs a
      hard cutoff.
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
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
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The value used for the "inside" part. If `Return Type` is `Float`, only
      the first parameter will be used.
  - label: Outside Value
    name: Outsidevalue
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The value used for the "outside" part. If `Return Type` is `Float`, only
      the first parameter will be used.
  - label: Enable
    name: Enable
  - label: Reverse
    name: Reverse
    readOnlyHandling: constant
    regularHandling: constant
  - label: Enable Repeat
    name: Enablerepeat
    readOnlyHandling: constant
    regularHandling: constant
  - label: Repeat Size
    name: Repeatsize
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Repeat Shift
    name: Repeatshift
    readOnlyHandling: macro
    regularHandling: runtime
  summary: Field that applies values based on a band/slice of an axis.
  thumb: assets/images/reference/operators/field/bandField_thumb.png

---


Field that applies values based on a band/slice of an axis.

For example, this can be used to have one color within Z = 0.3 to 0.5, and another color for all other coordinates.

See also the `slice` operator, which behaves similarly for SDF results.