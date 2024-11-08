class Solution {
    public int solution(String my_string, String target) {
        int answer = 0;
        for( int i = 0; i < my_string.length() - target.length() + 1; i++){
                
            System.out.println(my_string.substring(i,i + target.length()) +  ", " + target);
            if (my_string.substring(i,i + target.length()).equals(target) ) {
                
                return 1;
            }
        }

        return answer;
    }
}