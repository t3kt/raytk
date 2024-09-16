---
layout: operator
title: texture3dVolume
parent: Volume Operators
grand_parent: Operators
permalink: /reference/operators/volume/texture3dVolume
redirect_from:
  - /reference/opType/raytkVolumes.operators.volume.texture3dVolume/
op:
  category: volume
  detail: The volume is defined for a box-shaped area, and the texture is stretched
    to fill that area.
  moduleName: raytkVolumes
  name: texture3dVolume
  opType: raytkVolumes.operators.volume.texture3dVolume
  parameters:
  - label: Volume Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Center of the volume box.
  - label: Volume Size
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Size of the volume box.
  - label: Density Texture
    name: Densitytexture
    summary: 3D texture that contains density values in the red channel.
  - label: Distance Texture
    name: Distancetexture
    summary: Optional 3D texture that contains SDF distance values in the red channel.
  - label: Color Texture
    name: Colortexture
    summary: Optional 3D texture that contains color values.
  status: beta
  summary: Creates a Volume based on a 3D texture that contains density values.

---


Creates a Volume based on a 3D texture that contains density values.

The volume is defined for a box-shaped area, and the texture is stretched to fill that area.