---
layout: operatorCategory
title: Utility Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/utility/
cat:
  name: utility
  operators:
  - name: extractIteration
    status: beta
    summary: 'A field that returns the current iteration, from a downstream

      operator.'
  - name: injectGlobalPosition
    summary: Calls its input using the untransformed global position.
  - name: injectObjectId
    status: beta
    summary: 'Assigns an arbitrary value to the objectId field of an SDF, which can
      later

      be extracted from rendered output.'
  summary: Advanced operators that change how ROP chains behave.

---

# Utility Operators

Advanced operators that change how ROP chains behave.
