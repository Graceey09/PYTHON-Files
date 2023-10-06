def runner_up_core():
    # scores = []
    # num_scores = int(input("Enter the number of scores: "))
    # for number in range(num_scores):
    #     score = int(input("Enter a score: "))
    #     scores.append(score)
    #
    # unique_scores = list(set(scores))
    # unique_scores.sort(reverse=True)
    #
    # runner_up_score = unique_scores[1]
    #
    # print("The runner-up score is:", runner_up_score)

    if __name__ == '__main__':
        n = int(input("Enter a number: "))
        arr = list(map(int, input("Enter a score: ").split()))
        unique_scores = list(set(arr))
        unique_scores.sort(reverse=True)
        runner_up_score = unique_scores[1]
        print(runner_up_score)


runner_up_core()
