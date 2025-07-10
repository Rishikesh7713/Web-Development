tuple=()
tuple=('1','2','3')
print(tuple)
tuple=('text','Hello','no',123)
print(tuple['text'])
tuple=("abc",[8,6,7],(1,2,3))
print(tuple)
tuple=('n','a','m','e')
print(tuple[0])
print(tuple[4])
n_tuple=("abc",[8,6,7],(1,2,3))
print(n_tuple[0][2])
print(n_tuple[1][2])

print("Sliced :",tuple[123])

for i in (tuple):
    print("Hello",i)