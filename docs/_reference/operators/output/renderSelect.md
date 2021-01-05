---
layout: operator
title: renderSelect
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/renderSelect
redirect_from:
  - /reference/opType/raytk.operators.output.renderSelect/
op:
  name: renderSelect
  opType: raytk.operators.output.renderSelect
  category: output
  parameters:
    - name: Outputop
      label: Output OP
    - name: Outputbuffer
      label: Output Buffer
      menuOptions:
        - name: colorOut
          label: Color
        - name: sdfOut
          label: SDF Result
        - name: depthOut
          label: Depth
        - name: worldPosOut
          label: World Position
        - name: normalOut
          label: Normal
        - name: rayDirOut
          label: Ray Direction
        - name: rayOriginOut
          label: Ray Origin
        - name: orbitOut
          label: Orbit Trap
        - name: nearHitOut
          label: Near Hit
        - name: stepsOut
          label: Step Count
        - name: iterationOut
          label: Iteration
        - name: objectIdOut
          label: Object Id
        - name: debugOut
          label: Debug
    - name: Lockbuffermenu
      label: Lock Buffer Menu
    - name: Help
      label: Help

---

# renderSelect

Category: output

