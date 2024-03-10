# opDefinition

Generates the Definition for a ROP.

Each ROP contains one instance of this component, named `opDefinition`. The ROP sets the values of the parameters, which control how the definition is created.

## Type spec evaluation

Evaluates a type spec in an OP, expanding wildcards and inheriting input types or using fallback type.
Produces a list of 1 or more concrete type names, or a `@` reference to another op (for reverse inheritance).

Formats for spec input:

* `Type1 Type2`
* `*`
* `useinput|Type1 Type2`
* `useinput|*`
* `@some_op_name`

Output formats:
* 
* `Type1`
* `Type1 Type2`
* `@some_op_name`

These outputs are what appear in the generated definition tables passed between ops.
