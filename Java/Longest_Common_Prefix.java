package Java;

import java.util.Arrays;

/**
 * Longest_Common_Prefix
 */
public class Longest_Common_Prefix {
    public static String longestCommonPrefix(String[] v) {

        Arrays.sort(v);

        StringBuilder s = new StringBuilder();

        String initial = v[0];
        String last = v[v.length - 1];

        for (int i = 0; i < Math.min(initial.length(), last.length()); i++) {

            if (initial.charAt(i) != last.charAt(i)) {
                return s.toString();
            }
            s.append(initial.charAt(i));
        }
        return s.toString();
    }

    public static void main(String[] args) {
        String[] v = {"flower", "flow", "flight"};
        System.out.println(longestCommonPrefix(v));
    }
}
