package Java;

public class Maxmin {
    public static int[] minmax(int[] arr) {
        int n = arr.length;

        if (n == 1) {
            return new int[] { arr[0], arr[0] };
        }

        int minimum, maximum;

        if (arr[0] > arr[1]) {
            minimum = arr[1];
            maximum = arr[0];
        } else {
            minimum = arr[0];
            maximum = arr[1];
        }

        for (int i = 2; i < n; i++) {
            if (arr[i] > maximum) {
                maximum = arr[i];
            } else if (arr[i] < minimum) {
                minimum = arr[i];
            }

        }
        return new int[] { minimum, maximum };

    }

    public static void main(String[] args) {
        int[] array = { 3, 1, 8, 4, 6, 2, 10, 96996 };
        int[] result = minmax(array);
        System.out.println("Min: " + result[0]);
        System.out.println("Max: " + result[1]);

    }
}
