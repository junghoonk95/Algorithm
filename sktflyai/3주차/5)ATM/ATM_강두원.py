def solution(N, P):
    P.sort()

    count = 0
    answer = 0
    for p in P:
        count += p
        answer += count

    return answer


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    print(solution(N, P))


if __name__ == "__main__":
    main()
