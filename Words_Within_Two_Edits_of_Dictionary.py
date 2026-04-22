def twoEditWords(queries, dictionary):
    result = []
    
    for q in queries:
        for d in dictionary:
            diff = 0
            
            for i in range(len(q)):
                if q[i] != d[i]:
                    diff += 1
                    
                if diff > 2:
                    break
            
            if diff <= 2:
                result.append(q)
                break  
    
    return result

queries = ["word","note","ants","wood"]
dictionary = ["wood","joke","moat"]

print(twoEditWords(queries, dictionary))

queries = ["yes"]
dictionary = ["not"]

print(twoEditWords(queries, dictionary))

