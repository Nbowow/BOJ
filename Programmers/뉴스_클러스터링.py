def solution(str1, str2):
    one = []
    two = []
    for i in range(len(str1)-1):
        if 65 <= ord(str1[i]) <= 90 or 97 <= ord(str1[i]) <= 122:
            if 65 <= ord(str1[i+1]) <= 90 or 97 <= ord(str1[i+1]) <= 122:
                one.append(str1[i:i+2])
    for i in range(len(str2)-1):
        if 65 <= ord(str2[i]) <= 90 or 97 <= ord(str2[i]) <= 122:
            if 65 <= ord(str2[i+1]) <= 90 or 97 <= ord(str2[i+1]) <= 122:
                two.append(str2[i:i+2])
    for i in range(len(one)): # 소문자로 통일
        one[i] = one[i].lower()
    for i in range(len(two)): # 소문자로 통일
        two[i] = two[i].lower()
    
    one1 = one.copy()
    two1 = two.copy()

    # 교집합
    inter = []
    for i in range(len(one)):
        if one[i] in two1:
            inter.append(one[i])
            two1.remove(one[i])
            
    #합집합
    union = one + two
    for i in range(len(inter)):
        if inter[i] in union:
            union.remove(inter[i])
   
    if len(union) != 0:
        answer = int(len(inter) / len(union)*65536)
    else: answer = 65536
        
    return answer

#print(solution("FRANCE", "french")) 