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

for i in range(4):
    g = gini_formula(data, i)
    print("X" + str(i+1), round(g,3))

ginis = [gini_formula(data, i) for i in range(4)]
mini_gini = min(ginis)
best = ginis.index(mini_gini)+ 1

print(str(best))            
