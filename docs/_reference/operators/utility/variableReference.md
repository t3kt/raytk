---
layout: operator
title: variableReference
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/variableReference
redirect_from:
  - /reference/opType/raytk.operators.utility.variableReference/
op:
  category: utility
  detail: 'These operators are generally created using the "Reference Variable" option
    in the editor tools menu.


    <iframe width="560" height="315" src="https://www.youtube.com/embed/eqqOlSEk0YA"
    frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media;
    gyroscope; picture-in-picture" allowfullscreen></iframe>'
  name: variableReference
  opType: raytk.operators.utility.variableReference
  parameters:
  - label: Enable
    name: Enable
  - label: Source ROP
    name: Source
  - label: Source Variable
    name: Variable
  - label: Variable Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector2
      name: vec2
    - label: Vector3
      name: vec3
    - label: Vector
      name: vec4
    - label: Bool
      name: bool
    - label: BoolVector2
      name: bvec2
    - label: BoolVector3
      name: bvec3
    - label: BoolVector4
      name: bvec4
    - label: Int
      name: int
    - label: IntVector2
      name: ivec2
    - label: IntVector3
      name: ivec3
    - label: IntVector4
      name: ivec4
    - label: UInt
      name: uint
    - label: UIntVector2
      name: uvec2
    - label: UIntVector3
      name: uvec3
    - label: UIntVector4
      name: uvec4
    - label: SDF
      name: Sdf
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    - label: Particle
      name: Particle
    name: Variabletype
  - label: Field
    menuOptions:
    - label: (value)
      name: this
    name: Field
  - label: Default Value
    name: Defaultval
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Accesses the value of a variable provided by another operator.

---


Accesses the value of a variable provided by another operator.

These operators are generally created using the "Reference Variable" option in the editor tools menu.

<iframe width="560" height="315" src="https://www.youtube.com/embed/eqqOlSEk0YA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>