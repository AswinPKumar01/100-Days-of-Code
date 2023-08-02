class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        begin = 0
        end = len(nums) - 1 
        while begin <= end:
            mid = (begin + end)//2
            if nums[mid] == target:
                return True
            if nums[mid] == nums[end]:
                end -= 1
            elif nums[mid] > nums[end]:
                if  nums[begin] <= target and target < nums[mid]:
                    end = mid - 1
                else:
                    begin = mid + 1
            else:
                if  nums[mid] < target and target <= nums[end]:
                    begin = mid + 1
                else:
                    end = mid - 1
        return False
