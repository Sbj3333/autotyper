import timeit
a = []
for i in range(1000):
    a.append(i)

b = timeit.timeit(sorted(a), number = 1)
print(f"{b:.06f} secs.")