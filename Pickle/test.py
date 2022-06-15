import pickle

# Data
data = [1,2,3]
a = 5
b = "Hello"

# Save data as a binary format
fh = open('numbers', 'wb')

# Pickele stuff
pickle.dump(data, fh)
pickle.dump(a, fh)
pickle.dump(b, fh)

fh.close()

# Tests
print(type(data))
print(data)
print('----')
print(type(a))
print(a)
print('----')
print(type(b))
print(b)
