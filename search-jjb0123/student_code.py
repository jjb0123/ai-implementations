import collections
from importlib.resources import path
from queue import PriorityQueue
from time import time
from expand import expand


def a_star_search (dis_map, time_map, start, end):
	queue = PriorityQueue()
	queue.put([dis_map[start][end], [start]])
	covered = set()

	while queue:
		dis,path = queue.get()
		node = path[-1]
		if node not in covered:
			covered.add(node)
			if path[-1] == end:
				return path
			for num in expand(node, time_map):
				new_path = path + [num]
				d_0 = dis_map[node][end]
				d_1 = dis_map[num][end]
				tim = time_map[node][num]
				queue.put([dis - d_0 + d_1 + tim, new_path])
	return False 
			


def depth_first_search(time_map, start, end):
	stck = []
	stck.append([start])

	while stck:
		new_path = stck.pop()
		new_node = new_path[-1]
		if new_node == end:
			return new_path
		for num in expand(new_node, time_map):
			new_ = new_path + [num]
			stck.append(new_)
	return False 
			




def breadth_first_search(time_map, start, end):
	covered = set()
	queue = collections.deque()
	queue.append([start])

	while queue:
		new_path = queue.popleft()
		new_node = new_path[-1]
		if new_node not in covered:
			covered.add(new_node)
			if new_node == end:
				return new_path
			for num in expand(new_node, time_map):
				new = new_path + [num]
				queue.append(new)
	return False

