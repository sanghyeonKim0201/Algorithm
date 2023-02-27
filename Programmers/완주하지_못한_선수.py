def solution(participant, completion):

    answer = ''

    participant.sort()
    completion.sort()

    print(participant)
    print(completion)

    for i in range(len(participant)):

        if i == len(participant) - 1:
            answer = participant[i]
            return answer

        if participant[i] != completion[i]:
            answer = participant[i]
            return answer

    return answer

# print(solution(	["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]	))
