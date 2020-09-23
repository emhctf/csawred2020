import subprocess


strings = subprocess.check_output("strings -n1 6A", shell=True)




print(''.join(q[0] for q in strings.split(b"\n")[:-1]))
