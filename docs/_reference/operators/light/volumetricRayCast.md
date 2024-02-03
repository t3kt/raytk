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
    readOnlyHandling: macro
    regularHandling: macro
  - label: Level
    name: Level
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Skip Missed Rays
    name: Skipmissedrays
    readOnlyHandling: constant
    regularHandling: runtime
  - label: March Mode
    menuOptions:
    - label: Fixed Step
      name: fixedstep
    - label: Divisions
      name: divisions
    name: Marchmode
    readOnlyHandling: macro
    regularHandling: macro
  - label: Fixed Step
    name: Fixedstep
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Max Steps
    name: Maxsteps
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Step Divisions
    name: Stepdivisions
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Ray Miss Distance
    name: Raymissdist
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Recalculate Light
    name: Recalculatelight
    readOnlyHandling: macro
    regularHandling: macro
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: macro
    regularHandling: macro
  status: beta

---
