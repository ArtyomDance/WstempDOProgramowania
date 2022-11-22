values = [10, 20, 30]
keys = ["dziesiench", "dwadziescza", "trzydziesci"]
D1 = dict(zip(keys, values))
print(D1)
D1 = {}
for i in range(len(keys)):
    D1[keys[i]] = values[i]
print(D1)


D2 = (dict(trzydziesci = 30, czterdziesci = 40, piecdziesat = 50))

D3 = {}
D3.update(D1)
D3.update(D2)
print(D3)
