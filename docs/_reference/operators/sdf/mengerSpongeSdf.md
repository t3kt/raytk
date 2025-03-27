---
layout: operator
title: mengerSpongeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mengerSpongeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mengerSpongeSdf/
op:
  category: sdf
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
    - vec3
    label: Box Scale Field
    name: boxScaleField
    returnTypes:
    - float
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Cross Scale Field
    name: crossScaleField
    returnTypes:
    - float
    supportedVariableInputs:
    - boxScaleField
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Step Offset Field
    name: stepOffsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - boxScaleField
    - crossScaleField
    supportedVariables:
    - step
    - normstep
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - boxScaleField
    - crossScaleField
    - stepOffsetField
    supportedVariables:
    - step
    - normstep
  name: mengerSpongeSdf
  opType: raytk.operators.sdf.mengerSpongeSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the shape.
  - label: Steps
    name: Steps
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of levels of detail.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Box Scale
    name: Boxscale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The scale of the boxes used at each step.
  - label: Cross Scale
    name: Crossscale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the holes cut through the boxes at each step.
  - label: Variant
    menuOptions:
    - label: Klems
      name: klems
    - label: TheArchCoder
      name: thearchcoder
    name: Variant
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Step Offset
    name: Stepoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  thumb: assets/images/reference/operators/sdf/mengerSpongeSdf_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---


Menger sponge fractal, made of boxes with holes cut through each axis.