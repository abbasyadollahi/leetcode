// https://leetcode.com/problems/longest-common-subsequence/

function longestCommonSubsequence(text1: string, text2: string): number {
    let l1 = text1.length;
    let l2 = text2.length;
    let dp = new Array(l1 + 1).fill(0).map(() => new Array(l2 + 1).fill(0));

    for (const [i, t1] of ['', ...text1].entries()) {
        for (const [j, t2] of ['', ...text2].entries()) {
            if (i == 0 || j == 0) {
                continue;
            } else if (t1 == t2) {
                dp[i][j] = 1 + dp[i-1][j-1];
            } else {
                dp[i][j] = Math.max(dp[i-1][j], dp[i][j-1]);
            }
        }
    }
    return dp[l1+1][l2+1];
};
