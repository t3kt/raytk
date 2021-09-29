---
layout: operator
title: instance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/instance
redirect_from:
  - /reference/opType/raytk.operators.filter.instance/
op:
  category: filter
  detail: 'It is important to note that unless something in the input chain is making
    use of the iteration to change or

    move those copies, they will all be in the same position. The `rangeTransform`
    operator is designed for this

    purpose, though there are also other ops that can do so.


    Refer to the Iteration guide for details.


    It is also important to note that this operator, like `radialClone` evaluates
    its input separately for each

    iteration, which can cause a significant drain on resources if the input network
    is complex or costly.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  keywords:
  - copy
  - instance
  - iterate
  - repeat
  name: instance
  opType: raytk.operators.filter.instance
  parameters:
  - label: Enable
    name: Enable
  - label: Instance Count
    name: Instancecount
    summary: The number of copies to produce and merge.
  - label: Combine
    menuOptions:
    - description: Combines the shapes so that all of their volumes are included.
      label: Simple Union
      name: simpleUnion
    - description: Combines the shapes so that only the places where all overlap are
        included.
      label: Simple Intersect
      name: simpleIntersect
    - description: Subtracts the second copy from the first, the third from that,
        and so on.
      label: Simple Difference
      name: simpleDiff
    - label: Smooth Union
      name: smoothUnion
    - label: Smooth Intersect
      name: smoothIntersect
    - label: Smooth Difference
      name: smoothDiff
    - label: Round Union
      name: roundUnion
    - label: Round Intersect
      name: roundIntersect
    - label: Round Difference
      name: roundDiff
    - label: Chamfer Union
      name: chamferUnion
    - label: Chamfer Intersect
      name: chamferIntersect
    - label: Chamfer Difference
      name: chamferDiff
    name: Combine
    summary: How to combine the copies. Only the "simple" options are guaranteed to
      work properly. The others may produce unexpected and problematic results.
  - label: Radius
    name: Radius
  - label: Enable Transform
    name: Enabletransform
  - label: Transform CHOP
    name: Transformchop
  - label: Enable Translate
    name: Enabletranslate
  - label: Enable Rotate
    name: Enablerotate
  summary: Repeats its input some number of times, exposing the index as the iteration
    x value, and combines the results.

---


Repeats its input some number of times, exposing the index as the iteration x value, and combines the results.

It is important to note that unless something in the input chain is making use of the iteration to change or
move those copies, they will all be in the same position. The `rangeTransform` operator is designed for this
purpose, though there are also other ops that can do so.

Refer to the Iteration guide for details.

It is also important to note that this operator, like `radialClone` evaluates its input separately for each
iteration, which can cause a significant drain on resources if the input network is complex or costly.