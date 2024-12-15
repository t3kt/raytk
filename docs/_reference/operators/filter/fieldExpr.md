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
  detail: "The Expression parameter's menu contains common examples.\n\nWriting expressions:\n\
    \n* To access a value from input 1, use a function call like `inputOp1(p, ctx)`\n\
    \  * The `p` part is the spatial coordinate, so you can modify it with something\
    \ like `inputOp1(p + vec3(1, 0, 0), ctx)`, which would move that field to the\
    \ left.\n  * The `ctx` part is required as the second argument to the function.\n\
    * Other inputs are available as `inputOp2(...)` etc\n* The two slider parameters\
    \ are available as `THIS_Param1` and `THIS_Param2`\n* The two vector parameters\
    \ are available as `THIS_Vecparam1` and `THIS_Vecparam2`\n  * To get at an individual\
    \ part of one of the vector params, you can use `THIS_Vecparam1.y`"
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input Field 1
    name: definition_in_1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input Field 2
    name: definition_in_2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input Field 3
    name: definition_in_3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Input Field 4
    name: definition_in_4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
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
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Param 2
    name: Param2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Vector Param 1
    name: Vecparam1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Vector Param 2
    name: Vecparam2
    readOnlyHandling: baked
    regularHandling: runtime
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
  summary: Modifies field values using a custom expression.

---


Modifies field values using a custom expression.

The Expression parameter's menu contains common examples.

Writing expressions:

* To access a value from input 1, use a function call like `inputOp1(p, ctx)`
  * The `p` part is the spatial coordinate, so you can modify it with something like `inputOp1(p + vec3(1, 0, 0), ctx)`, which would move that field to the left.
  * The `ctx` part is required as the second argument to the function.
* Other inputs are available as `inputOp2(...)` etc
* The two slider parameters are available as `THIS_Param1` and `THIS_Param2`
* The two vector parameters are available as `THIS_Vecparam1` and `THIS_Vecparam2`
  * To get at an individual part of one of the vector params, you can use `THIS_Vecparam1.y`