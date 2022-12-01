def splitList(g, s):
	r = []
	for i in g:
		if i != s:
			r.append(i)
			continue
		yield r
		r = []
	yield r

with open("input", "r") as f:
	print(sum(sorted(map(lambda x: sum(map(int, x)),splitList(map(str.rstrip,f), "")), reverse=True)[:3]))
