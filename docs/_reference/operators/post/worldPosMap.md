---
layout: operator
title: worldPosMap
parent: Post Operators
grand_parent: Operators
permalink: /reference/operators/post/worldPosMap
redirect_from:
  - /reference/opType/raytk.operators.post.worldPosMap/
op:
  category: post
  detail: In order for this to work, the associated raymarchRender3D has to have its
    World Position output enabled.
  inputs:
  - label: worldPos_in
    name: worldPos_in
    summary: World position data from a raymarchRender3D's world position output.
  name: worldPosMap
  opType: raytk.operators.post.worldPosMap
  parameters:
  - label: Range X
    name: Rangex
  - label: Range Y
    name: Rangey
  - label: Range Z
    name: Rangez
  - label: Snapshot Range
    name: Snapshotrange
    summary: Looks at the world position data and finds the minimum / maximum for
      each axis and updates `Rangex`, `Rangey`, `Rangez` so the data is scaled from
      that range to 0..1.
  - label: Output OP
    name: Outputop
  summary: Access the world position values from a raymarchRender3D, scaled to a normalized
    range.

---


Access the world position values from a raymarchRender3D, scaled to a normalized range.

In order for this to work, the associated raymarchRender3D has to have its World Position output enabled.