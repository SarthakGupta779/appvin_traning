h=list(map(lambda x:x,'sarthak'))
print(h)

#
l=[x for x in range(50) if x%2==0 if x%5==0]
print(l)

#
mat=[[1,2],[3,4],[5,6],[7,8]]
trans=[[row[i] for row in mat]for i in range(2)]
print(trans)