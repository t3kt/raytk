---
layout: page
title: Concepts
---

RayTK is a collection of several types of components, which can be placed into scenes, and a set of tools for working with those components.

## Types of Components

* ROPs - create "definitions" for operations.
* OutputOPs - take in "definitions" and use them to build and run a shader.
* PostOPs - image filters or processors that are designed to work with the TOP streams from OutputOPs.
* RComps - helper components that work with other operators.

## Definitions

Definitions are chunks of data that come out of ROPs and are passed down chains of ROPs in a scene. They are represented as `DAT` tables.

Unless you are developing the core of the RayTK library itself, you will never need to deal directly with the contents of the Definitions. They should be treated as an opaque data type. They're just the "thing" that comes out of a ROP and goes into other ops.

Each Definition describes a GLSL function and its dependencies (such as parameters). The functions take in coordinates and other information, and produce some kind of value, such as a color, or the distance to a surface. So in a sense, Definitions have sub-types, such as "Definition of a function that looks up colors based on 3D coordinates", or "Definition of a function that decides what direction to shoot a ray based on 2D coordinates".

## ROPs

Each ROP produces a single Definition table, which describes that ROP's function code and properties.

Many ROPs take inputs of other Definition tables, which it merges with its own and sends it back out of the ROP. For example, a `rotate` ROP takes in an input and inserts its own definition of a function that rotates coordinates and then does whatever that input describes.

## OutputOPs

A Definition on its own is just a chunk of data in a DAT. To render a scene, the Definition needs to be fed into an OutputOP, such as `raymarchRender3d`.

These components take in one or more Definition inputs, construct a shader based on those inputs, and run it in a `GLSL TOP`, to produce various types of image outputs. They are equivalent to `Render TOP`s, which take in some `Geometry COMP`s and render them to an image.

As the name suggests, `raymarchRender3d` uses the ROP network to build a raymarching shader, producing a rendered view of your scene, from some sort of camera.

## Execution Chain

The Output ROP at the end of a chain of ROPs generates a shader along with things like uniforms, textures, etc. It then runs that shader in a `GLSL TOP` and outputs the results.

Each type of Output ROP has a block of GLSL called the "body", which contains the `main()` function. The body code will call functions from input ROPs for various purposes.

In the case of `render2d` (when using a vector field input ROP), it calls the input function once per pixel, to determine the color of that pixel.

In the case of `raymarchRender3d`, the main scene input is executed once per each step of the rays. In addition to the scene input, `raymarchRender3d` has an input for a camera function, which called for each pixel of output to determine where the ray goes, and a light function that is called by materials to determine colors.

## Data Types

There are several types of data that a ROP function can return, including:
* `Sdf`: An SDF result, including surface distance, material settings, and other properties.
* `float`: A single floating point value. These can be used to drive the parameters of other ROPs, such as applying different amounts of rotation for different points in space.
* `vec4`: A 4-part vector value. These can be used to drive the parameters of other ROPs, such as applying colors based on position in space.
* `Ray`: A position and direction. These are returned by camera ROPs, to determine what direction the ray should march for each pixel of the output.
* `Light`: A point in space, and an amount of color. These are returned by light ROPs.

There are several types of coordinates that a ROP can use:
* `float`: 1D coordinates, which can be used for 1D vector fields.
* `vec2`: 2D coordinates, which are used in 2D SDFs, texture lookups, and screen UV coordinates.
* `vec3`: 3D coordinates, which are the main coordinate type for SDFs and raymarching.
