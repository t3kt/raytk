---
layout: operator
title: fieldExpr
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/fieldExpr
redirect_from:
  - /reference/opType/raytk.operators.filter.fieldExpr/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
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
    label: definition_in1
    name: definition_in1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
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
    label: definition_in2
    name: definition_in2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
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
    label: definition_in3
    name: definition_in3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: fieldExpr
  opType: raytk.operators.filter.fieldExpr
  parameters:
  - label: Enable
    name: Enable
  - label: Expression
    menuOptions:
    - label: sqrt(x)         Square Root
      name: sqrt
    - label: abs(x)         Absolute Value
      name: abs
    - label: sign(x)         Sign
      name: sign
    - label: cos(x)         Cosine
      name: cos
    - label: sin(x)          Sine
      name: sin
    - label: tan(x)         Tangent
      name: tan
    - label: acos(x)       Arccosine
      name: acos
    - label: asin(x)        Arcsine
      name: asin
    - label: atan(x)        Arctan ( Input1 )
      name: atan
    - label: atan2(x,y)   Arctan ( Input1 / Input2 )
      name: atan2
    - label: cosh(x)       Hyperbolic Cosine
      name: cosh
    - label: sinh(x)        Hyperbolic Sine
      name: sinh
    - label: tanh(x)        Hyperbolic Tangent
      name: tanh
    - label: log2(x)         Log Base 2
      name: log2
    - label: log(x)            Natural Log
      name: ln
    - label: exp(x)          e ^ Input1
      name: exp
    - label: exp2(x)        2 ^ Input1
      name: exp2
    - label: pow(x)         Base ^ Input1
      name: powb
    - label: pow(x,y)      Input1 ^ Input2
      name: powxy
    name: Expression
  - label: Param 1
    name: Param1
  - label: Param 2
    name: Param2
  - label: Vector Param 1
    name: Vecparam1
  - label: Vector Param 2
    name: Vecparam2
  - label: Coord Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: float
      name: float
    - label: vec2
      name: vec2
    - label: vec3
      name: vec3
    name: Coordtype
  - label: Return Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: Sdf
      name: Sdf
    - label: vec4
      name: vec4
    - label: float
      name: float
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
  - label: Context Type
    menuOptions:
    - label: Use Input
      name: useinput
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
  status: beta

---
