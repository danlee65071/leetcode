int maxArea(int* height, int heightSize)
{
    int     max_area = 0;
    int     current_area = 0;
    int     start = 0;
    int     end = heightSize - 1;

    while (start < end)
    {
        if (height[start] <= height[end])
        {
            current_area = height[start] * (end - start);
            start++;
        }
        else
        {
            current_area = height[end] * (end - start);
            end--;
        }
        if (current_area > max_area)
            max_area = current_area;
    }
    return max_area;
}
