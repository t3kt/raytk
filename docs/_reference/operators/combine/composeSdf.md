---
layout: operator
title: composeSdf
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/composeSdf
redirect_from:
  - /reference/opType/raytk.operators.combine.composeSdf/
op:
  category: combine
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
    label: definition_in_1
    name: definition_in_1
    returnTypes:
    - Sdf
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
    label: definition_in_2
    name: definition_in_2
    returnTypes:
    - Sdf
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
    label: definition_in_3
    name: definition_in_3
    returnTypes:
    - Sdf
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
    label: definition_in_4
    name: definition_in_4
    returnTypes:
    - Sdf
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
    label: definition_in_5
    name: definition_in_5
    returnTypes:
    - Sdf
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
    label: definition_in_6
    name: definition_in_6
    returnTypes:
    - Sdf
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
    label: definition_in_7
    name: definition_in_7
    returnTypes:
    - Sdf
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
    label: definition_in_8
    name: definition_in_8
    returnTypes:
    - Sdf
  name: composeSdf
  opType: raytk.operators.combine.composeSdf
  parameters:
  - label: Enable 1
    name: Enable1
  - label: Input 1
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input1
  - label: Translate 1
    name: Translate1
  - label: Combine 1
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine1
  - label: Radius 1
    name: Blendradius1
  - label: Number 1
    name: Blendnumber1
  - label: Offset 1
    name: Blendoffset1
  - label: Enable 2
    name: Enable2
  - label: Input 2
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input2
  - label: Translate 2
    name: Translate2
  - label: Combine 2
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine2
  - label: Radius 2
    name: Blendradius2
  - label: Number 2
    name: Blendnumber2
  - label: Offset 2
    name: Blendoffset2
  - label: Enable 3
    name: Enable3
  - label: Input 3
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input3
  - label: Translate 3
    name: Translate3
  - label: Combine 3
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine3
  - label: Radius 3
    name: Blendradius3
  - label: Number 3
    name: Blendnumber3
  - label: Offset 3
    name: Blendoffset3
  - label: Enable 4
    name: Enable4
  - label: Input 4
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input4
  - label: Translate 4
    name: Translate4
  - label: Combine 4
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine4
  - label: Radius 4
    name: Blendradius4
  - label: Number 4
    name: Blendnumber4
  - label: Offset 4
    name: Blendoffset4
  - label: Enable 5
    name: Enable5
  - label: Input 5
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input5
  - label: Translate 5
    name: Translate5
  - label: Combine 5
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine5
  - label: Radius 5
    name: Blendradius5
  - label: Number 5
    name: Blendnumber5
  - label: Offset 5
    name: Blendoffset5
  - label: Enable 6
    name: Enable6
  - label: Input 6
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input6
  - label: Translate 6
    name: Translate6
  - label: Combine 6
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine6
  - label: Radius 6
    name: Blendradius6
  - label: Number 6
    name: Blendnumber6
  - label: Offset 6
    name: Blendoffset6
  - label: Enable 7
    name: Enable7
  - label: Input 7
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input7
  - label: Translate 7
    name: Translate7
  - label: Combine 7
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine7
  - label: Radius 7
    name: Blendradius7
  - label: Number 7
    name: Blendnumber7
  - label: Offset 7
    name: Blendoffset7
  - label: Enable 8
    name: Enable8
  - label: Input 8
    menuOptions:
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    - label: Input 3
      name: input3
    - label: Input 4
      name: input4
    - label: Input 5
      name: input5
    - label: Input 6
      name: input6
    - label: Input 7
      name: input7
    - label: Input 8
      name: input8
    name: Input8
  - label: Translate 8
    name: Translate8
  - label: Combine 8
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
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
    - label: Stair Union
      name: stairUnion
    - label: Stair Intersect
      name: stairIntersect
    - label: Stair Difference
      name: stairDiff
    - label: Column Union
      name: columnUnion
    - label: Column Intersect
      name: columnIntersect
    - label: Column Difference
      name: columnDiff
    name: Combine8
  - label: Radius 8
    name: Blendradius8
  - label: Number 8
    name: Blendnumber8
  - label: Offset 8
    name: Blendoffset8
  status: beta

---
