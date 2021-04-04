Impulse functions that are useful as trigger patterns or animation envelopes.

Based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).

## Parameters

* `Function`
  * `exponential`: Great for triggering behaviours or making envelopes for music or animation, and for anything that grows fast and then slowly decays.
  * `sustained`: Similar to exponential, but it allows for control on the width of attack and the release independently.
  * `quad`: Simple impulse with configurable falloff.
  * `poly`: Generalized form of quad impulse for various different degrees of polynomials.
* `Attack`
* `Release`
* `Falloff`
* `Polydegree`
* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`