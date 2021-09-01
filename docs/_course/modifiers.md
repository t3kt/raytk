The filters that we've discussed so far are based around changing the coordinates that their inputs use. Most filters fall into that category, but there are a few which instead modify the answers produced by their input.

# The `round` operator

The `round` operator expands or contracts the surface produced by its input.It does this by adjusting the distance that's reported in the SDF result, either increasing it (to expand the surface) or decreasing it (to contract it).

![https://iquilezles.org/www/articles/distfunctions/gfx43.png](https://iquilezles.org/www/articles/distfunctions/gfx43.png)

[https://iquilezles.org/www/articles/distfunctions/distfunctions.htm](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm)

# The `onion` operator

The `onion` operator converts a solid SDF shape to a hollow shell of the surface.

To see the result, you'll need to cut through the shell with an operator like `knife` or `slice`. 

Similar to `round`, the `onion` operator works by adjusting the distance that's reported in the SDF result. For points close to the surface, it will report those as "inside" and anything that isn't close to the surface, even if that used to be "inside" will be reported as "outside".

![https://iquilezles.org/www/articles/distfunctions/gfx44.png](https://iquilezles.org/www/articles/distfunctions/gfx44.png)

[https://iquilezles.org/www/articles/distfunctions/distfunctions.htm](https://iquilezles.org/www/articles/distfunctions/distfunctions.htm)

# The `assignColor` and `assignUV` operators

These operators don't change the surface directly. Instead that change attributes of it which other operators such as materials can use.

They're like the attribute parts of `Point SOP`/ `Primitive SOP`/ etc, or the `Texture SOP`.

Attributes like color and UV are primarily used by materials, which will be covered later.
