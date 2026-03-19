data = [
    {"anun": "C1", "t1": 25, "t2": 200, "t3": 50, "label": 1},
    {"anun": "C2", "t1": 30, "t2": 180, "t3": 90, "label": 0},
    {"anun": "C3", "t1": 22, "t2": 150, "t3": 30, "label": 1},
    {"anun": "C4", "t1": 40, "t2": 300, "t3": 120, "label": 0},
    {"anun": "C5", "t1": 35, "t2": 220, "t3": 70, "label": 1},
    {"anun": "C6", "t1": 28, "t2": 250, "t3": 60, "label": 1},
    {"anun": "C7", "t1": 50, "t2": 400, "t3": 200, "label": 0},
    {"anun": "C8", "t1": 45, "t2": 350, "t3": 150, "label": 0},
    {"anun": "C9", "t1": 27, "t2": 160, "t3": 40, "label": 1},
    {"anun": "C10", "t1": 33, "t2": 210, "t3": 80, "label": 1},
    {"anun": "C11", "t1": 31, "t2": 190, "t3": 95, "label": 0},
    {"anun": "C12", "t1": 29, "t2": 230, "t3": 55, "label": 1},
    {"anun": "C13", "t1": 42, "t2": 280, "t3": 130, "label": 0},
    {"anun": "C14", "t1": 36, "t2": 240, "t3": 75, "label": 1},
    {"anun": "C15", "t1": 38, "t2": 260, "t3": 100, "label": 0},
    {"anun": "C16", "t1": 26, "t2": 170, "t3": 45, "label": 1}
]

test_data = [
    {"anun": "T1", "t1": 27, "t2": 160, "t3": 40},
    {"anun": "T2", "t1": 33, "t2": 210, "t3": 80},
    {"anun": "T3", "t1": 31, "t2": 190, "t3": 95},
    {"anun": "T4", "t1": 29, "t2": 230, "t3": 55}
]

y = [1, 1, 0, 1]

K = 3

def euclidean_distance(p1, p2):
    d1 = (p1["t1"] - p2["t1"]) ** 2
    d2 = (p1["t2"] - p2["t2"]) ** 2
    d3 = (p1["t3"] - p2["t3"]) ** 2
    return (d1 + d2 + d3) ** 0.5

def predict(test_point):
    distances = []
    for train_point in data:
        dist = euclidean_distance(test_point, train_point)
        label = train_point["label"]
        distances.append({"dist": dist, "label": label})

    distances.sort(key=lambda x: x["dist"])

    neighbors = [distances[i]["label"] for i in range(K)]

    if neighbors.count(1) > neighbors.count(0):
        return 1
    else:
        return 0

print("Գուշակման արդյունքներ")
print("-------------------")
i = 0
for t in test_data:
    result = predict(t)
    print(f"{t['anun']} → {result} (իրական արժեքը {y[i]})")
    i += 1
print("\nՆոր հաճախորդի մուտքագրում")
print("-------------------")
anun = input("Անուն։ ")
t1 = int(input("Տարիք(20-50)"))
t2 = int(input("եկամուտ։ (150-400 ՀՀ դրամ)"))
t3 = int(input("Պարտք (30-200  ՀՀ դրամ։)"))

new_point = {"anun": anun, "t1": t1, "t2": t2, "t3": t3}
prediction = predict(new_point)

if prediction == 1:
    print(f"{anun} → Կփակի պարտքը(1)")
else:
    print(f"{anun} → Չի փակի պարտքը(0)")
