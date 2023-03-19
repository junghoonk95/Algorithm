def solution(N, K, A):
    A.sort(reverse=True)
    answer = 0
    for a in A:
        while K >= a:
            answer += 1
            K -= a

    return answer


def main():
    import sys
    input = sys.stdin.readline
    N, K = map(int, input().split())
    A = []
    for _ in range(N):
        A.append(int(input()))

    print(solution(N, K, A))


if __name__ == '__main__':
    main()
