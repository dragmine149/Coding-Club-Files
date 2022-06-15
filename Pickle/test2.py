import pickle

# Open binary file and convert it to readable format.
fh = open('numbers', 'rb')
data = pickle.load(fh)
a = pickle.load(fh)
b = pickle.load(fh)
fh.close()

# tests
print(data)
print(type(data))
print('----')
print(a)
print(type(a))
print('----')
print(b)
print(type(b))
