---
layout: page
title: Variable Handling
nav_order: 5
---

# Variable Handling

## What Are Variables?

Many ROPs support what are known as "variables". These are values which a ROP makes available to upstream operators (anything connected to one of its inputs or to one of those inputs' inputs, and so on).

Variables provide context-specific information that can be used to base fields on how and where they are being used.

For example, `torusSdf` provides a variable for the angle around its center (normalized to a 0..1 range). This could be referenced by a `waveField` controlling the thickness of the torus. No matter where the torus is placed, or what axis its on, that `waveField` would always be using the correct value.

## Referencing Variables

The `variableReference` ROP takes a reference to a provider ROP and the name of a variable, and returns the value when called.

It does this by specifying a table of references (though there's only one item in the table), which gets included in the ROP's definition and passed to the `shaderBuilder`.

It is technically possible for there to be other types of ROPs that use references, but in practice, it's only `variableReference` (for now).

## Connecting Variables and References

After pulling together all the ROPs in the scene, the `shaderBuilder` ends up with two tables: variables and references. It matches references to variables, and strips out any variables that aren't referenced.

Then it takes the results and generates code for them:
* Preprocessor macros, which indicate which variables should be provided, what their types are, and helpers for converting them to the relevant supported return type.
* Global variables, which hold the values of the variables.

## Providing Variables

A ROP can provide a table that lists out the variables that it can provide, with names and data types.

Within the code for a ROP that provides a variable, there will be a conditional block that calculates the value and puts it into the global variable.

```glsl
#ifdef THIS_EXPOSE_normangle
THIS_normangle = atan(p.x, p.z) / TAU + .5;
#endif
```

This allows operators to skip calculations that might not be needed, for variables that aren't referenced.

## Where Variables Can Be Used

The rules around where variables can be used all come down to this: a variable has to be populated before it can be used.

This means that (with certain exceptions) all paths from a `variableReference` to a render have to pass through the operator that provides the variable for that reference.

In many cases, a ROP will have several inputs, but only some of them will be able to use certain variables.

For example, `reflect` provides a `side` variables indicating which side the current position is on. However, the input that determines where the reflection plane is can't use that variable, since it can't be determined until after the reflection plane is chosen. But the primary input, if it was an SDF for example, would be able to use the `side` since it would have already been determined by the time the `reflect` calls the SDF.
