class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) -1

        while left <= right:
            mid = left + (right - left) // 2
            # print(mid)

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
            # normal world
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    # somewhere on the other side
                    left = mid + 1
            else:
            # pivot between left and mid
                # mid to right should be normal
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                # target is somewhere in the wonky world
                    right = mid - 1
        
        return -1