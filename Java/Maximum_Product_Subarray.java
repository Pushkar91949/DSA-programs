package Java;

/**
 * Maximum_Product_Subarray
 */
public class Maximum_Product_Subarray {
    public static int maxProduct(int[] nums) {
        int maxi = Integer.MIN_VALUE;
        int prod = 1;

        for (int i = 0; i < nums.length; i++) {
            prod *= nums[i];
            maxi = Math.max(prod, maxi);
            if (prod == 0) {
                prod = 1;
            }
        }
        int prod2 = 1;
        for (int i = nums.length - 1; i >= 0; i--) {
            prod2 *= nums[i];

            maxi = Math.max(prod, maxi);
            if (prod2 == 0) {
                prod2 = 1;
            }
        }
        return maxi;
    }

    public static void main(String[] args) {
        int[] nums = { 2, 3, -2, 4 };
        int res = maxProduct(nums);
        System.out.println(res);
    }
}