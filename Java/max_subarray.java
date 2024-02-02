package Java;

class max_subarray {

    // BRUTE FORCE APPROACH:

    public static int maxsub(int[] arr) {
        int n = arr.length;
        int ans = Integer.MIN_VALUE;
        for (int i = 0; i < n; i++) {
            int curr_sum = 0;
            for (int j = i; j < n; j++) {
                curr_sum += arr[j];
                ans = Math.max(curr_sum, ans);
            }
        }
        return ans;

        // The above approach is inefficient for larger arrays as it checks each and
        // every
        // possible subarray. Time complexity = O(n^3)
        // For this problem, the optimal solution is by using the Kadane's algorithm.
    }

    // KADANE'S ALGORITHM : The optimal solution to this problem.

    public static int Kadane(int[] arr) {
        int n = arr.length;
        int maxsum = Integer.MIN_VALUE;
        int currsum = 0;

        for (int i = 0; i < n; i++) {
            currsum += arr[i];

            if (maxsum < currsum) {
                maxsum = currsum;
            }

            if (currsum < 0) {
                currsum = 0;
            }
        }
        return maxsum;
    }

    public static void main(String[] args) {
        int[] array = { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        int result = Kadane(array);

        int result2 = maxsub(array);

        System.out.println(result);
        System.out.println(result2);
    }
}
// Time complexity = O(n)
