def ruffier_index(P1, P2, P3):
    ruffier_index = (4 * (P1 + P2 + P3) - 200) / 10
    return ruffier_index

def max_ruffier_index(age):
    index = (min(age, 15) - 7) // 2
    result = 21 - index * 1.5
    return result

def ruffier_level(ruffier_ind, max_ruffier_ind):


    if ruffier_ind >= max_ruffier_ind: 
        return 0

    max_ruffier_ind = max_ruffier_ind - 4
    
    if ruffier_ind >= max_ruffier_ind: 
        return 1

    max_ruffier_ind = max_ruffier_ind - 5
    
    if ruffier_ind >= max_ruffier_ind: 
        return 2

    max_ruffier_ind = max_ruffier_ind - 5.5
    
    if ruffier_ind >= max_ruffier_ind: 
        return 3
    
    return 4
    
def test(P1,P2,P3,age):
    ruffier_ind = ruffier_index(P1,P2,P3)
    max_ruffier_ind = max_ruffier_index(age)
    level = ruffier_level(ruffier_ind, max_ruffier_ind)
    
