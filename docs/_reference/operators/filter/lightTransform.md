---
layout: operator
title: lightTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/lightTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.lightTransform/
op:
  category: filter
  detail: Similar to `cameraTransform`, this operator is specificaly designed to work
    on lights.
  inputs:
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    required: true
    returnTypes:
    - Light
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Position Translate Field
    name: posTranslateField
    returnTypes:
    - vec4
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Direction Rotate Field
    name: dirRotateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - posTranslateField
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Look At Translate Field
    name: lookAtTranslateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - posTranslateField
    - dirRotateField
  name: lightTransform
  opType: raytk.operators.filter.lightTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Position Translate
    name: Postranslate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Translation offset applied to the position of the light source.
  - label: Direction Rotate
    name: Dirrotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotation applied to the direction which the light source is facing.
  - label: Look At Mode
    menuOptions:
    - description: The look at position should be moved by the same amount that the
        main position is moved.
      label: Include Position Translate
      name: includepos
    - description: The look at position should remain in place regardless of how the
        main position moves.
      label: Separate Translate Only
      name: separate
    name: Lookatmode
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the look at position (if used) should be adjusted with the main
      position or remain stationary.
  - label: Look At Translate
    name: Lookattranslate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Translation offset applied to only the look at position.
  status: beta
  summary: Specialized transform that can be applied to lights, taking into account
    things like look at direction.

---


Specialized transform that can be applied to lights, taking into account things like look at direction.

Similar to `cameraTransform`, this operator is specificaly designed to work on lights.