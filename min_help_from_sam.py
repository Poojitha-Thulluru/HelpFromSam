def min_help_from_sam(score: int) -> int:
    min_count = 0
    while score > 1:
        if score % 2 == 0:
            score //= 2
        else:
            score -= 1
        min_count += 1

    return min_count


try:
    target_score = int(input("Enter the target score : "))
    print(f"The minimum number of times Alex needs to take help from Sam to achieve a score of {target_score} is : ",
          min_help_from_sam(target_score))
except ValueError:
    print("Invalid Input. Please enter only integers")

