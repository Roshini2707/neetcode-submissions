class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        connected = 0
        adj = [[] for _ in range(n)]
        visit = [False] * n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node):
            for i in adj[node]:
                if not visit[i]:
                    visit[i] = True
                    dfs(i)

        for node in range(n):
            if not visit[node]:
                visit[node] = True
                dfs(node)
                connected += 1
        return connected
        