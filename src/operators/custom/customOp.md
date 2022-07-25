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

For multi-part parameters (`Par` styles including `XYZ`, `RGBA`, `UV` and `Float`/`Int` with more than 1 part) the
alias evaluates to a value of the relevant `vec*` type, with the name of the tuplet without any suffix, which combines
all of those parts (e.g. `THIS_Translate`).

## Parameters

* `Enable`
* `Codeheader`
* `Opglobals`
* `Initcode`
* `Function`: DAT with the main shader function.
* `Materialcode`: DAT with the optional material snippet.
* `Settingsheader`
* `Macrotable`
* `Buffertable`
* `Texturetable`
* `Librarynames`
  * `hg_sdf`
  * `raytkCommon`
  * `raytkSdf`
  * `raytkMaterial`
* `Typesheader`
* `Coordtype`: The type of coordinates that the op uses.
  * `auto`
  * `float`
  * `vec2`
  * `vec3`
* `Returntype`: The type of return value produced by the op.
  * `Sdf`
  * `float`
  * `vec4`
  * `Ray`
  * `Light`
* `Contexttype`: The type of return value produced by the op.
  * `auto`
  * `Context`: The most commonly used context type, used for the main scene graph.
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`
* `Paramsop`: The COMP that contains any custom parameters used by the op.
* `Createopglobals`
* `Createinit`
* `Createfunction`
* `Creatematerial`
* `Createparamsop`: Creates and attaches a new COMP for `Paramsop`, if there is none.
* `Createmissingparams`: Adds any parameters referred to by shader code that aren't defined in the `Paramsop`.
* `Removeunusedparams`: Removes any custom parameters from the `Paramsop` that aren't used in the shader code.
* `Autocreatemissingparams`: Automatically create custom parameters whenever shader code changes.
* `Useinputcoordtype`
* `Useinputreturntype`
* `Useinputcontexttype`

## Inputs

* `definition_in1`: 
* `definition_in2`: 
* `definition_in3`: 
* `definition_in4`: 