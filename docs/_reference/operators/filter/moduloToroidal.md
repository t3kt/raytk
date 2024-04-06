---
layout: operator
title: moduloToroidal
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloToroidal
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloToroidal/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
    supportedVariableInputs:
    - repetitionsField
    - radiusField
    - thicknessField
    - shiftField
    supportedVariables:
    - cell
    - normcell
    - angle
    - normangle
    - innerangle
    - norminnerangle
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
    label: Repetitions Field
    name: repetitionsField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - angle
    - normangle
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - repetitionsField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - repetitionsField
    - radiusField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
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
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - repetitionsField
    - radiusField
    - thicknessField
    supportedVariables:
    - angle
    - normangle
    - cell
    - normcell
  name: moduloToroidal
  opType: raytk.operators.filter.moduloToroidal
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Repetitions
    name: Repetitions
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Shift
    name: Shift
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/moduloToroidal_thumb.png
  variables:
  - label: cell
    name: cell
  - label: normcell
    name: normcell
  - label: angle
    name: angle
  - label: normangle
    name: normangle
  - label: innerangle
    name: innerangle
  - label: norminnerangle
    name: norminnerangle

---
