def twoOutOfThree(nums1, nums2, nums3):
    s1 = set(nums1)
    s2 = set(nums2)
    s3 = set(nums3)

    result = set()

    for i in s1:
        if i in s2 or i in s3:
            result.add(i)

    for i in s2:
        if i in s3:
            result.add(i)

    return list(result)

nums1 = [1,1,3,2]
nums2 = [2,3]
nums3 = [3]

print(twoOutOfThree(nums1, nums2, nums3))

nums1 = [3,1]
nums2 = [2,3]
nums3 = [1,2]

print(twoOutOfThree(nums1, nums2, nums3))

nums1 = [1,2,2]
nums2 = [4,3,3]
nums3 = [5]
print(twoOutOfThree(nums1, nums2, nums3))

