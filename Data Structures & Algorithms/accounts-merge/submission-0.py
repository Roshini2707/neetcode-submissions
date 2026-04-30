class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = defaultdict(set)
        email_to_name = {}

        for acc in accounts:
            name = acc[0]
            first_email = acc[1]

            for email in acc[1:]:
                email_to_name[email] = name
                graph[first_email].add(email)
                graph[email].add(first_email)

        visited = set()
        res = []

        def dfs(email, component):
            visited.add(email)
            component.append(email)

            for nei in graph[email]:
                if nei not in visited:
                    dfs(nei, component)

        for email in graph:
            if email not in visited:
                component = []
                dfs(email, component)

                res.append(
                    [email_to_name[email]] + sorted(component)
                )

        return res