# INITIALIZING A SET

s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1, s2)

s = {5, 6, 5, 5, 6, 5, 6, 6, 5} # It automatically removes duplicate values
print(s)


# ADD AND UPDATE

s.add(1) # Add a single element
print(s)

s.update([9, 2, 0]) # Add multiple ones
print(s)


# REMOVE AND DISCARD

s.remove(1) # It raise a key error if the value doesn't exist

s.discard(2) # Won't raise any errors

print(s)


# UNION
# Elements that are common to all of them
 
sa = {1, 2, 3, 4}
sb = {3, 4, 5, 6}

print(sb.intersection(sa))


# DIFFERENCE
# Elements that are unique to the first set

print(sb.difference(sa))


# SYMMETRIC DIFFERENCE
# Elements that are not common between them

print(sb.symmetric_difference(sa))
