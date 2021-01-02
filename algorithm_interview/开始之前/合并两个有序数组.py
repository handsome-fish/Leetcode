"""
混合插入有序数组，由于两个数组都是有序的，所以只要按顺序比较大小即可。
题目中说了nums1数组有足够大的空间，说明我们不用resize数组，
又给了我们m和n，那就知道了混合之后的数组大小，这样我们就从nums1和nums2数组的末尾开始一个一个比较，
把较大的数，按顺序从后往前加入混合之后的数组末尾。需要三个变量i，j，k，分别指向nums1,nums2,和混合数组的末尾。
"""
def merge_sorted_array(nums1, m, nums2, n):
    i = m-1
    j = n-1
    k = m+n-1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i = i-1
        else:
            nums1[k] = nums2[j]
            j = j-1
        k = k-1
    while j >= 0:
        nums1[k] = nums2[j]
        k = k-1
        j = j-1
    return nums1


if __name__=="__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    print(merge_sorted_array(nums1, m, nums2, n))
