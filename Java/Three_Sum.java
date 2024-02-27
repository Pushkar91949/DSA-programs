package Java;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Three_Sum {
    public List<List<Integer>> threeSum(int[] nums) {
        Arrays.sort(nums);
        List<List<Integer>> res = new ArrayList<>();

        for (int i = 0; i < nums.length - 2; i++) {
            if (i > 0 && nums[i] == nums[i - 1]) {
                continue;
            }

            int left = i + 1;
            int right = nums.length - 1;

            while (left < right) {
                int threeSum = nums[i] + nums[left] + nums[right];

                if (threeSum > 0) {
                    right--;
                } else if (threeSum < 0) {
                    left++;
                } else {
                    res.add(Arrays.asList(nums[i], nums[left], nums[right]));
                    left++;

                    while (left < right && nums[left] == nums[left - 1]) {
                        left++;
                    }
                }
            }
        }

        return res;
    }

    public static void main(String[] args) {
        Three_Sum threeSumObj = new Three_Sum();
        int[] nums = { -1, 0, 1, 2, -1, -4 };
        List<List<Integer>> result = threeSumObj.threeSum(nums);

        System.out.println(result);
    }
}


// Time complexity = O(n^2)

// O(nlogn) for sorting and O(n^2) when we run two loops, one inside another.) --> O(nlogn) + O(n^2) = O(n^2).

// We take each element of nums and firs element of the triplet one by one. When the 1st element is set, we just need 2 more elements which we get by using 2 pointers, 
// left and right (as we have already sorted the array). if sum of first element, nums[left] and nums[right] == 0: We add [a, nums[left], nums[right]] to our result array.
// This process is done for each and every element when it is set as first element, it is not necessary that we find a solution for all the elements when they are set as first.
