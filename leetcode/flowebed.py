# https://leetcode.com/problems/can-place-flowers/?envType=problem-list-v2&envId=array
def canPlaceFlowers(flowerbed: list[int], n: int) -> bool:
    if n == 0:
        return True
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0 and (i == 0 or flowerbed[i - 1] == 0) and \
        (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0):
            flowerbed[i] = 1
            n -= 1
            if n == 0:
                return True

    return False


flowerbeds = [1, 0, 0, 0, 1]

canPlaceFlowers(flowerbeds, 1)  # true

