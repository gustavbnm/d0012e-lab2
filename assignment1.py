from array import array
import random

def main():
    n=10
    min_val, max_val = 0, 100
    a = array("i", random.sample(range(min_val,max_val),n))
    test = worst_case_three(a,0,1,2)

def worst_case_three(arr: array, i, j, k):
    length = len(arr)

    # If i hits the end there is no solution
    if i >= length:
        print("Nah")
        return False

    # If j hits the end we move to the next i
    if j >= length:
        return worst_case_three(arr, i+1, i+2, i+3)

    # If k hits the end we move to the next j
    if k >= length:
        return worst_case_three(arr, i, j+1, j+2)

    if i != j and i != k and j != k:
        if arr[i] + arr[j] == arr[k]:
            print(arr[i], "+", arr[j], "=", arr[k])
            return True

    # If none of the if statements is matched,
    # continue the recursion with the next k
    return worst_case_three(arr, i, j, k+1)

main()
