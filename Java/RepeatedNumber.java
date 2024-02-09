package Java;
import java.util.HashSet;
import java.util.Set;

public class RepeatedNumber {
    public static void main(String[] args) {
        int[] A = {3, 1, 2, 5, 3};
        int[] result = repeatedNumber(A);
        System.out.println("Repeated: " + result[0] + ", Missing: " + result[1]);
    }

    public static int[] repeatedNumber(int[] A) {
        int n = A.length;
        Set<Integer> uniqueEle = new HashSet<>();
        int tsum = (n * (n + 1)) / 2;

        int sumA = 0;
        int repeat = 0;
        int missing = 0;

        for (int num : A) {
            if (uniqueEle.contains(num)) {
                repeat = num;
            }
            uniqueEle.add(num);
            sumA += num;
        }

        int uniqueSum = sumA - repeat;
        missing = tsum - uniqueSum;

        return new int[]{repeat, missing};
    }
}
