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
    counts[name] = counts.get(name, 0) + 1
print(counts)
