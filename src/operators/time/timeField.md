Field that produces time-based values, equivalent to a `timeline CHOP`.

This field ignores the provided coordinates and instead returns one of several different types of time-based values.

For timeline based values, output operators have a parameter that can specify the time reference operator. Otherwise it uses the timeline scoped to the COMP containing the scene.

## Parameters

* `Part`: Which type of time value to produce.
  * `seconds`: Timeline seconds.
  * `frame`: Timeline frame index.
  * `start`: The start frame of the timeline.
  * `end`: The end index of the timeline.
  * `fraction`: The fraction of the current frame within the timeline range.
  * `rate`: The timeline frame rate (which isn't necessarily the actual frame rate).
  * `bpm`: The timeline BPM.
  * `absFrame`: Absolute frame counting from when TouchDesigner started.
  * `absSeconds`: Absolute seconds counting from when TouchDesigner started.
  * `absStepFrames`: The number of absolute frames elapsed between the previous and current frame.
  * `absStepSeconds`: The number of absolute seconds elapsed between the previous and current frame.
* `Timesource`: Where to pull the time values from.
  * `global`: Global time is always the same throughout the whole shader scene graph.
  * `context`: Context time can be modified by downstream operators.