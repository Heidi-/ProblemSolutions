
# brute force
class Solution:
    def twoSum(self, nums, target):
        for i, ni in enumerate(nums):
            print(i, ni)
            for j, nj in enumerate(nums[i+1:]):
                print(j, nj)
                if ni + nj == target:
                    print(i, j, ni, nj)
                    return [i, j+i+1]

# using numpy
class Solution:
    def twoSum(self, nums, target):
        arr = np.array(nums)
        for idx in range(1, len(arr)):
            eq_target = arr + np.append(arr[idx:], arr[:idx]) == target
            if any(eq_target):
                i = np.argwhere(eq_target)[0][0]
                j = idx + i
                return [i, j]



