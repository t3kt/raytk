---
layout: page
title: ROP Code
nav_order: 1
---

# Writing ROP Code
{: .no_toc }

Each ROP has one primary block of "function" code, and several other optional code blocks. Most of these blocks are designed to contain top-level declarations of variables and/or functions. Some blocks are intended to contain a snippet of code that will be inserted into another generated function.

<details open markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

## ROP Names

Each ROP has a unique name generated for it based on the ROP's path. These names are used throughout the toolkit and the shader code.

## Code Blocks

* OP globals: Global declarations such as variables or functions used by the OP.
* Init code: A snippet of code that the shader will call before running the rest of the shader code. Typically this is used to set up the values of global variables.
* Function: Declaration of the ROP's primary function. This can also contain supplemental functions used by the primary function.
* Material: A snippet of code that is inserted into a function that determines the color for a surface when the surface matches the ROP's material id.

## Preprocessing Applied to Code Blocks

Each block of code is passed through a series of modifications before eventually being injected into the shader.

The following symbols are replaced everywhere, even if they are part of a longer symbol (such as `THIS_Foo`):

* `THIS_`: The ROP name. This is used as a way to add unique prefixes to function / variable / macro names.
* `thismap`: Also the ROP name. This is intended for the name of the ROP's primary function.
* `THISMAT`: Unique material ID generated for the ROP (if applicable). This is implemented as a macro that resolves to a unique integer.
* `inputOp1` - `inputOp4`: The names of the attached input ROPs.

The following type aliases are replaced, only when they appear as a whole word without prefix or suffix:

* `CoordT`: The ROP's coordinate type.
* `ContextT`: The ROP's context type.
* `ReturnT`: The ROP's return type.

## General Guidelines for ROP Code

The generated shader contains combined elements from all of the blocks of all of the ROPs in the scene. This means that any declared symbols used by one ROP can't conflict with those of any other ROP, including other instances of the same ROP type. To avoid conflicts, all global symbols (functions, variables, macros) should use the `THIS_` prefix to keep them unique.

## Parameters

Each parameter defined by a ROP and listed in the definition's parameter list and special parameter list will be made available to all code as an alias macro like `THIS_Paramname` that references whatever the source of the parameter value is. Typically this will be a reference to the uniform array that is used to pass in parameter values. In some cases they could also be inlined values.

For multi-part parameters (`Par` styles including `XYZ`, `RGBA`, `UV` and `Float`/`Int` with more than 1 part), several aliases are generated. Each part in the macro will have its own alias, using each parameter's tuplet suffix (e.g. `THIS_Translatex`). There will also be an alias that evaluates to a value of the relevant `vec*` type, with the name of the tuplet without any suffix, which combines all of those parts (e.g. `THIS_Translate`).

For parameters in the definition's "macro" parameter list, an alias will be generated that evaluates to the literal inlined value of that parameter. For numeric parameters, this will be a simple inline float/int value.

For menu parameters, there will be a macro evaluating to the selected menu name itself (which is only useful when that is a valid piece of code such as a swizzle like `xy`). There will also be a macro that appends the selected menu name to the end of the parameter name separated by an underscore (e.g. `THIS_Param_value`), which is typically used for `#ifdef` blocks.

It is important to remember that because macro-based parameters use inlined values, any changes to them will cause the shader to rebuild. This is both a limitation (if the user wants to be able to change them quickly) and an optimization which avoids having to pass in those values and also allows GPU driver optimizations like dead code removal and loop unrolling.

```glsl
#define PREFIX_Amount       vecParams[17].y
#define PREFIX_Translatex   vecParams[18].x
#define PREFIX_Translatey   vecParams[18].y
#define PREFIX_Translate    vec2(vecParams[18].xy)
#define PREFIX_Inlined      12.5
#define PREFIX_Plane        yz
#define PREFIX_Plane_yz
```

## Macros

Each ROP can define several groups of macros. These are specified in DATs with 3 columns, which can involve evaluating Python expressions. The first column is checked for either `False` or `0`, stripping out those macros. This is used to toggle macros based on expressions. The second column is either the macro name, or the macro name and expression separated by a space. The third column is treated as the macro's value expression.

| 0  | 1 | 2 |
| --- | --- | --- |
|  `op("foo")["x"] > 2` | `'THIS_HAS_TWO_THINGS'` | |
| | `'THIS_USE_THINGS'` |
| | `'THIS_STUFF'` | `'vec2(0.3, 0.1)'` |
| | `'THIS_FOO 3.5'` |

Evaluates to:

| 0  | 1 | 2 |
| --- | --- | --- |
| `False` | `THIS_HAS_TWO_THINGS` | |
| | `'THIS_USE_THINGS'` |
| | `THIS_STUFF` | `vec2(0.3, 0.1)` |
| | `THIS_FOO 3.5` | |

Generates:

```glsl
#define PREFIX_USE_THINGS
#define PREFIX_STUFF  vec2(0.3, 0.1)
#define PREFIX_FOO 3.5
```

Each ROP can have one explicitly defined macro table, and some number of generated tables produced by various helper subcomponents.

### Global Macros

ROPs can also define a table of "global" macros. These differ from ROP-specific macros in that they are included earlier in the shader before library includes. They are intended to enable features within shared libraries. For example, `RAYTK_STEPS_IN_SDF` enables the `steps` field in the `Sdf` struct, and is used by ops that depend on it, allowing that field to be omitted if nothing is using it.

## Types

As mentioned above, the symbols `CoordT`, `ContextT` and `ReturnT` are replaced with the relevant types of the ROP. This is implemented using type alias macros such as `THIS_CoordT` which evaluates to a types such as `vec2` or `float`. Each ROP will also generate macros that append the type name such as `THIS_COORD_TYPE_vec2` and `THIS_RETURN_TYPE_Sdf`. These are typically used for switching blocks of code using `#ifdef`.

```glsl
#define PREFIX_CoordT   vec3
#define PREFIX_ContextT Context
#define PREFIX_ReturnT  Sdf
#define PREFIX_COORD_TYPE_vec3
#define PREFIX_CONTEXT_TYPE_Context
#define PREFIX_RETURN_TYPE_Sdf
```

## Inputs

When a ROP has an input definition, aliases like `inputOp3` are replaced by the name of that definition. This can be used both as a reference to that ROP's primary function, and as a prefix for macros.

```glsl
#ifdef inputOp1_COORD_TYPE_vec2
Sdf res = inputOp1(p.xy, ctx);
#else
Sdf res = inputOp1(p, ctx);
#endif
```

## Textures

A ROP can define a table of textures, each of which have a name and a path to a TOP. Each one will generate a prefixed macro like `THIS_textureName`. The output OP will use `select TOP`s to pull from the provided TOPs and feed them into the `glsl TOP` as inputs. The generated macros refer to the input textures by the index of the attached input.

Generated macro:
```glsl
#define PREFIX_texture sTD2DInputs[3]
``` 

Usage in ROP function:
```glsl
ReturnT thismap(CoordT p, ContextT ctx) {
  return texture(THIS_texture, p.xy).r;
}
```

## Buffers

## Materials

ROPs that define materials provide the "Material" code block. These OPs automatically generate a unique integer material identifier, which is made available to the ROP as `THISMAT`. SDF operators set the `material` (and/or `material2` field in the `Sdf` struct), which then gets passed along to the ouput shader's `map()` function return value. The output shader then inserts the provided code snippet into a generated switch block, which is run when the result's material id matches the generated material id for the ROP.

Typically ROPs will define a prefixed function in their "Function" block and then call it within the "Material" snippet.

Function block:
```glsl
ReturnT thismap(CoordT p, ContextT ctx) {
  Sdf res = inputOp1(p, ctx);
  assignMaterial(res, THISMAT);
  return res;
}

vec3 THIS_getColor(CoordT p, MaterialContext matCtx) {
  return THIS_Color; // ....
}
```

Material snippet:
```glsl
col.rgb = THIS_getColor(p, matCtx);
```

That snippet is inserted into a function like:

```glsl
vec3 getColor(vec3 p, MaterialContext matCtx, int m) {
  vec3 col = vec3(0.);
  if (m == MAT_PREFIX_1_ETC) {
    col.rgb = PREFIX_1_getColor(p, matCtx);
  } else if (m == MAT_PREFIX_2_ABC) {
    col.rgb = PREFIX_2_getColor(p, matCtx);
  }
  //...
  return col;
}
```

## Contexts

ROP functions are called with two parameters: a coordinate `p`, and a secondary context value `ctx`. The context value contains information about the context for which the function is being called. This includes both fixed global values and values that are modified or provided by one ROP and passed to the input ROPs that it calls.

There are several different types of contexts, each used for different reasons that a ROP is being called by the output OP's shader.

### Default Context

The `Context` type is used for the primary call made by the shader to evaluate the scene result. For raymarching, this is for the call at each marching step to evaluate the scene SDF. For 2D rendering, this is for the call made for each pixel to determine the output values.

#### Context Iteration

The `Context` type includes an `iteration` field which certain ROPs populate with different values depending on how/where it's calling an input. The value is a `vec4`, where the first value is an "index" and the second is a "total count". The third and fourth are not yet used.

Example ROPs that provide iteration values:
 
* The `reflect` ROP sets a value of `vec4(0, 2, 0, 0)` when calling the input if it is one one side of the reflection plane and a value of 1 when calling the input on the other side.
* The `mirrorOctant` ROP sets a different value for each quadrant, `vec4(0, 4, 0, 0)` for one quadrant, `vec4(1, 4, 0, 0)` for the next, and so on.

Several types of ROPs make use of the iteration values passed to them:

* The `iterationField` ROP will return the iteration in one of several formats (raw index, scaled to total count, full `vec4` data, etc).
* The `iterationSwitch` ROP will call one input for index 0 and the other for index 1.

### Camera Context

The `CameraContext` is used in raymarching when determining the position and direction of the camera ray. It contains information such as the render resolution, which can be used with the normalized UV coordinates in `p` to calculate values based on pixel offsets.

### LightContext

The `LightContext` is used in raymarching when determining the relevant light position and color for a surface ray hit. It includes the surface `Sdf` result and the surface normal vector.

### MaterialContext

The `MaterialContext` is used in raymarching when calculating the color to use for a ray surface hit. It includes the `Sdf` result, the camera `Ray`, the computed `Light`, and other properties used by materials.

## Working with SDF Results

The `Sdf` struct represents a ray hitting a surface (so a more accurate name might be `SurfaceHit`). It includes information about that surface and properties of the ray process that caused the hit. The struct is the only way that an SDF-based operator can pass value to the ROP that called it.

The struct will contain different fields depending on whether those features are being used. For example, if the "Object ID" output buffer is being used, it contains an `objectId` field. Because the struct can contain different types of fields, it is important to use the provided functions for things like creating and modifying them, rather than manually constructing them.

This code is problematic because it fails to account for properties like material blending settings, reflection properties (if those are being used), near hit values (if those are being used), etc:

```glsl
Sdf badRes;
badRes.x = dist;
badRes.material = THISMAT;
return badRes;
```

This code uses the provided functions to create and modify the `Sdf` value, which properly handle all the fields that are being used:

```glsl
Sdf goodRes = createSdf(dist);
assignMaterial(goodRes, THISMAT);
return goodRes;
```

Similarly, when combining two `Sdf` values, ROPs should use the `blendInSdf()` function, which appropriately handles all the fields:

```glsl
Sdf res1 = inputOp1(p, ctx);
Sdf res2 = inputOp2(p, ctx);
Sdf combinedRes = res1;
combinedRes.x = min(res1.x, res2.x);
float ratio = smoothBlendRatio(res1.x, res2.x, THIS_Foo);
blendInSdf(combinedRes, res2, ratio);
return combinedRes;
```

