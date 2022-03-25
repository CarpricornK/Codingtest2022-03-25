def solution(participant, completion):
    tmp = 0
    dic = {}

    for p in participant:
        dic[hash(p)] = p

        tmp += int(hash(p))

    for com in completion:
        tmp -= hash(com)

    return dic[tmp]

def solution2(phone_book):
    phone_book.sort()
    answer = str(True)
    phone_length = len(phone_book)

    for i in range(phone_length - 1):
        if phone_book[i] == phone_book[i + 1][0:len(phone_book[i])]:
            answer = str(False)

            break

    return answer

print("완주하지 못한 선수 ="+solution(["leo", "kiki", "eden"],["leo", "kiki"]))
print("전화번호 목록['12','123','1235','567','88'] = "+solution2(["12","123","1235","567","88"]))
print("전화번호 목록['123','456','789'] = "+solution2(["123","456","789"]))


