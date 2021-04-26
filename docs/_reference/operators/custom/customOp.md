---
layout: operator
title: customOp
parent: Custom Operators
grand_parent: Operators
permalink: /reference/operators/custom/customOp
redirect_from:
  - /reference/opType/raytk.operators.custom.customOp/
op:
  category: custom
  detail: "When created, the operator will also create several docked operators that\
    \ are used\nto provide define behavior.\n\n## Shader Code\n\nThe `Function` code\
    \ is the main block that defines the behavior of the op. It contains the definition\
    \ of a function\nnamed `thismap`. This function must take two parameters: a coordinate\
    \ named `p`, and a context value named `ctx`. The\nfunction returns some supported\
    \ type of value.\n\n### Type Aliases\n\nWithin shader code, `CoordT`, `ContextT`,\
    \ and `ReturnT` are replaced with the actual types that the OP is using. This\n\
    allows you to define an OP as using whatever kind of coordinates its input uses\
    \ (e.g. `vec2` or `vec3`) without having\nto change the code.\n\n```glsl\nReturnT\
    \ thismap(CoordT p, ContextT ctx)  {\n  // custom code goes here\n}\n```\n\nAlternatively\
    \ if you know that the ROP will always use some specific type, you can use that\
    \ explicit type, as long as\nthat type is supported for that kind of use.\n\n\
    ```glsl\nSdf thismap(vec2 p, ContextT ctx) {\n  return createSdf(length(p) - THIS_Radius);\n\
    }\n```\n\n### Prefixes and Uniqueness\n\nAny functions, global variables, and\
    \ macros defined in the shader code will be inserted into the generated shader.\
    \ This\nmeans that they cannot conflict with things defined in any other OP or\
    \ in the toolkit's libraries. This can be a problem\nwhen copying and pasting\
    \ code from Shadertoy or elsewhere.\n\nTo avoid this, when defining any functions,\
    \ global variables, or macros, use the prefix `THIS_`, which gets replaced\nwith\
    \ a unique op-specific prefix.\n\n```glsl\nfloat THIS_helperFunc(vec2 foo) {\n\
    \  return foo.x * 12 + foo.y;\n}\n#define THIS_helperMacro    1.2345\nfloat THIS_globalVar\
    \ = 3;\n\nReturnT thismap(CoordT p, ContextT ctx) {\n  if (p.y > THIS_globalVar)\
    \ {\n    THIS_globalVar = p.y;\n  }\n  return vec4(THIS_helperFunc(p.xy), THIS_helperMacro,\
    \ THIS_globalVar, 0.);\n}\n```\n\n### Using Inputs\n\nROPs connected to the inputs\
    \ of the `customOp` are available to be called as functions named `inputOp1`,\
    \ `inputOp2`,\netc. When calling these, pass in some type of coordinate value\
    \ and the `ctx` context value passed into the `thismap`\nfunction.\n\n```\nReturnT\
    \ thismap(CoordT p, ContextT ctx) {\n    return inputOp1(p.xz + vec2(THIS_Foo,\
    \ 1.0), ctx);\n}\n```\n\n### More Information About Shader Code\n\nSee [Writing\
    \ ROP Code] for more details about ROP code. Note that some features described\
    \ there may not be available for\nuse with `customOp`.\n\n[Writing ROP Code]:\
    \ /raytk/development/rop-code\n\n## Custom Parameters\n\nIn order to control the\
    \ behavior of the op, you can create custom parameters on the associated \"params\"\
    \ COMP which is\ncreated along with the `customOp`. These parameters can be used\
    \ in the shader code as variables named like\n`THIS_Paramname`.\n\nThe `customOp`'s\
    \ \"Tools\" parameter page includes several pulse parameters that can help automatically\
    \ manage these\ncustom parameters based on the shader code. For example, 'Createmissingparams'\
    \ will add new custom parameters that are\nreferenced in the shader code but are\
    \ missing on the \"params\" COMP.\n\nFor multi-part parameters (`Par` styles including\
    \ `XYZ`, `RGBA`, `UV` and `Float`/`Int` with more than 1 part), you\ncan either\
    \ refer to the individual parts (such as `THIS_Sizex`), or to the tuplet name\
    \ which represents a value of the\nrelevant `vec*` type, which combines all of\
    \ those parts (e.g. `THIS_Size` could be a `vec3`)."
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in1
    name: definition_in1
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in2
    name: definition_in2
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in3
    name: definition_in3
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in4
    name: definition_in4
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
  name: customOp
  opType: raytk.operators.custom.customOp
  parameters:
  - label: Enable
    name: Enable
  - label: Code
    name: Codeheader
  - label: Op Globals
    name: Opglobals
  - label: Init Code
    name: Initcode
  - label: Function
    name: Function
    summary: DAT with the main shader function.
  - label: Material Code
    name: Materialcode
    summary: DAT with the optional material snippet.
  - label: Settings
    name: Settingsheader
  - label: Macro Table
    name: Macrotable
  - label: Buffer Table
    name: Buffertable
  - label: Texture Table
    name: Texturetable
  - label: Library Names
    menuOptions:
    - label: hg_sdf
      name: hg_sdf
    - label: raytkCommon
      name: raytkCommon
    - label: raytkSdf
      name: raytkSdf
    - label: raytkMaterial
      name: raytkMaterial
    name: Librarynames
  - label: Types
    name: Typesheader
  - label: Coord Type
    menuOptions:
    - description: Use whatever type of coordinates the first input uses, or `vec3`
        if the first input is not connected.
      label: Use Input
      name: useinput
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 3D
      name: vec3
    - label: 2D
      name: vec2
    name: Coordtype
    summary: The type of coordinates that the op uses.
  - label: Return Type
    menuOptions:
    - description: Use whatever type of return value the first input uses, or `Sdf`
        if the first input is not connected.
      label: Use Input
      name: useinput
    - label: SDF Result
      name: Sdf
    - label: Float
      name: float
    - label: Vector4
      name: vec4
    - label: Ray
      name: Ray
    - label: Light
      name: Light
    name: Returntype
    summary: The type of return value produced by the op.
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - description: Use whatever type of context the first input uses, or `Context`
        if the first input is not connected.
      label: Use Input
      name: useinput
    - description: The most commonly used context type, used for the main scene graph.
      label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
    summary: The type of return value produced by the op.
  - label: Params OP
    name: Paramsop
    summary: The COMP that contains any custom parameters used by the op.
  - label: Create Op Globals
    name: Createopglobals
  - label: Create Init
    name: Createinit
  - label: Create Function
    name: Createfunction
  - label: Create Material
    name: Creatematerial
  - label: Create Params OP
    name: Createparamsop
    summary: Creates and attaches a new COMP for `Paramsop`, if there is none.
  - label: Create Missing Params
    name: Createmissingparams
    summary: Adds any parameters referred to by shader code that aren't defined in
      the `Paramsop`.
  - label: Remove Unused Params
    name: Removeunusedparams
    summary: Removes any custom parameters from the `Paramsop` that aren't used in
      the shader code.
  - label: Auto Create Missing Params
    name: Autocreatemissingparams
    summary: Automatically create custom parameters whenever shader code changes.
  status: beta
  summary: A custom operator that integrates blocks of custom shader code into a RayTK
    network.

---


A custom operator that integrates blocks of custom shader code into a RayTK network.

When created, the operator will also create several docked operators that are used
to provide define behavior.

## Shader Code

The `Function` code is the main block that defines the behavior of the op. It contains the definition of a function
named `thismap`. This function must take two parameters: a coordinate named `p`, and a context value named `ctx`. The
function returns some supported type of value.

### Type Aliases

Within shader code, `CoordT`, `ContextT`, and `ReturnT` are replaced with the actual types that the OP is using. This
allows you to define an OP as using whatever kind of coordinates its input uses (e.g. `vec2` or `vec3`) without having
to change the code.

```glsl
ReturnT thismap(CoordT p, ContextT ctx)  {
  // custom code goes here
}
```

Alternatively if you know that the ROP will always use some specific type, you can use that explicit type, as long as
that type is supported for that kind of use.

```glsl
Sdf thismap(vec2 p, ContextT ctx) {
  return createSdf(length(p) - THIS_Radius);
}
```

### Prefixes and Uniqueness

Any functions, global variables, and macros defined in the shader code will be inserted into the generated shader. This
means that they cannot conflict with things defined in any other OP or in the toolkit's libraries. This can be a problem
when copying and pasting code from Shadertoy or elsewhere.

To avoid this, when defining any functions, global variables, or macros, use the prefix `THIS_`, which gets replaced
with a unique op-specific prefix.

```glsl
float THIS_helperFunc(vec2 foo) {
  return foo.x * 12 + foo.y;
}
#define THIS_helperMacro    1.2345
float THIS_globalVar = 3;

ReturnT thismap(CoordT p, ContextT ctx) {
  if (p.y > THIS_globalVar) {
    THIS_globalVar = p.y;
  }
  return vec4(THIS_helperFunc(p.xy), THIS_helperMacro, THIS_globalVar, 0.);
}
```

### Using Inputs

ROPs connected to the inputs of the `customOp` are available to be called as functions named `inputOp1`, `inputOp2`,
etc. When calling these, pass in some type of coordinate value and the `ctx` context value passed into the `thismap`
function.

```
ReturnT thismap(CoordT p, ContextT ctx) {
    return inputOp1(p.xz + vec2(THIS_Foo, 1.0), ctx);
}
```

### More Information About Shader Code

See [Writing ROP Code] for more details about ROP code. Note that some features described there may not be available for
use with `customOp`.

[Writing ROP Code]: /raytk/development/rop-code

## Custom Parameters

In order to control the behavior of the op, you can create custom parameters on the associated "params" COMP which is
created along with the `customOp`. These parameters can be used in the shader code as variables named like
`THIS_Paramname`.

The `customOp`'s "Tools" parameter page includes several pulse parameters that can help automatically manage these
custom parameters based on the shader code. For example, 'Createmissingparams' will add new custom parameters that are
referenced in the shader code but are missing on the "params" COMP.

For multi-part parameters (`Par` styles including `XYZ`, `RGBA`, `UV` and `Float`/`Int` with more than 1 part), you
can either refer to the individual parts (such as `THIS_Sizex`), or to the tuplet name which represents a value of the
relevant `vec*` type, which combines all of those parts (e.g. `THIS_Size` could be a `vec3`).