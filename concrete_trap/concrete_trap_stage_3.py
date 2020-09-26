import angr
import claripy
from pprint import pprint

proj = angr.Project("./concrete_trap", main_opts={'base_addr': 0})
print(proj.factory.block(0xb3b).pp())


state = proj.factory.call_state(0xb3b)#, claripy.BVS("first", 32), claripy.BVS("second", 32), claripy.BVS("third", 32), claripy.BVS("fourth", 32), claripy.BVS("fifth", 32))

simgr = proj.factory.simulation_manager(state)
simgr.explore(find=lambda s: s.addr == 0xc6b and s.regs.rax == 1)

pprint(vars(simgr))
pprint(vars(simgr.deadended[1]))
print(simgr.deadended[1].regs.rax)
print(simgr.deadended[1].stack_read(-0x10, 4, True))
print(simgr.deadended[1].stack_read(-0x14, 4, True))
print(simgr.deadended[1].stack_read(-0x18, 4, True))
print(simgr.deadended[1].stack_read(-0x1c, 4, True))
print(simgr.deadended[1].stack_read(-0x20, 4, True))
print(simgr.deadended[1].stack_read(-0x10, 4, False))
print(simgr.deadended[1].stack_read(-0x14, 4, False))
print(simgr.deadended[1].stack_read(-0x18, 4, False))
print(simgr.deadended[1].stack_read(-0x1c, 4, False))
print(simgr.deadended[1].stack_read(-0x20, 4, False))