def merge_sorted_array(nums1, m, nums2, n):
    """ Leetcode 88 - Merge Sorted Array"""
    # get last index of nums1

    last_index = m + n - 1
    # merge arrays in reverse order
    while m > 0  and n > 0:
        if nums1[m-1] > nums2[n-1]:
            nums1[last_index] = nums1[m-1]
            m -= 1
        else:
            nums1[last_index] = nums2[n-1]
            n -= 1
        last_index -= 1

    # edge case if there's leftover elements from nums2

    while n > 0:
        nums1[last_index] = nums2[n-1]
        last_index, n = last_index - 1, n - 1
    return nums1

print(merge_sorted_array([1,2,3,0,0,0], 3, [2, 5, 6], 3))

