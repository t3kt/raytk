---
layout: page
title: Utility Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/utility/
---

Advanced operators that change how ROP chains behave.

* [`extractDebugValues`](extractDebugValues/) - 
* [`extractIteration`](extractIteration/) - A field that returns the current iteration, from a downstream
operator.
* [`injectGlobalPosition`](injectGlobalPosition/) - Calls its input using the untransformed global position.
* [`injectObjectId`](injectObjectId/) - Assigns an arbitrary value to the objectId field of an SDF, which can later
be extracted from rendered output.
