package Java;

import java.util.Arrays;

public class chocolateDistribution {
    public static int minDiffChocolates(int[] arr, int n, int m) {
        int min_diff_final = Integer.MAX_VALUE;

        Arrays.sort(arr);

        for (int i = 0; i < n - m + 1; i++) {
            int mini = arr[i];
            int maxi = arr[i + m - 1];
            int min_diff_curr = maxi - mini;
            if (min_diff_curr < min_diff_final) {
                min_diff_final = min_diff_curr;
            }

        }
        return min_diff_final;
    }

    public static void main(String[] args) {
        int[] chocolates = { 12, 4, 7, 9, 2, 23, 25, 41,
                30, 40, 28, 42, 30, 44, 48,
                43, 50 };
        int n = chocolates.length;
        int m = 7;

        System.out.println("Min difference = " + minDiffChocolates(chocolates, n, m));
    }
}
// Time complexity = O(n*log(n))