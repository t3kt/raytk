---
layout: page
title: Utility Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/utility/
---

# Utility Operators

Advanced operators that change how ROP chains behave.

* [`extractIteration`](extractIteration/) - A field that returns the current iteration, from a downstream
operator. *beta*{: .label .status-beta }
* [`injectGlobalPosition`](injectGlobalPosition/) - Calls its input using the untransformed global position.
* [`injectObjectId`](injectObjectId/) - Assigns an arbitrary value to the objectId field of an SDF, which can later
be extracted from rendered output. *beta*{: .label .status-beta }
