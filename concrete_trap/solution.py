import angr
import claripy

OFFSET = 0x400000

BASE = 0x1000 + OFFSET
FUNC = 0x1145 + OFFSET
FIND = 0x1286 + OFFSET
AVID = 0x127a + OFFSET

proj = angr.Project("./stage3final", main_opts={'base_addr': BASE})


state = proj.factory.call_state(FUNC, claripy.BVS("first", 32), claripy.BVS("second", 32), claripy.BVS("third", 32), claripy.BVS("fourth", 32), claripy.BVS("fifth", 32))

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=FIND, avoid=AVID)


print(proj.factory.block(OFFSET + 0x1140).vex.pp())
print(simgr.errored)


