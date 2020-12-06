# opDefinition

Generates the Definition for a ROP.

Each ROP contains one instance of this component, named `opDefinition`. The ROP sets the values of the parameters, which control how the definition is created.

* `Enable` - Enables or disables the op. Switching this to false will totally bypass the ROP. As far as anything downstream is concerned, this ROP does not exist when it this is false.
