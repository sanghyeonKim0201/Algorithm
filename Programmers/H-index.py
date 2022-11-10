def solution(citations):
    citations.sort()
    article_count = len(citations)

    for i in range(article_count):
        
        if citations[i] >= article_count-i:
            return article_count-i
    return 0

print(solution([0,9,6,8,3]))