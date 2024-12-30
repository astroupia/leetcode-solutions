def mergePalindrome(nums):
    lft_ptr, rgt_ptr, count = 0, len(nums) - 1, 0
    while lft_ptr < rgt_ptr:
        if nums[lft_ptr] == nums[rgt_ptr]:
            lft_ptr += 1
            rgt_ptr -= 1
        elif nums[lft_ptr] < nums[rgt_ptr]:
            nums[lft_ptr + 1] += nums[lft_ptr]
            lft_ptr += 1
            count += 1
        else:
            nums[rgt_ptr - 1] += nums[rgt_ptr]
            rgt_ptr -= 1
            count += 1
    return count