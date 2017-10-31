from cluster import Cluster
from node import Node


abel = Cluster('regneklynge.txt')


# For implementasjon som ikke leser av filnavn

# abel = Cluster(12)
# for i in range(650):
#     abel.insertNode(Node(64, 1))
#
# for i in range(16):
#     abel.insertNode(Node(1024, 2))


print(f'Noder med minst 32 GB minne: {abel.necessaryNodeMemoy(32)}')
print(f'Noder med minst 64 GB minne: {abel.necessaryNodeMemoy(64)}')
print(f'Noder med minst 1024 GB minne: {abel.necessaryNodeMemoy(1024)}')
print('')
print(f'Antall prosessorer: {abel.getProcessorTotal()}')
print(f'Antall racks: {abel.getRackTotal()}')
