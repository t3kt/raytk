---
layout: page
title: ROP Structure
nav_order: 0
---

# ROP Structure

ROPs are the core of the RayTK library. A ROP is essentially some chunks of GLSL code, and some metadata.

A ROP is a COMP that generates a Definition, which is output as a DAT table.

## ROP Definitions

Each ROP contributes one row to a DAT table that also contains rows for all the ROPs that are upstream.

A definition contains:

* `name`: globally unique name for the ROP, based on the path.
* `path`: path to the ROP.
* `opType`: identifies the type of ROP, and is derived from the path of the clone master used to create a ROP.
* `opVersion`: version of that particular type of ROP.
* `functionPath`: path to a text DAT containing the main chunk of code.
* `paramSource`: path to a CHOP containing the values of the parameters for the ROP.
* `paramTable`: path to a table listing the globally unique names of the ROP's individual parameters.
* `paramTupletTable`: path to a table with details about the parameters, organized into tuplets.
* `materialTable`: path to a table listing out the material identifiers used by the ROP.
* `macroTable`: path to a table with preprocessor macros used by the ROP's code.
* `textureTable`: path to a table listing out texture sources used by the ROP.
* `libraryNames`: names or paths of shared libraries that the ROP depends on.
* `initPath`: path to a text DAT with initialization code that the ROP needs to run before its other code is used.
* `opGlobalsPath`: path to a text DAT with declarations of global variables used by the ROP (generally initialized using the code from the `initPath`).
* `coordType`: the type of coordinates that the ROP's function accepts.
* `returnType`: the type of value the that the ROP's function returns.
* `contextType`: the type of context that the ROP's function expects along with the coordinates.
* `inputName1` - `inputName4`: the names of other ROPs that this ROP's function calls.


