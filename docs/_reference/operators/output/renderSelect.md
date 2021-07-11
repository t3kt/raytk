---
layout: operator
title: renderSelect
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/renderSelect
redirect_from:
  - /reference/opType/raytk.operators.output.renderSelect/
op:
  category: output
  name: renderSelect
  opType: raytk.operators.output.renderSelect
  parameters:
  - label: Output OP
    name: Outputop
  - label: Output Buffer
    menuOptions:
    - label: Color
      name: colorOut
    - label: SDF Result
      name: sdfOut
    - label: Depth
      name: depthOut
    - label: World Position
      name: worldPosOut
    - label: Normal
      name: normalOut
    - label: Ray Direction
      name: rayDirOut
    - label: Ray Origin
      name: rayOriginOut
    - label: Orbit Trap
      name: orbitOut
    - label: Near Hit
      name: nearHitOut
    - label: Step Count
      name: stepsOut
    - label: Iteration
      name: iterationOut
    - label: Object Id
      name: objectIdOut
    - label: Debug
      name: debugOut
    - label: UV
      name: uvOut
    name: Outputbuffer
  - label: Lock Buffer Menu
    name: Lockbuffermenu

---
