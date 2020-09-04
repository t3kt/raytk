#ifndef THIS_USE_LENGTH

#define thismap(p, ctx) inputOp1(p, ctx).THIS_PART

#else

#define thismap(p, ctx) length(inputOp1(p, ctx).THIS_PARTS)

#endif

