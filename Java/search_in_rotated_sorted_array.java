package Java;

public class search_in_rotated_sorted_array {
    public static int search(int[] nums, int target) {
        int n = nums.length;
        int low = 0;
        int high = n - 1;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (target == nums[mid]) {
                return mid;
            }

            else if (nums[low] <= nums[mid]) {
                if (nums[low] <= target && target < nums[mid]) {
                    high = mid - 1;
                } else {
                    low = mid + 1;
                }
            } else {
                if (nums[mid] < target && target <= nums[high]) {
                    low = mid + 1;
                } else {
                    high = mid - 1;
                }
            }
        }
        return -1;
    }

    public static void main(String[] args) {
        int[] array = { 4, 5, 6, 7, 8, 9, 10, 1, 2, 3 };
        int target = 10;
        int result = search(array, target);
        System.out.println("Element " + target + " found at index " + result);
    }
}
