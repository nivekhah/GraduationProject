import os
import numpy as np
import matplotlib.pyplot as plt

file_q = open('../log/log_f3_q.txt')
file_dqn = open('../log/log_f3_dqn.txt')

full_local, full_offload, qlearn, dqn = [], [], [], []

for line in file_q:
    if 'Full_local' in line:
        full_local.append(float(line[12:]))
    if 'Full Offload' in line:
        full_offload.append(float(line[14:]))
    if 'Q-learning' in line:
        line = line.split(' ')
        qlearn.append(float(line[2]))
file_q.close()

tmp = -1
for line in file_dqn:
    if 'Namespace' in line:
        dqn.append(tmp)
        tmp = 0x3f3f3f3f
    if 'Namespace' not in line and 'Full' not in line and '[' not in line:
        tmp = min(tmp, float(line))
file_dqn.close()
dqn.append(tmp)
dqn.pop(0)
bn = [ i*200 for i in range(1, 6)]

print(full_local)
print(full_offload)
print(qlearn)

plt.plot(bn, full_local, '^-', linewidth=0.4, label='Full Local')
plt.plot(bn, full_offload,'v-', linewidth=0.4, label='Full Offload')
plt.plot(bn, qlearn, '<-', linewidth=0.4, label='Q-learning')
plt.plot(bn, dqn, '>-', linewidth=0.4, label='DQN')
plt.grid(True)

plt.xlabel('data size of task(kbits)')
plt.ylabel('Sum Cost')
plt.legend(loc='upper left')
plt.show()
