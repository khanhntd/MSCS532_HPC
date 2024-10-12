from functools import lru_cache

#@lru_cache(maxsize=16)
# stepsTo will determine the possible combination of all possible ways from the ground
# to a given stair by combining all possible variations of the current step with 1 or 2
# or 3 steps
# Time complexity: O(3^n) (without cache since for each of the step, it will have 3 different ways)
# Space complexity: O(n)
@profile
def stepsTo(stair: int) -> int:
    if stair == 0:
        return 1
    elif stair < 0:
        return 0
    else:
        return stepsTo(stair-1) + stepsTo(stair-2) + stepsTo(stair-3)

if __name__ =="__main__":
    numberOfSteps = stepsTo(30)
    print("Number of combination that can reach to step 7 is ", numberOfSteps)
    #print(stepsTo.cache_info())