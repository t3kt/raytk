---
layout: operator
title: hashField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/hashField
redirect_from:
  - /reference/opType/raytk.operators.field.hashField/
op:
  category: field
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
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  name: hashField
  opType: raytk.operators.field.hashField
  parameters:
  - label: Function
    menuOptions:
    - label: BBS
      name: bbs
    - label: CityHash32 (1D)
      name: city11
    - label: CityHash32 (2D)
      name: city12
    - label: CityHash32 (3D)
      name: city13
    - label: CityHash32 (4D)
      name: city14
    - label: Schechter and Bridson hash
      name: esgtsa
    - label: UE4 RandFast
      name: fast
    - label: Hash without Sine 1:1
      name: hashwithoutsine11
    - label: Hash without Sine 2:1
      name: hashwithoutsine12
    - label: Hash without Sine 3:1
      name: hashwithoutsine13
    - label: Hash without Sine 1:2
      name: hashwithoutsine21
    - label: Hash without Sine 2:2
      name: hashwithoutsine22
    - label: Hash without Sine 3:2
      name: hashwithoutsine23
    - label: Hash without Sine 1:3
      name: hashwithoutsine31
    - label: Hash without Sine 2:3
      name: hashwithoutsine32
    - label: Hash without Sine 3:3
      name: hashwithoutsine33
    - label: Hash without Sine 1:4
      name: hashwithoutsine41
    - label: Hash without Sine 2:4
      name: hashwithoutsine42
    - label: Hash without Sine 3:4
      name: hashwithoutsine43
    - label: Hash without Sine 4:4
      name: hashwithoutsine44
    - label: Hybrid Taus
      name: hybridtaus
    - label: Interleaved Gradient Noise
      name: ign
    - label: Integer Hash I
      name: iqint1
    - label: Integer Hash II
      name: iqint2
    - label: Integer Hash III
      name: iqint3
    - label: JKiss32
      name: jkiss32
    - label: Linear Congruential Generator
      name: lcg
    - label: MD5GPU
      name: md5
    - label: Murmur Hash 3 1:1
      name: murmur311
    - label: Murmur Hash 3 2:1
      name: murmur312
    - label: Murmur Hash 3 3:1
      name: murmur313
    - label: Murmur Hash 3 4:1
      name: murmur314
    - label: PCG Random
      name: pcg
    - label: PCG 2D
      name: pcg2d
    - label: PCG 3D
      name: pcg3d
    - label: PCG 3D 16
      name: pcg3d16
    - label: PCG 4D
      name: pcg4d
    name: Function
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
  - label: Coord Type
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  status: alpha

---
