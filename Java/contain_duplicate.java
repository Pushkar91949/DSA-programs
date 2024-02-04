package Java;

import java.util.Arrays;
import java.util.HashSet;

//BRUTE FORCE
// This solution checks all the elements with all other elements which is slower.
//Time complexity of this Brute force approach is O(n^2)

public class contain_duplicate {
    public static boolean containsDuplicateBruteForce(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (arr[i] == arr[j]) {
                    return true;
                }
            }

        }
        return false;

    }
    // Time complexity = O(n^2)

    // SORTING METHOD

    public static boolean containsDuplicateSorting(int[] arr) {
        Arrays.sort(arr);
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] == arr[i + 1])
                return true;
        }
        return false;
    }
    // Time complexity = O(nlog(n))
    //

    // USING HASHSET - Most efficient solution

    public static boolean containsDuplicate(int[] arr) {
        HashSet<Integer> present_elements = new HashSet<>();
        for (int num : arr) {
            if (present_elements.contains(num))
                return true;
            present_elements.add(num);
        }
        return false;
    }
    // Time complexity = O(n)

    public static void main(String[] args) {
        int[] array = { 1, 2, 3, 4, 5, 6, 1 };
        int[] array2 = { 1, 2, 3, 4, 5, 6, 7, 8, 9 };
        int[] array3 = { 1, 2, 3, 4, 5, 6, 1, 6, 7, 1 };

        System.out.println(containsDuplicateBruteForce(array));

        System.out.println(containsDuplicateSorting(array2));

        System.out.println(containsDuplicate(array3));
    }
}

// If we used HashMap, it is similar to HashSet that we used, but it will also
// keep the count of the occurences.