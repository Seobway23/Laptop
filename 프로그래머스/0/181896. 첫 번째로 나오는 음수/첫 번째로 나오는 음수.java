class Solution {
    public int solution(int[] num_list) {
        int ans = -1;
        for ( int i=0; i<num_list.length; i++){
            if (num_list[i] < 0){
                ans = i;
                break;
            }
        }
        
        return ans;
    }
}