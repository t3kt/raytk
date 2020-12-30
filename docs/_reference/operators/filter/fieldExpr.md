---
layout: operator
title: fieldExpr
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/fieldExpr
redirect_from:
  - /reference/opType/raytk.operators.filter.fieldExpr/
op:
  name: fieldExpr
  opType: raytk.operators.filter.fieldExpr
  category: filter
  inputs:
    - name: definition_in
      label: definition_in
      required: false
    - name: definition_in1
      label: definition_in1
      required: false
    - name: definition_in2
      label: definition_in2
      required: false
    - name: definition_in3
      label: definition_in3
      required: false
  parameters:
    - name: Enable
      label: Enable
    - name: Expression
      label: Expression
      menuOptions:
        - name: sqrt(inputOp1(p, ctx))
          label: sqrt(x)         Square Root
        - name: sqrt(inputOp1(p, ctx))
          label: abs(x)         Absolute Value
        - name: sign(inputOp1(p, ctx))
          label: sign(x)         Sign
        - name: cos(inputOp1(p, ctx))
          label: cos(x)         Cosine
        - name: sin(inputOp1(p, ctx))
          label: sin(x)          Sine
        - name: tan(inputOp1(p, ctx))
          label: tan(x)         Tangent
        - name: acos(inputOp1(p, ctx))
          label: acos(x)       Arccosine
        - name: asin(inputOp1(p, ctx))
          label: asin(x)        Arcsine
        - name: atan(inputOp1(p, ctx))
          label: atan(x)        Arctan ( Input1 )
        - name: atan2(inputOp1(p, ctx), inputOp2(p, ctx))
          label: atan2(x,y)   Arctan ( Input1 / Input2 )
        - name: cosh(inputOp1(p, ctx))
          label: cosh(x)       Hyperbolic Cosine
        - name: sinh(inputOp1(p, ctx))
          label: sinh(x)        Hyperbolic Sine
        - name: tanh(inputOp1(p, ctx))
          label: tanh(x)        Hyperbolic Tangent
        - name: log2(inputOp1(p, ctx))
          label: log2(x)         Log Base 2
        - name: log(inputOp1(p, ctx))
          label: log(x)            Natural Log
        - name: exp(inputOp1(p, ctx))
          label: exp(x)          e ^ Input1
        - name: exp2(inputOp1(p, ctx))
          label: exp2(x)        2 ^ Input1
        - name: pow(THIS_Param1, inputOp1(p, ctx))
          label: pow(x)         Base ^ Input1
        - name: pow(inputOp1(p, ctx), inputOp2(p, ctx))
          label: pow(x,y)      Input1 ^ Input2
    - name: Param1
      label: Param 1
    - name: Param2
      label: Param 2
    - name: Vecparam1
      label: Vector Param 1
    - name: Vecparam2
      label: Vector Param 2
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: float
          label: 1D
        - name: vec3
          label: 3D
        - name: vec2
          label: 2D
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: Sdf
          label: SDF Result
        - name: float
          label: Float
        - name: vec4
          label: Vector4
        - name: Ray
          label: Ray
        - name: Light
          label: Light
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
        - name: RayContext
          label: Ray Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# fieldExpr

Category: filter

