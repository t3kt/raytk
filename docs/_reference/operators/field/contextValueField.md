---
layout: page
title: contextValueField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/contextValueField
redirect_from:
  - /reference/opType/raytk.operators.field.contextValueField/
---

# contextValueField

Category: field



Field that returns various fields from the context, from a downstream OP.

## Parameters

* `Coordtype` *Coord Type*
  * `vec2` *2D*
  * `vec3` *3D*
* `Contextfield` *Context Field*
  * `iteration` *Iteration*
  * `matorbit` *Orbit Trap (Material)*
  * `matsteps` *Step Count (Material)*
  * `matnearhits` *Near Hits (Material)*
  * `matiteration` *Iteration (Material)*
  * `matobjectid` *Object ID (Material)*
  * `lightorbit` *Orbit Trap (Light)*
  * `lightsteps` *Step Count (Light)*
  * `lightnearhits` *Near Hits (Light)*
  * `lightiteration` *Iteration (Light)*
  * `lightobjectid` *Object ID (Light)*
* `Inspect` *Inspect*
* `Help` *Help*