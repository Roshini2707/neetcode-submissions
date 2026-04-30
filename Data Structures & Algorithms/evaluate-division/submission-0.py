class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for (a, b), value in zip(equations, values):
            graph[a].append((b, value))
            graph[b].append((a, 1 / value))

        def dfs(src, dst, visited):
            if src == dst:
                return 1.0

            visited.add(src)

            for nei, weight in graph[src]:
                if nei not in visited:
                    result = dfs(nei, dst, visited)

                    if result != -1.0:
                        return weight * result

            return -1.0

        ans = []

        for src, dst in queries:
            if src not in graph or dst not in graph:
                ans.append(-1.0)
            else:
                ans.append(dfs(src, dst, set()))

        return ans