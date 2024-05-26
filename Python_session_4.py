n = int(input("Enter the value of n: "))
scores = list(map(int, input("Enter the value of array: ").split()))

unique_scores = list(set(scores))

unique_scores.sort(reverse=True)

runner_up_score=unique_scores[1]

print("Runner-up Scores is; ", runner_up_score)



