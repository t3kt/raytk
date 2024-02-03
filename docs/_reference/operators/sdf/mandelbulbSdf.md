---
layout: operator
title: mandelbulbSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mandelbulbSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mandelbulbSdf/
op:
  category: sdf
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
    - vec3
    label: Shift (Theta, Phi) field
    name: shiftField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - step
    - normstep
  keywords:
  - fractal
  - mandelbrot
  - mandelbulb
  name: mandelbulbSdf
  opType: raytk.operators.sdf.mandelbulbSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Power
    name: Power
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The number of repetitions around the z axis.
  - label: Theta Shift
    name: Thetashift
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Offset the theta rotation.
  - label: Phi Shift
    name: Phishift
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Offset the phi rotation.
  - label: Iterations
    name: Iterations
    readOnlyHandling: constant
    regularHandling: constant
    summary: The number of steps used when refining the fractal.
  summary: Mandelbulb fractal.
  thumb: assets/images/reference/operators/sdf/mandelbulbSdf_thumb.png
  variables:
  - label: step
    name: step
  - label: normstep
    name: normstep

---


Mandelbulb fractal.