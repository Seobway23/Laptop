class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        String A = "";
        String B = "";
        for (int i =0; i < num_list.length; i++){
            if (num_list[i] % 2 == 0) { // 짝수일 경우
                A += num_list[i];
            }
            
            else {
                B += num_list[i];
            }
        }
        
        answer = Integer.parseInt(A) + Integer.parseInt(B);
        return answer;
    }
}