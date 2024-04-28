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
  - label: Direction Rotate
    name: Dirrotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Look At Mode
    menuOptions:
    - label: Include Position Translate
      name: includepos
    - label: Separate Translate Only
      name: separate
    name: Lookatmode
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Look At Translate
    name: Lookattranslate
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta

---
