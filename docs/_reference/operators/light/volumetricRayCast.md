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
  - label: Level
    name: Level
  - label: Skip Missed Rays
    name: Skipmissedrays
  - label: March Mode
    menuOptions:
    - label: Fixed Step
      name: fixedstep
    - label: Divisions
      name: divisions
    name: Marchmode
  - label: Fixed Step
    name: Fixedstep
  - label: Max Steps
    name: Maxsteps
  - label: Step Divisions
    name: Stepdivisions
  - label: Ray Miss Distance
    name: Raymissdist
  - label: Recalculate Light
    name: Recalculatelight
  - label: Enable Shadow
    name: Enableshadow
  status: beta

---
