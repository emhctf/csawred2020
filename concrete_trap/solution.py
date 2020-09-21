import angr
proj = angr.Project('concrete_trap')
state = proj.factory.call_state(0x400b3b)
state.regs.rbp = 0x100
simgr = proj.factory.simgr(state)
simgr.explore()
simgr.deadended[1].stack_read(-0x10, 4, False)
a = simgr.deadended[1].stack_read(-0x20, 4, False)
print(a)
