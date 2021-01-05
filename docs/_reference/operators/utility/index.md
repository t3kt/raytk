---
layout: operatorCategory
title: Utility Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/utility/
cat:
  name: utility
  summary: |
    Advanced operators that change how ROP chains behave.
  operators:
    - op:
      name: extractIteration
      summary: A field that returns the current iteration, from a downstream operator.
      status: beta
    - op:
      name: injectGlobalPosition
      summary: Calls its input using the untransformed global position.
    - op:
      name: injectObjectId
      summary: Assigns an arbitrary value to the objectId field of an SDF, which can later be extracted from rendered output.
      status: beta

---

# Utility Operators

Advanced operators that change how ROP chains behave.
