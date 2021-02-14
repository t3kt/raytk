# multiInputHandler

Process a variably sized group of definition inputs within a ROP.

It collects the inputs that have connected definitions and renumbers them if some are not connected.
For example, if inputs 2 and 4 are connected, they are renumbered to 1 and 2.
It also generates a table of macros that the containing ROP can use to vary behavior based on the number
of connected inputs (`THIS_INPUT_COUNT`).
