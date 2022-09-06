---
layout: page
title: The Raymarching Process
nav_order: 4
---

# The Raymarching Process

The `raymarchRender3D` operator takes in an SDF describing a scene, and several other types of inputs, and uses a raymarching process to produce a color for each pixel of output.

This page breaks down that process and how different features fit into it.

## General Outline

At a high level, the raymarching process works like this, for each pixel of output:

1. Pick a starting position and a direction for the pixel.
2. Move a point along that ray (origin position and direction)
   1. At each step, check the SDF to determine what the closest surface is and how far away it is.
   2. If the closest surface is close enough to be considered a hit, stop the marching process and move to the next stage.
   3. If the point has gone beyond the maximum distance or gone outside the scene bounds, consider it a miss and move on.
   4. If it isn't a hit, take another step along the ray.
3. If the ray hit a surface, determine a color for it.
4. If the ray did not hit a surface, determine a background color.
5. If enabled, a secondary raymarch is done to add color to the result. This is used for volumetric light.
6. Output the resulting color (and other data like depth).

## Camera

The camera operator connected to the renderer (or a default internal camera if none is connected) is used to determine where in space the lens is and what direction it's pointing for each pixel.

## SDF

The SDF connected to the renderer is used to determine the closest surface to a point in space as well as some properties of that part of the surface.

The renderer calls the SDF in a few different parts of the process:

* While marching the ray from the camera into the scene.
* When determining surface normals (by checking several nearby points and comparing the results).
* When marching a ray from a surface hit towards a light to see if there's a shadow.
* When marching a ray from a surface hit away from the surface to get a reflection color.

In some of those cases, the additional properties of the surface are relevant (e.g. the material id and uv coordinates).

But in other cases, all it cares about is whether a point has hit a surface (calculating normals, checking shadows).
For these cases, some operators will skip work that isn't needed (like calculating uv coordinates).

## Determining Colors For Surface Hits

When a ray has hit a surface, the renderer needs to calculate a color for that spot on the surface.

### Choosing and Assigning Materials

This is where materials come in. Material operators (such as `basicMat` or `modularMat`) insert their unique ID number into the surface properties.
The renderer uses those IDs to pick which function (provided by the material operator) it should call to get the color.

In cases where combiners are used to merge surfaces, there can be two different material IDs and a ratio of how much to use from each. The surface also ends up with two separate UV coordinates since those may differ.
When there are two materials, the renderer calls each of them and then blends the results using the ratio.

### Preparing `MaterialContext`

Before the renderer calls the material(s), it packages up some info (refered to as a `MaterialContext`) that's required by most materials:

* The surface properties from the SDF (including the assigned surface color property from `assignColor`)
* The origin and direction of the ray that hit the surface.
* The position and color of the light.
* The surface normal.
  * This is produced by calling the SDF for several nearby points and comparing the results.
* The amount of shadow (if enabled).
  * This is calculated by marching another ray from the surface towards the light to check if anything is blocking it.
* The reflected color (if enabled).
  * This is calculated basically by doing the render process from the perspective of that surface hit to get the color that would be reflected onto that spot on the surface.
  * Depending on the settings, this process may repeat multiple times, bouncing the ray from one surface to another.
* (Not yet implemented) The refracted color.
* UV coordinates relevant to the current material.
* Coordinates in space at the point in the process when the material is assigned (referred to as material local position). This allows transforms to be applied after a material is assigned without impacting how the material uses its position to pass to input fields.

### Lights

Lights are called by the renderer when preparing the `MaterialContext`, to produce a position (where the light is) and a color (which may include adjustments based on the distance from the light).

Lights can produce different colors for different surface hits.

Lights can also produce different positions for different surface hits. The `directionalLight` uses this to produce a position that is always in the same direction relative to the surface hit.

When multiple lights are used (via `multiLight`) the renderer repeats the colorization process separately for each light, and then adds the results to get the final color.

### Using Materials to Produce Colors

When the renderer asks the relevant material for a color for a surface hit, it passes along the info in the `MaterialContext`.

Different materials use different calculations to produce their color.

Many materials support inputs that it can call to get parameters (like the base color, or roughness). When they do so, they pass in the `MaterialContext`, so anything upstream from them can use its properties.

The `modularMat`, when calculating a color, essentially just calls several inputs and adds up the resulting colors. Those inputs are typically operators like `specularContrib`, but they can be any float/vector field that can work with `MaterialContext`.

