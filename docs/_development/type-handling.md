---
layout: page
title: Data Type Handling
nav_order: 3
---

# Data Type Handling

There are several categories of data types used in RayTK:

1. Coordinates (1D, 2D, 3D)
2. Return values (Sdf surface info, float, vector, etc.)
3. Contexts (Context, MaterialContext, etc)

When building the shader, each ROP ends up using exactly one type from each category.

In other words, a ROP is a function, taking in a coordinate and a context, and returning a value.

When a ROP has an input ROP, it's responsible for providing a coordinate and a context to that input when it calls it. And then it uses the return value from that input.

## Contexts

Contexts are a secondary piece of data passed into each ROP's function with supplemental info, providing by the ROP that's calling it.

There are several types of contexts, including:

1. `Context`: the standard data passed while marching a ray
2. `MaterialContext`: data with properties of an sdf surface like surface normal, assigned color, material id, uv coordinates.  When materials are calculating colors, they can use those properties.

## The Simple Case

In the most simple case, each ROP declares which specific type it's going to use for each category.

For example, a `boxSdf` will always use 3D coordinates, will produce `Sdf` surface info, and will use the standard `Context`.

### Why This Is Problematic

This is nice and simple but it imposes limitations. It means that the ROP can only be attached to certain inputs of certain types of ROPs.

For a `boxSdf`, it's easy, but for something like a `waveField`, it might be connected to something expecting 2D coordinates, or it might be used within a material (using `MaterialContext`).

In early versions of RayTK, this meant that many ROPs had a Context type parameter and a Coordinate type parameter. And those had to be set to the types expected by whatever the ROP gets connected to.

## Type Inheritance

For many ROPs, they don't really care what type of coordinates they or what return value they produce.

A `rotate` might produce a vector or an Sdf, depending on its input. And it could use either 2D or 3D coordinates.

So ROPs can specify that they inherit whatever coordinate or return (or context) type is connected to their input.

They may also limit which types it allows, in other words saying: "I use whatever type of coordinates my input uses, but it has to be either 2D or 3D".

To represent this, in the definition produced by a `rotate` would reference which ROP's coordinate type it uses. This reference is resolved down to a specific type later in the process.

## Multi-Types

Type inheritance involves types flowing downward, from inputs to outputs.

But what if an input ROP says that it could use one of several possible types?

For example, `constantField` doesn't care what type of coordinates or context it gets since it doesn't use them anyway. To handle that, it specifies several possible coordinate types, and several possible context types.

## Type Restriction

While the `constantField` could accept any type of coordinate, whatever it's connected to might have more specific requirements.

For example, if it was connected to the "Size" input on a `boxSdf`, the `boxSdf` will only be able to provide it with 3D coordinates. (This would be an unnecessary use of a `constantField`, but it's useful as an example.)

So as the `boxSdf` takes in the definition from the `constantField`, it restricts which types the `constantField` could get. In this case it would be restricting it down to only one type, but it could be several.

By the time the ROP definitions get to the `shaderBuilder` inside a renderer, each one needs to have its types restricted to a single type per category.

So each input on a renderer has rules saying which type it prefers in the case where there could be multiple. For example, `render2D` can take an input that says "I'm either 2D or 1D". But in that case, it picks "2D" since it prefers that over 1D. But if its input only supports 1D, then it would use that instead.

## Type Resolution

The `shaderBuilder` gets a table of ROP definitions, with columns for coord type, context type, and return type.

At this point it finds any that are references ("I use whatever coord type X is using") and replaces those with the specific type that the target of the reference ended up with (after all the restrictions reducing it to a single type).

## How Types Are Used in ROP Code

The implication of this whole restriction and resolution process is that a ROP might not know ahead of time what specific types it's going to use.

But the `shaderBuilder` has the final types for every ROP. So it generates a set of preprocessor macros like:

```glsl
#define someOperator1_COORD_TYPE_vec3
#define someOperator1_CoordT vec3
#define someOperator1_CONTEXT_TYPE_Context
#define someOperator1_ContextT Context
#define someOperator1_RETURN_TYPE_float
#define someOperator1_ReturnT float
```

The ROP's code can then use those to switch between different blocks of code, or to swap in placeholder types.

The original source code for an operator would look like this:

```glsl
ReturnT  thismap(CoordT p, ContextT ctx) {
  CoordT p2 = p * 2.;  // A variable using the same type as the coordinates.
  ReturnT res = inputOp1(p2, ctx);
  #ifdef THIS_RETURN_TYPE_Sdf  // Code that's only used when producing Sdf results
  res.color = vec4(1, 2, 3, 1);
  #endif
  return res;
}
```

Before being added to the final shader, those placeholders (`ReturnT`, `THIS_RETURN_TYPE_Sdf`) would be replaced with references to the generated macros (`someOperator1_ReturnT`, `someOperator1_RETURN_TYPE_Sdf`).
