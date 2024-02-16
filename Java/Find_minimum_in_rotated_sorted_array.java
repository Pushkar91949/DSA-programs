package Java;
/**
 * Find_minimum_in_rotated_sorted_array
 */
public class Find_minimum_in_rotated_sorted_array {
    public static int minimum(int[] arr){
        int l = 0;
        int r = arr.length - 1;
        int result = arr[0];

        while(l <= r){

            if (arr[l] < arr[r]){
                result = Math.min(arr[l], result);
            }

            int mid = l + (r - l)/2;

            result = Math.min(arr[mid], result);

            if (arr[mid] >= arr[l]){
                l = mid + 1;
            }else{
                r = mid - 1;
            }


        }
        return result;


    }

    public static void main(String[] args) {
        int[] arr = {8,9,1,2,3,4,5,6,7};
        int res = minimum(arr);
        System.out.println(res);
        
    }
}