---
layout: page
title: ROP Code
nav_order: 1
---

# Writing ROP Code

Each ROP has one primary block of "function" code, and several other optional code blocks. Most of these blocks are designed to contain top-level declarations of variables and/or functions. Some blocks are intended to contain a snippet of code that will be inserted into another generated function.

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

Equivalent to:

| 0  | 1 | 2 |
| --- | --- | --- |
| `False` | `THIS_HAS_TWO_THINGS` | |
| | `THIS_STUFF` | `vec2(0.3, 0.1)` |
| | `THIS_FOO 3.5` | |

Generates:

```glsl
#define PREFIX_USE_THINGS
#define PREFIX_STUFF  vec2(0.3, 0.1)
#define PREFIX_FOO 3.5
```

Each ROP can have one explicitly defined macro table, and some number of generated tables produced by various helper subcomponents.

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
