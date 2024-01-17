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
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
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
    - label: BBS  (X[u] -> X[u])
      name: bbs
    - label: CityHash32 (1D)  (X[u] -> X[u])
      name: city11
    - label: CityHash32 (2D)  (XY[u] -> X[u])
      name: city12
    - label: CityHash32 (3D)  (XYZ[u] -> X[u])
      name: city13
    - label: CityHash32 (4D)  (XYZW[u] -> X[u])
      name: city14
    - label: Schechter and Bridson  (X[u] -> X[u])
      name: esgtsa
    - label: UE4 RandFast  (XY -> X)
      name: fast
    - label: Hash w/o Sine 1:1  (X -> X)
      name: hashwithoutsine11
    - label: Hash w/o Sine 2:1  (XY -> X)
      name: hashwithoutsine12
    - label: Hash w/o Sine 3:1  (XYZ -> X)
      name: hashwithoutsine13
    - label: Hash w/o Sine 1:2  (X -> XY)
      name: hashwithoutsine21
    - label: Hash w/o Sine 2:2  (XY -> XY)
      name: hashwithoutsine22
    - label: Hash w/o Sine 3:2  (XYZ -> XY)
      name: hashwithoutsine23
    - label: Hash w/o Sine 1:3  (X -> XYZ)
      name: hashwithoutsine31
    - label: Hash w/o Sine 2:3  (XY -> XYZ)
      name: hashwithoutsine32
    - label: Hash w/o Sine 3:3  (XYZ -> XYZ)
      name: hashwithoutsine33
    - label: Hash w/o Sine 1:4  (X -> XYZW)
      name: hashwithoutsine41
    - label: Hash w/o Sine 2:4  (XY -> XYZW)
      name: hashwithoutsine42
    - label: Hash w/o Sine 3:4  (XYZ -> XYZW)
      name: hashwithoutsine43
    - label: Hash w/o Sine 4:4  (XYZW -> XYZW)
      name: hashwithoutsine44
    - label: Hybrid Taus  (XYZW[u] -> X)
      name: hybridtaus
    - label: Interleaved Gradient  (XY -> X)
      name: ign
    - label: Integer Hash I  (X[u] -> X[u])
      name: iqint1
    - label: Integer Hash II  (XYZ[u] -> XYZ[u])
      name: iqint2
    - label: Integer Hash III  (XY[u] -> X[u])
      name: iqint3
    - label: JKiss32  (XY[u] -> X[u])
      name: jkiss32
    - label: Linear Congruential  (X[u] -> X[u])
      name: lcg
    - label: MD5GPU  (XYZW[u] -> XYZW[u])
      name: md5
    - label: Murmur Hash 3 1:1  (X[u] -> X[u])
      name: murmur311
    - label: Murmur Hash 3 2:1  (XY[u] -> X[u])
      name: murmur312
    - label: Murmur Hash 3 3:1  (XYZ[u] -> X[u])
      name: murmur313
    - label: Murmur Hash 3 4:1  (XYZW[u] -> X[u])
      name: murmur314
    - label: PCG Random  (X[u] -> X[u])
      name: pcg
    - label: PCG 2D  (XY[u] -> XY[u])
      name: pcg2d
    - label: PCG 3D  (XYZ[u] -> XYZ[u])
      name: pcg3d
    - label: PCG 3D 16  (XYZ[u] -> XYZ[u])
      name: pcg3d16
    - label: PCG 4D  (XYZW[u] -> XYZW[u])
      name: pcg4d
    - label: UE4 PseudoRandom  (XY -> X)
      name: pseudo
    - label: RanLim 32  (X[u] -> X[u])
      name: ranlim32
    - label: SuperFastHash 1:1  (X[u] -> X[u])
      name: superfast11
    - label: SuperFastHash 2:1  (XY[u] -> X[u])
      name: superfast21
    - label: SuperFastHash 3:1  (XYZ[u] -> X[u])
      name: superfast31
    - label: SuperFastHash 4:1  (XYZW[u] -> X[u])
      name: superfast41
    - label: Trig 2:1  (XY -> X)
      name: trig21
    - label: Wang 1:1  (X[u] -> X[u])
      name: wang11
    - label: 128-bit XOR Shift  (XYZW[u] -> X[u])
      name: xorshift128
    - label: 32-bit XOR Shift  (X[u] -> X[u])
      name: xorshift32
    - label: 32-bit XX Hash 1:1  (X[u] -> X[u])
      name: xxhash321
    - label: 32-bit XX Hash 2:1  (XY[u] -> X[u])
      name: xxhash322
    name: Function
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    - label: 4D
      name: vec4
    name: Coordtype
  status: beta

---
