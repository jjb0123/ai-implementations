expand_count = 0

#Defining the expand function
def expand(node, _map):
	global expand_count
	print(node)
	expand_count = expand_count + 1
	return [next for next in _map[node] if _map[node][next] is not None]
