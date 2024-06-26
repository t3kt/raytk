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
  detail: See [Output Buffers](/raytk/guide/output-buffers/) for more details.
  name: renderSelect
  opType: raytk.operators.output.renderSelect
  parameters:
  - label: Output OP
    name: Outputop
  - label: Output Buffer
    menuOptions:
    - label: GUI
      name: guiOut
    - label: Color
      name: colorOut
    - label: SDF Result
      name: sdfOut
    - label: Value
      name: valueOut
    - label: Normal
      name: normalOut
    - label: Object Id
      name: objectIdOut
    - label: Depth
      name: depthOut
    - label: World Position
      name: worldPosOut
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
    - label: Debug
      name: debugOut
    - label: UV
      name: uvOut
    - label: Final Output
      name: finalOut
    - label: Custom 1
      name: customOut1
    - label: Custom 2
      name: customOut2
    - label: Position
      name: posOut
    - label: Direction
      name: dirOut
    - label: Velocity
      name: velOut
    - label: Angular Velocity
      name: angVelOut
    - label: Life + State
      name: lifeStateOut
    name: Outputbuffer
  summary: Accesses a color output buffer from a renderer.

---


Accesses a color output buffer from a renderer.

See [Output Buffers](/raytk/guide/output-buffers/) for more details.