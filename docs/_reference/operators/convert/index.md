---
layout: operatorCategory
title: Convert Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/convert/
cat:
  name: convert
  operators:
  - name: coordTo2D
  - name: coordTo3D
  - name: extrude
    summary: Creates a 3D SDF by extruding a 2D SDF along along an axis.
  - name: floatToSdf
    summary: Converts a float value field into an SDF.
  - name: floatToVector
    summary: Converts one or more float value field inputs into a single vector value
      field.
  - name: revolve
    summary: Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.
  - name: sdfToFloat
    summary: Converts an SDF into a float value field, based on the SDF surface distance.
  - name: sweep
    summary: Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D
      SDF.
  - name: vectorToFloat
    summary: Converts a vector value field to a float field using one part of the
      vector.
  summary: 'Operators that convert between different types of coordinates and

    return types (SDF, float/vector field, etc).'

---

# Convert Operators

Operators that convert between different types of coordinates and
return types (SDF, float/vector field, etc).
