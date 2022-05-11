def orangecap(d):
    dict_new = {}
    for match in d.keys():
        #list_of_players = match.keys()
        for player in  d[match].keys():
            if player in dict_new.keys():
                dict_new[player] = dict_new[player] + d[match][player]
            else:
                dict_new[player] = d[match][player]
    highest = 0
    for score in dict_new.keys():
        if dict_new[score] > highest:
            highest = dict_new[score]
            (playername, score1) = (score, dict_new[score])
    return (playername, score1)

def addpoly(*arg):
    list1 = []
    for j,i in enumerate(arg):
        list1.extend(i)
        
    def func(l):
        return l[1]   
    
    list1 = sorted(list1, key=func, reverse = True)
    list2 =[]
    
    #print(list1,len(list1))
    i = 0
    while i < len(list1)-1:
        #print(i)
        if list1[i][1] == list1[i+1][1]:
            ele = list1[i][0] + list1[i+1][0]
            i = i + 1
            if ele != 0:
                list2.append((ele,list1[i][1]))
        else:
            list2.append(list1[i])
        i = i+1
    #print(list1, list2)
    
    if list2 != [] and list2[-1][1] != list1[-1][1]:
        list2.append(list1[-1])
    return list2

def multpoly(l1,l2):
    final_list = {}
    for i in l1:
        for j in l2:
            coeff = i[0]*j[0]
            power = i[1] + j[1]
            if power in final_list.keys():
                final_list[power] = final_list[power] + coeff
            else:
                final_list[power] = coeff
    result = []
    for i in final_list.keys():
        if final_list[i] != 0:
            result.append((final_list[i], i))
            
    return result
