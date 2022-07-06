# opElement

Properties of a reusable element within a ROP.

This component is just a collection of parameters, without
any actual implementation.

The opDefinition looks for these within the host ROP and
pulls properties from them.

Provided properties include:

* Paramgrouptable - Parameters used by the element, matching the same format
  as the equivalent table in opDefinition's settings.
* Macrotable - Macros produced by the element.
* Placeholder1/2 - Placeholder text that gets replaced in the ROP's code. E.g. `BODY();`
* Code1/2 - DAT with code that gets swapped in.