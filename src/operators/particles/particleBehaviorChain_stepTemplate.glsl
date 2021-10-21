if (haltOnDeath&&!isAlive(part)) {return part;}
ctx.particle = part;
part = inputOp$(part.pos, ctx);