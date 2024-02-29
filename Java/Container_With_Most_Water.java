package Java;

public class Container_With_Most_Water {
    public static int mostWater(int[] height) {
        int maxWater = 0;
        int left = 0;
        int right = height.length - 1;

        while (left < right) {
            int waterNow = Math.min(height[left], height[right]) * (right - left);
            maxWater = Math.max(maxWater, waterNow);

            if (height[left] < height[right]) {
                left += 1;
            } else {
                right -= 1;
            }
        }

        return maxWater;
    }

    public static void main(String[] args) {
        int[] heights = { 1, 8, 6, 2, 5, 4, 8, 3, 7 };

        int res = mostWater(heights);

        System.out.println(res);
    }

}
