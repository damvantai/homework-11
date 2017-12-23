import re
from priodict import priorityDictionary


class Egde(object):
	"""docstring for Egde"""
	def __init__(self, start, end):
		super(Egde, self).__init__()
		self.start = start
		self.end = end
		self.dist = 1


class Node(object):
	"""docstring for Node"""
	def __init__(self, name):
		super(Node, self).__init__()
		self.name = name
		self.neighbor = set()

	def add_neighbor(self, other):
		self.neighbor.add(other)
		other.neighbor.add(self)
		

def different(a,b):
	count = sum(1 for a, b in zip(a, b) if a != b)
	return count

def connected_components(nodes):
	result = []
	num = 0
	nodes = set(nodes)

	while nodes:
		n = nodes.pop()
		group = set()
		group.add(n)
		queue = [n]

		while queue:
			n = queue.pop(0)
			neighbor = n.neighbor
			neighbor.difference_update(group)
			nodes.difference_update(neighbor)
			group.update(neighbor)
			queue.extend(neighbor)

		result.append(group)
		num += 1
	return num
	#return result


def Dijkstra(G, start, end=None):
    D = {}  # dictionary of final distances
    P = {}  # dictionary of predecessors
    Q = priorityDictionary()  # estimated distances of non-final vertices
    Q[start] = 0

    for v in Q:
        D[v] = Q[v]
        if v == end:
            break

        for w in G[v]:
            vwLength = D[v] + G[v][w]
            if w in D:
                if vwLength < D[w]:
                    raise ValueError("Dijkstra: found better path to already-final vertex")
            elif w not in Q or vwLength < Q[w]:
                Q[w] = vwLength
                P[w] = v

    return (D, P)


def shortestPath(G, start, end):
    D, P = Dijkstra(G, start, end)
    Path = []
    while 1:
        Path.append(end)
        if end == start:
            break
        end = P[end]
    Path.reverse()
    return Path


######################
print "Reading graph ... "

f = open("word2.txt")
a = f.read()

#tao mang gom cac tu
words = re.sub("[^\w]", " ",  a).split()

#tao cac node trong do thi
graph = []
for i in range(len(words)):
	x = Node(words[i])
	graph.append(x)
G = {}

#tao danh sach cac canh
edge = []

#them hang xom cho moi node va them vao danh sach canh
for i in range(len(words)):
	G[words[i]] = {}

for i in range(len(words)):
	for j in xrange(i+1,len(words)):
		if different(words[i],words[j]) == 1:
			G[words[i]][words[j]] = 1
			G[words[j]][words[i]] = 1
			graph[i].add_neighbor(graph[j])
			x = Egde(graph[i].name,graph[j].name)
			edge.append(x)
while 1:
	option = int(raw_input("Chon:\n1.Dem so thanh phan lien thong \n2.Tim duong ngan nhat\n3.Ket thuc\n"))
	if option == 1:
		print "So thanh phan lien thong la: ",connected_components(graph)
	elif option == 2:
		s = raw_input("Chon diem dau:\n")
		t = raw_input("Chon diem cuoi:\n")
		print "Duong di ngan nhat la:"
		print(shortestPath(G,s,t))
	elif option == 3:
		exit()
		
# for i in range(len(graph)):
# 	print graph[i].name + " and neighbor:"
# 	for x in graph[i].neighbor:
# 		print x.name

# number = 1
# for components in connected_components(graph):
#     names = sorted(node.name for node in components)
#     names = ", ".join(names)
#     print "Group #%i: %s" % (number, names)
#     number += 1