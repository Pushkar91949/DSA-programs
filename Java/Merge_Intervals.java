import java.util.ArrayList;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Iterator;
import java.util.List;

public class MergeIntervals {
    public static List<List<Integer>> merge(List<List<Integer>> intervals) {
        intervals.sort(Comparator.comparingInt(x -> x.get(0)));

        
        Iterator<List<Integer>> iterator = intervals.iterator();
        int i = 0;
        while (iterator.hasNext()) {
            List<Integer> current = iterator.next();

            if (iterator.hasNext()) {
                List<Integer> next = iterator.next();

                if (current.get(1) >= next.get(0)) {
                    current.set(1, Math.max(current.get(1), next.get(1)));
                    iterator.remove();
                } else {
                    i++;
                }
            }
        }

        return intervals;
    }

    public static void main(String[] args) {
        
        List<List<Integer>> intervals = new ArrayList<>(Arrays.asList(
                Arrays.asList(1, 3),
                Arrays.asList(2, 6),
                Arrays.asList(8, 10),
                Arrays.asList(15, 18)
        ));

        List<List<Integer>> result = merge(intervals);
        System.out.println(result);
    }
}
