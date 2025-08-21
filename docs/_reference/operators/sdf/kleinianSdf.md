---
layout: operator
title: kleinianSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/kleinianSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.kleinianSdf/
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
    - PopContext
    coordTypes:
    - vec3
    label: KleinR Field
    name: kleinRField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: KleinI Field
    name: kleinIField
    returnTypes:
    - float
    supportedVariableInputs:
    - kleinRField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    supportedVariableInputs:
    - kleinRField
    - kleinIField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: Box Size Field
    name: boxSizeField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - kleinRField
    - kleinIField
    - scaleField
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
    - PopContext
    coordTypes:
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - kleinRField
    - kleinIField
    - scaleField
    - boxSizeField
    supportedVariables:
    - step
    - normstep
  keywords:
  - fractal
  name: kleinianSdf
  opType: raytk.operators.sdf.kleinianSdf
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Klein R
    name: Kleinr
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Klein I
    name: Kleini
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Box Size
    name: Boxsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Sphere Inversion
    name: Enableinversion
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Inversion Center
    name: Inversioncenter
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Inversion Radius
    name: Inversionradius
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf/kleinianSdf_thumb.png
  variables:
  - label: Step Index
    name: step
  - label: Normalized Step (0..1)
    name: normstep

---
