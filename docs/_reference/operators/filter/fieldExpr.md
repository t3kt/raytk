---
layout: page
title: fieldExpr
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/fieldExpr
---

# fieldExpr

Category: filter



## Parameters

* `Enable` *Enable*
* `Expression` *Expression*
  * `sqrt(inputOp1(p, ctx))` *sqrt(x)         Square Root*
  * `sqrt(inputOp1(p, ctx))` *abs(x)         Absolute Value*
  * `sign(inputOp1(p, ctx))` *sign(x)         Sign*
  * `cos(inputOp1(p, ctx))` *cos(x)         Cosine*
  * `sin(inputOp1(p, ctx))` *sin(x)          Sine*
  * `tan(inputOp1(p, ctx))` *tan(x)         Tangent*
  * `acos(inputOp1(p, ctx))` *acos(x)       Arccosine*
  * `asin(inputOp1(p, ctx))` *asin(x)        Arcsine*
  * `atan(inputOp1(p, ctx))` *atan(x)        Arctan ( Input1 )*
  * `atan2(inputOp1(p, ctx), inputOp2(p, ctx))` *atan2(x,y)   Arctan ( Input1 / Input2 )*
  * `cosh(inputOp1(p, ctx))` *cosh(x)       Hyperbolic Cosine*
  * `sinh(inputOp1(p, ctx))` *sinh(x)        Hyperbolic Sine*
  * `tanh(inputOp1(p, ctx))` *tanh(x)        Hyperbolic Tangent*
  * `log2(inputOp1(p, ctx))` *log2(x)         Log Base 2*
  * `log(inputOp1(p, ctx))` *log(x)            Natural Log*
  * `exp(inputOp1(p, ctx))` *exp(x)          e ^ Input1*
  * `exp2(inputOp1(p, ctx))` *exp2(x)        2 ^ Input1*
  * `pow(THIS_Param1, inputOp1(p, ctx))` *pow(x)         Base ^ Input1*
  * `pow(inputOp1(p, ctx), inputOp2(p, ctx))` *pow(x,y)      Input1 ^ Input2*
* `Param1` *Param 1*
* `Param2` *Param 2*
* `Vecparam1` *Vector Param 1*
* `Vecparam2` *Vector Param 2*
* `Coordtype` *Coord Type*
  * `useinput` *Use Input*
  * `float` *1D*
  * `vec3` *3D*
  * `vec2` *2D*
* `Returntype` *Return Type*
  * `useinput` *Use Input*
  * `Sdf` *SDF Result*
  * `float` *Float*
  * `vec4` *Vector4*
  * `Ray` *Ray*
  * `Light` *Light*
* `Contexttype` *Context Type*
  * `useinput` *Use Input*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
  * `RayContext` *Ray Context*
* `Inspect` *Inspect*

## Inputs

* `definition_in`
* `definition_in1`
* `definition_in2`
* `definition_in3`