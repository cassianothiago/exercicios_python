
print('='*120)
a=[1,2,3,4,5,6,7,8,9]
print(a)
print(max(a))
print(min(a))
print(sum(a))
print(sum(a)/len(a))
x=(sum(a))
y=(len(a))
z=x/y
print(z)

print('='*120)
b=['a','b','c','d','e','f']
print(b[1:3])
print(b[:4])
print(b[3:])
print(b[:])
print(b[0:6])

print('='*120)
frutas=['banana','maca','cereja']
frutas[0]='pera'
frutas[-1]='laranja'
print(frutas)

print('='*120)
c=['flor','azul',[1,'casa']]
print(c)
c[2][1]='escola'
print(c)

print('='*120)
d=['a','b','c','d','e','f']
print(d)
d[1:3]=['x','y']
print(d)

print('='*120)
e=['a','b','c','d','e','f']
print(e)
print(len(e))
e[1:3]=[]
print(e)
print(len(e))

print('='*120)
f=['a','b','c']
print(f)
f[1:1]=['b','c']
print(f)
f[1:1]=['x']
print(f)
f[4:4]=['e']
print(f)

print('='*120)
g=['um','dois','tres']
del g[1]
print(g)
h=['a','b','c','d','e','f']
del h[1:5]
print(h)

print('='*120)
i=[81,82,83]
print(i)
i.append(5)
print(i)

print('='*120)
j=[84,81,82,83]
print(j)
j.sort()
print(j)
j.sort(reverse=True)
print(j)

print('='*120)
h=[1,2,3,4,5,6,7,8,9]
print(h)
print(h.index(4))

print('='*120)
i=[88,81,82,83]
print(i)
i.insert(1,100)
print(i)

print('='*120)
l=[88,81,82,83,88,85,88,86]
print(l)
print(l.count(88))

print('='*120)
m=[88,81,82,83,84,85,88,86]
print(m)
m.pop(0)
print(m)
m.pop()
print(m)
