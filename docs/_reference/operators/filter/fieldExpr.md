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
    - none
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
    - none
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
    - none
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
    - none
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
      name: sqrt(inputOp1(p, ctx))
    - label: abs(x)         Absolute Value
      name: sqrt(inputOp1(p, ctx))
    - label: sign(x)         Sign
      name: sign(inputOp1(p, ctx))
    - label: cos(x)         Cosine
      name: cos(inputOp1(p, ctx))
    - label: sin(x)          Sine
      name: sin(inputOp1(p, ctx))
    - label: tan(x)         Tangent
      name: tan(inputOp1(p, ctx))
    - label: acos(x)       Arccosine
      name: acos(inputOp1(p, ctx))
    - label: asin(x)        Arcsine
      name: asin(inputOp1(p, ctx))
    - label: atan(x)        Arctan ( Input1 )
      name: atan(inputOp1(p, ctx))
    - label: atan2(x,y)   Arctan ( Input1 / Input2 )
      name: atan2(inputOp1(p, ctx), inputOp2(p, ctx))
    - label: cosh(x)       Hyperbolic Cosine
      name: cosh(inputOp1(p, ctx))
    - label: sinh(x)        Hyperbolic Sine
      name: sinh(inputOp1(p, ctx))
    - label: tanh(x)        Hyperbolic Tangent
      name: tanh(inputOp1(p, ctx))
    - label: log2(x)         Log Base 2
      name: log2(inputOp1(p, ctx))
    - label: log(x)            Natural Log
      name: log(inputOp1(p, ctx))
    - label: exp(x)          e ^ Input1
      name: exp(inputOp1(p, ctx))
    - label: exp2(x)        2 ^ Input1
      name: exp2(inputOp1(p, ctx))
    - label: pow(x)         Base ^ Input1
      name: pow(THIS_Param1, inputOp1(p, ctx))
    - label: pow(x,y)      Input1 ^ Input2
      name: pow(inputOp1(p, ctx), inputOp2(p, ctx))
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
    - label: 1D
      name: float
    - label: 3D
      name: vec3
    - label: 2D
      name: vec2
    name: Coordtype
  - label: Return Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: SDF Result
      name: Sdf
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
  - label: Context Type
    menuOptions:
    - label: Use Input
      name: useinput
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    - label: Ray Context
      name: RayContext
    name: Contexttype

---
