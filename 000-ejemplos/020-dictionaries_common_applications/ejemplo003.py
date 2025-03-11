counts = dict()
names = [
    "daniel",
    "alberto",
    "macarena",
    "alberto",
    "macarena",
    "macarena",
    "daniel",
    "alberto",
    "macarena",
    "alberto",
    "macarena",
    "macarena",
    "daniel"
]
for name in names :
    if name not in counts :
        counts[name] = 1
    else :
        counts[name] = counts[name] + 1
print(counts)
