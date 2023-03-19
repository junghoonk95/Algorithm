def main():
    import sys
    input = sys.stdin.readline
    N = int(input())

    li = []
    for i in range(N):
        li.append(tuple(map(int, input().split())))

    print(solution(N, li))


def solution(N: int, li: list):
    answer = 0

    li.sort(key=lambda x: (x[1], x[0]))
    last_end = 0
    for s, e in li:
        if s >= last_end:
            answer += 1
            last_end = e

    return answer


if __name__ == "__main__":
    main()
