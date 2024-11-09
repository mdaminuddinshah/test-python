a = 'good'
b = 'nice'
c = 'great'
d = 'cool'
e = 12
f = 10 
g = 7

# f-string
print(f"he is really {d} and {a}")    # => he is really cool and good

# .format()
print("why he so {} and {}" .format(b, c))  # => why he so nice and great

# commas
print(c, "person always", d)  # => great person always cool

# concatenate 
print(d + " stuff always " + b + ' to know')  # => cool stuff always nice to know