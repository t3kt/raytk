---
layout: operator
title: fieldFunction
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/fieldFunction
redirect_from:
  - /reference/opType/raytk.operators.filter.fieldFunction/
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
    label: Value 1 Field
    name: definition_in_1
    returnTypes:
    - float
    - vec4
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
    label: Value 2 Field
    name: definition_in_2
    returnTypes:
    - float
    - vec4
  name: fieldFunction
  opType: raytk.operators.filter.fieldFunction
  parameters:
  - label: Enable
    name: Enable
  - label: Function
    menuOptions:
    - label: abs(x)            Absolute Value
      name: abs
    - label: ceil(x)           Ceiling (Round Up)
      name: ceil
    - label: floor(x)          Floor (Round Down)
      name: floor
    - label: sign(x)           Sign
      name: sign
    - label: e^x               Natural Exponentiation
      name: exp
    - label: 2^x               2 To The Power Of
      name: exp2
    - label: fract(x)          Fractional Part
      name: fract
    - label: mod(x,y)         Modulo
      name: mod
    - label: inversesqrt(x)    Inverse Square Root
      name: inversesqrt
    - label: pow(x,y)         To The Power Of
      name: pow
    - label: round(x)          Round
      name: round
    - label: roundEven(x)      Round To Even Integer
      name: roundEven
    - label: sqrt(x)           Square Root
      name: sqrt
    - label: trunc(x)          Truncate (Integer <=)
      name: trunc
    - label: cos(x)            Cosine
      name: cos
    - label: sin(x)            Sine
      name: sin
    - label: tan(x)            Tangent
      name: tan
    - label: acos(x)           Arccosine
      name: acos
    - label: asin(x)           Arcsine
      name: asin
    - label: atan(x)           Arctan( Input1 )
      name: atan
    - label: atan(x,y)        Arctan( Input1 )
      name: atan2
    - label: cosh(x)           Hyperbolic Cosine
      name: cosh
    - label: sinh(x)           Hyperbolic Sine
      name: sinh
    - label: tanh(x)           Hyperbolic Tangent
      name: tanh
    - label: log2(x)           Log Base 2
      name: log2
    - label: log(x)            Natural Log
      name: log
    - label: degrees(x)        Radians to Degrees
      name: degrees
    - label: radians(x)        Degrees to Radians
      name: radians
    name: Function
  - label: Value 1
    name: Value1
  - label: Value 2
    name: Value2
  status: beta

---
