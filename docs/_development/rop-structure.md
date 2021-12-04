---
layout: page
title: ROP Structure
nav_order: 0
---

# ROP Structure

ROPs are the core of the RayTK library. A ROP is essentially some chunks of GLSL code, and some metadata.

A ROP is a COMP that generates a Definition, which is output as a DAT table.

## ROP Definitions

Each ROP contributes one row to a DAT table that also contains rows for all the ROPs that are upstream.

Inside each ROP, an `opDefinition` COMP is used to construct the definition.

A definition contains:

* `name`: globally unique name for the ROP, based on the path.
* `path`: path to the ROP.
* `opType`: identifies the type of ROP, and is derived from the path of the clone master used to create a ROP.
* `opVersion`: version of that particular type of ROP.
* `functionPath`: path to a text DAT containing the main chunk of code.
* `paramSource`: path to a CHOP containing the values of the parameters for the ROP.
* `paramTable`: path to a table listing the globally unique names of the ROP's individual parameters.
* `paramTupletTable`: path to a table with details about the parameters, organized into tuplets.
* `materialTable`: path to a table listing out the material identifiers used by the ROP.
* `macroTable`: path to a table with preprocessor macros used by the ROP's code.
* `textureTable`: path to a table listing out texture sources used by the ROP.
* `libraryNames`: names or paths of shared libraries that the ROP depends on.
* `initPath`: path to a text DAT with initialization code that the ROP needs to run before its other code is used.
* `opGlobalsPath`: path to a text DAT with declarations of global variables used by the ROP (generally initialized using the code from the `initPath`).
* `coordType`: the type of coordinates that the ROP's function accepts.
* `returnType`: the type of value the that the ROP's function returns.
* `contextType`: the type of context that the ROP's function expects along with the coordinates.
* `inputNames`: the names of other ROPs that this ROP's function calls.

## ROP Functions and GLSL Types

Each ROP has a main function that it contributes to the shader. All of these functions take in two parameters: coordinates, and context, and return a single value.

```glsl
ReturnT sphere1(CoordT p, ContextT ctx) {
  return createSdf(length(p));
}
```

### Coordinate types

* `vec3`: 3D coordinates, such as a position along a ray as it is marching along through space.
* `vec2`: 2D coordinates, such as screen-space UV coordinates, texture coordinates, or positions used for 2D SDFs.
* `float`: 1D coordinates, which can be used for things like looking up how much to apply an effect based on distance from some point, or how to blend between two values.

### Context types

Each ROP function takes a second parameter that is used to pass along additional information about the context in which the function is being called. ROPs often don't make use of this, but they need to pass it along when calling other ROPs since they might need it.

* `Context`: This is the most common type, which is used when evaluating an SDF during raymarching. It contains fields like `iteration`, which is used in cases like the `reflect` ROP so its input can do something different depending on which side of the reflection plane it's on.
* `LightContext`: Used by light ROPs to pass along information about the surface that it is being applied to and the normal direction.
* `MaterialContext`: Used by materials to pass along information about the surface that it is being applied to, the light that's being used, and where the ray that hit it came from.
* `CameraContext`: Used by cameras to pass along information like the output resolution.
* `RayContext`: Used by ray modifiers that bend or alter rays.

### Return types

Each ROP function produces a single return value.

* `Sdf`: The result of a signed distance function (SDF), representing what the closest shape is and how far it is from the ray position. It also contains information like which material to use.
* `float`: A single numeric value. This can be used for value fields that determine how much of something to apply based on a position in space.
* `vec4`: 4 numeric values. This can be used for vector fields or colors.
* `Ray`: A position in 3D space and a direction. Cameras return one of these for each pixel in the ouput.
* `Light`: Information about how much color is provided by a light to a surface.
