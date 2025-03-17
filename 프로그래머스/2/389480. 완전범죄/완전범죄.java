import java.util.Arrays;

class Solution {
    public int solution(int[][] info, int n, int m) {
        int len = info.length;
        // dp[i][a][b] : 첫 i개의 항목을 사용해서, A 합이 a, B 합이 b인 경우의 수 (여기서는 가능 여부)
        boolean[][][] dp = new boolean[len + 1][n][m];
        dp[0][0][0] = true;
        
        for (int i = 0; i < len; i++) {
            for (int a = 0; a < n; a++) {
                for (int b = 0; b < m; b++) {
                    if (dp[i][a][b]) {
                        // A 선택: A 합 증가 (info[i][0])
                        int newA = a + info[i][0];
                        if (newA < n) {
                            dp[i + 1][newA][b] = true;
                        }
                        
                        // B 선택: B 합 증가 (info[i][1])
                        int newB = b + info[i][1];
                        if (newB < m) {
                            dp[i + 1][a][newB] = true;
                        }
                    }
                }
            }
        }
        
        int answer = Integer.MAX_VALUE;
        // dp[len][a][b]가 true인 상태 중에서 최소의 a값 선택
        for (int a = 0; a < n; a++) {
            for (int b = 0; b < m; b++) {
                if (dp[len][a][b]) {
                    answer = Math.min(answer, a);
                }
            }
        }
        
        return answer == Integer.MAX_VALUE ? -1 : answer;
    }
}
