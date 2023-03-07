import time


def input_process(*i):
    N = int(i[0])
    return N


def scoring(solution):
    input_list = []
    output_list = []

    with open("input.txt", "r") as f:
        for l in f:
            input_list.append(l.strip())

    with open("output.txt", "r") as f:
        for l in f:
            output_list.append(l.strip())

    wrong_list = []
    for index, (i, o) in enumerate(zip(input_list, output_list)):
        st = time.time()
        N = input_process(i)
        answer = solution(N)
        print(f'# {index+1}: running time: {time.time() - st:.5f}')
        print(f'yours: {answer}\nanswer: {o}')
        if str(o) == str(answer):
            print('correct')
        else:
            print('wrong')
            wrong_list.append(index+1)
        print()

    print(f'score: {len(input_list) - len(wrong_list)}/{len(input_list)}')
    print('wrong list:', *wrong_list)


def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    print(solution2(N))


def solution(N: int):
    answer = 0
    while N > 0:
        if N % 5 == 0:
            answer += N // 5
            break

        answer += 1
        N -= 3

    return answer if N >= 0 else -1


def solution2(N: int):
    INF = 2e+9
    dp = [INF] * 5001
    dp[3], dp[5] = 1, 1

    for i in range(6, N+1):
        dp[i] = min(dp[i-3], dp[i-5])

        if dp[i] != INF:
            dp[i] += 1

    if dp[N] == INF:
        return -1
    else:
        return dp[N]


if __name__ == "__main__":
    main()
    # scoring(solution2)
