# https://leetcode.com/problems/accounts-merge/

from collections import defaultdict


class EmailNode:
    def __init__(self, email: str):
        self.email = email
        self.connections = set()


class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        nodes = {}
        for account in accounts:
            name, *emails = account
            nodes.setdefault(emails[0], EmailNode(emails[0]))
            for email1, email2 in zip(emails, emails[1:]):
                node1 = nodes.setdefault(email1, EmailNode(email1))
                node2 = nodes.setdefault(email2, EmailNode(email2))
                node1.connections.add(node2)
                node2.connections.add(node1)

        visited = set()
        merged_accounts = []
        for account in accounts:
            name, email, *_ = account
            if nodes[email] in visited:
                continue
            merged_emails = []
            queue = [nodes[email]]
            while queue:
                node = queue.pop()
                if node in visited:
                    continue
                visited.add(node)
                merged_emails.append(node.email)
                queue.extend(nodes[node.email].connections - visited)
            merged_accounts.append([name] + sorted(merged_emails))

        return merged_accounts

    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        union_find = UnionFind(list(range(len(accounts))))

        ownership = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in ownership:
                    union_find.union(i, ownership[email])
                else:
                    ownership[email] = i

        merged = defaultdict(list)
        for email, owner in ownership.items():
            merged[union_find.find(owner)].append(email)

        return [[accounts[owner][0]] + sorted(emails) for owner, emails in merged.items()]


class UnionFind:
    def __init__(self, items: list[int]):
        self.items = items
        self.group_sizes = [1] * len(items)

    def find(self, x: int) -> int:
        """Find the root of the group `x` belongs to."""
        item = x
        while item != self.items[item]:
            item = self.items[item]

        while x != self.items[x]:
            x, self.items[x] = self.items[x], item

        return item

    def union(self, x: int, y: int) -> None:
        """Merge `x` and `y` groups."""
        x_root = self.find(x)
        y_root = self.find(y)

        x_size = self.group_sizes[x_root]
        y_size = self.group_sizes[y_root]

        if x_root == y_root:
            return

        if x_size > y_size:
            self.items[y_root] = x_root
            self.group_sizes[x] += y_size
            self.group_sizes[y] = 0
        else:
            self.items[x_root] = y_root
            self.group_sizes[y] += x_size
            self.group_sizes[x] = 0
