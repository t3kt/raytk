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
    summary: Converts a 3D (or 1D) operator to work in a 2D plane on the chosen axes.
  - name: coordTo3D
    summary: Converts a 2D (or 1D) operator to work in a 3D context.
  - name: crossSection
    summary: Takes a 3D (or 2D) operator and take a cross section of it across a plane
      or a single axis.
  - name: extrude
    shortcuts:
    - ext
    summary: Creates a 3D SDF by extruding a 2D SDF along along an axis.
    thumb: assets/images/reference/operators/convert/extrude_thumb.png
  - name: extrudeLine
    status: beta
    summary: Extrudes a 2D SDF cross-section into a 3D volume, like the extrude operator,
      but between two points.
  - name: floatToSdf
    summary: Converts a float value field into an SDF.
  - name: floatToVector
    summary: Converts one or more float value field inputs into a single vector value
      field.
  - name: projectPlane
    summary: Takes a 1D or 2D operator and converts it to a 3D operator by mapping
      it to a plane within 3D space.
  - name: projectPolar
    summary: Projects coordinates into various types of polar spaces.
  - name: revolve
    summary: Creates a 3D SDF by revolving a 2D cross-section SDF around an axis.
    thumb: assets/images/reference/operators/convert/revolve_thumb.png
  - name: sampleAlongLine
    status: beta
    summary: Samples a 2D/3D input along a single line, producing a 1D function.
  - name: sweep
    summary: Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D
      SDF.
    thumb: assets/images/reference/operators/convert/sweep_thumb.png
  - name: vectorToFloat
    summary: Converts a vector value field to a float field, e.g. using one part of
      the vector.
  summary: 'Operators that convert between different types of coordinates and

    return types (SDF, float/vector field, etc).'

---

# Convert Operators

Operators that convert between different types of coordinates and
return types (SDF, float/vector field, etc).
