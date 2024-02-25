---
layout: operator
title: volumetricRayCast
parent: Light Operators
grand_parent: Operators
permalink: /reference/operators/light/volumetricRayCast
redirect_from:
  - /reference/opType/raytk.operators.light.volumetricRayCast/
op:
  category: light
  inputs:
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Light Volume
    name: definition_in
    returnTypes:
    - float
    - vec4
  name: volumetricRayCast
  opType: raytk.operators.light.volumetricRayCast
  parameters:
  - label: Enable Volumetric Light
    name: Enablevolumetric
    readOnlyHandling: baked
    regularHandling: baked
  - label: Level
    name: Level
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Skip Missed Rays
    name: Skipmissedrays
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: March Mode
    menuOptions:
    - label: Fixed Step
      name: fixedstep
    - label: Divisions
      name: divisions
    name: Marchmode
    readOnlyHandling: baked
    regularHandling: baked
  - label: Fixed Step
    name: Fixedstep
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Max Steps
    name: Maxsteps
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Step Divisions
    name: Stepdivisions
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Ray Miss Distance
    name: Raymissdist
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Recalculate Light
    name: Recalculatelight
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  status: beta

---
