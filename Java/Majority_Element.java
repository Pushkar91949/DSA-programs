package Java;
import java.util.HashMap;
import java.util.Map;

public class Majority_Element {

    public static int majorityElement(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();
        int result = 0, majority = 0;

        for (int num : nums) {
            map.put(num, 1 + map.getOrDefault(num, 0));
            if (map.get(num) > majority) {
                result = num;
                majority = map.get(num);
            }
        }

        return result;
    }

    public static void main(String[] args) {
        int[] nums = {2, 3, 4, 5, 6, 6, 6, 7, 6, 6, 6, 6};
        System.out.println(majorityElement(nums));
    }
}
