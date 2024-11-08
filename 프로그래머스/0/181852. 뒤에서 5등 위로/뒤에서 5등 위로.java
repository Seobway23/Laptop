import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
         Arrays.sort(num_list);
         int[] target_list = Arrays.copyOfRange(num_list, 5, num_list.length);
         return target_list;
    }
}