data = [
    [1, 1, 1, 0, 1],
    [0, 1, 1, 1, 1],
    [1, 0, 1, 1, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

def gini_formula(data, f_i):
    total = len(data)
    count_x0 = 0
    count_x1 = 0
    y0_x0 = 0
    y1_x0 = 0
    y0_x1 = 0
    y1_x1 = 0
    for row in data:
        x = row[f_i]
        y = row[-1]
        if x == 0:
            count_x0 += 1
            if y == 0:
                y0_x0 +=1
            else:
                y1_x0 += 1
        else:
            count_x1 += 1
            if y == 0:
                y0_x1 += 1
            else:
                y1_x1 +=1
    p_x0 = count_x0/total
    p_x1 = count_x1/total
    if count_x0 ==0:
        p_y0_x0 = 0
        p_y1_x0 = 0
    else:
        p_y0_x0 = y0_x0/count_x0
        p_y1_x0 = y1_x0/count_x0
    if count_x1 == 0:
        p_y1_x1 = 0
        p_y0_x1 = 0
    else:
        p_y0_x1 = y0_x1/count_x1
        p_y1_x1 = y1_x1/count_x1
    G = p_x0*(p_y0_x0* p_y1_x0) + p_x1*(p_y0_x1*p_y1_x1)
    return G

# Ֆունկցիա տվյալների բաժանման համար
def split_data(data, feature_index):
    left = []
    right = []
    for row in data:
        if row[feature_index] == 0:
            left.append(row)
        else:
            right.append(row)
    return left, right

# Ֆունկցիա, որը ստուգում է արդյոք բոլոր լեյբլները նույնն են
def all_same_label(data):
    if len(data) == 0:
        return True
    first_label = data[0][-1]
    for row in data:
        if row[-1] != first_label:
            return False
    return True

# Ռեկուրսիվ Decision Tree կառուցելու ֆունկցիա
def build_tree(data, features):
    if len(data) == 0:
        return None
    
    if all_same_label(data):
        return data[0][-1]  # Leaf node՝ լեյբլը

    if len(features) == 0:
        # Leaf node՝ առավել տարածված լեյբլը
        counts = {}
        for row in data:
            counts[row[-1]] = counts.get(row[-1], 0) + 1
        return max(counts, key=counts.get)

    # Գնահատում ենք Gini-ն բոլոր հատկանիշների համար
    ginis = [gini_formula(data, i) for i in features]
    mini_gini = min(ginis)
    best_feature = ginis.index(mini_gini)

    left_data, right_data = split_data(data, best_feature)
    
    # Ստեղծում ենք ենթախմբերի համար մնացած հատկանիշների ցուցակ
    remaining_features = [i for i in features if i != best_feature]
    
    tree = {}
    tree["feature"] = best_feature
    tree["left"] = build_tree(left_data, remaining_features)
    tree["right"] = build_tree(right_data, remaining_features)
    
    return tree

# Բոլոր հատկանիշները (հիմնական data-ում առաջին 4-ը)
features = [0,1,2,3]

decision_tree = build_tree(data, features)

# Ֆունկցիա ծառի գեղեցիկ տպման համար
def print_tree(node, depth=0):
    if isinstance(node, dict):
        print("  "*depth + f"[X{node['feature']+1}]?")
        print_tree(node['left'], depth+1)
        print_tree(node['right'], depth+1)
    else:
        print("  "*depth + f"Leaf: {node}")

print_tree(decision_tree)
