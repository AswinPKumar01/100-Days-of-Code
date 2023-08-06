class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        
        def solve(n, goal):
            if goal==0 and n==0:
                return 1
            if goal==0 or n==0:
                return 0
            if memo[n][goal] != -1:
                return memo[n][goal]
            replay_old_song = solve(n, goal-1)*max(n-k, 0)
            play_new_song = solve(n-1, goal-1)*n
            memo[n][goal] = (replay_old_song + play_new_song)%1000000007 
            return memo[n][goal]

        memo = [[-1 for j in range(goal+1)]for i in range(n+1)]
        return solve(n, goal)
