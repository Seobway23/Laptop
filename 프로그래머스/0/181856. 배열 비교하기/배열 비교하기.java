import java.util.Arrays;

class Solution {
    public int solution(int[] arr1, int[] arr2) {
        int answer = 0;
        
        // 배열이 길다면 긴 배열이 승
        if (arr1.length > arr2.length) {
            answer = 1;
        }
        
        else if (arr1.length < arr2.length) {
            answer = -1;
        }
        
        else {
            // 1이 더 크면
            if(Arrays.stream(arr1).sum() > Arrays.stream(arr2).sum()){
                answer = 1;
            }

            // 2가 더 크면
            else if (Arrays.stream(arr1).sum() < Arrays.stream(arr2).sum()) {
                answer = -1;
            }
            
            // 같으면
            else{
                answer = 0;
            }

        }
        
        

        
        
        return answer;
    }
}