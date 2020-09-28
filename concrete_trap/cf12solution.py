import angr, claripy


project = angr.Project("./concrete_trap")

initial_state = project.factory.entry_state()

sm = project.factory.simulation_manager(initial_state)

sm.explore(find=0x400dcf, avoid=0x400d05)


