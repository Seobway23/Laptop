import java.util.Arrays;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        
        Arrays.sort(num_list); 
        return Arrays.stream(num_list)
                .limit(5)
                .toArray();
    }
}