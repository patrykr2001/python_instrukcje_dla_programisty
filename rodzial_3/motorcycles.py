motorcycles = ['homda', 'yamaha', 'suzuki']
print(motorcycles)

#motorcycles[0] = 'ducati'
#motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')

print(motorcycles)

del motorcycles[0]

print(motorcycles)

pooped_motorcycles = motorcycles.pop()
print(motorcycles)
print(pooped_motorcycles)
print(len(motorcycles))
