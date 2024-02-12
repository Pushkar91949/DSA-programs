package Java;

/**
 * trappingRainWater
 */
public class trappingRainWater {
    public static int Trapping_Rain_Water(int[] heights) {
        if (heights == null || heights.length == 0) {
            return 0;
        }
        int l = 0;
        int r = heights.length - 1;
        int leftMax = heights[l];
        int rightMax = heights[r];

        int res = 0;

        while (l < r) {
            if (leftMax < rightMax) {
                l += 1;
                leftMax = Math.max(leftMax, heights[l]);
                res += leftMax - heights[l];
            } else {
                r -= 1;
                rightMax = Math.max(rightMax, heights[r]);
                res += rightMax - heights[r];
            }
        }
        return res;

    }

    public static void main(String[] args) {
        int[] heights = { 0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1 };
        System.out.println(Trapping_Rain_Water(heights));
    }
}