void fill_gen_arr(int* nums1, int nums1Size, int* nums2, int nums2Size, int* gen_arr, int gen_size)
{
    int i = 0;
    int j = 0;
    
    for (int k = 0; k < gen_size; k++) {
        if (i < nums1Size && j < nums2Size)
            if (nums1[i] < nums2[j])
                gen_arr[k] = nums1[i++];
            else
                gen_arr[k] = nums2[j++];
        else if (i >= nums1Size)
            gen_arr[k] = nums2[j++];
        else
            gen_arr[k] = nums1[i++];
    }
}

double findMedianSortedArrays(int* nums1, int nums1Size, int* nums2, int nums2Size)
{
    int gen_size = nums1Size + nums2Size;
    int general_arr[gen_size];
    double median = 0.0;
    
    fill_gen_arr(nums1, nums1Size, nums2, nums2Size, general_arr, gen_size);
    if (gen_size % 2 != 0)
        median = general_arr[gen_size / 2];
    else
    {
        median = ((double)general_arr[gen_size / 2] + (double)general_arr[gen_size / 2 - 1]) / 2;
    }
    return median;
}
