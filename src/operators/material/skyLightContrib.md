A material element that acts as a basic pseudo directional light.

It applies lighting based on the direction that surfaces are facing.
Unlike the main lighting system, it does not support shadows or other lighting behavior.
It is a cheap way to add some secondary coloration to surfaces.

It is equivalent to the sky lighting feature in `basicMat`.

## Parameters

* `Color`
* `Level`
* `Dir`: The direction from which the "light" comes from.
* `Usecolor`: Whether to produce color or just a brightness value.
