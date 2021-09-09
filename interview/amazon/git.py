import hashlib
from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Optional


@dataclass
class Commit:

    id: int
    hash: str
    author: str
    message: str
    content: str
    timestamp: datetime


@dataclass
class CommitNode:

    current: Commit
    previous_node: Optional['CommitNode']
    next_node: Optional['CommitNode']


class Git:

    history: Dict[str, CommitNode] = {}
    head_commit_node: CommitNode = None

    def commit(self, commit: Commit) -> str:
        commit.hash = self._generate_commit_hash(commit)

        new_head_commit_node = CommitNode()
        new_head_commit_node.current = commit
        new_head_commit_node.previous_node = self.head_commit_node

        if self.head_commit_node is not None:
            self.head_commit_node.next_node = new_head_commit_node

        self.head_commit_node = new_head_commit_node
        self.history[commit.hash] = new_head_commit_node

        return commit.hash

    def checkout(self, commit_hash: str) -> Commit:
        return self._get_commit_node_by_hash(commit_hash).current

    def log(self, start_commit_hash: str, end_commit_hash: str) -> List[Commit]:
        start_commit_node = self._get_commit_node_by_hash(start_commit_hash)
        end_commit_node = self._get_commit_node_by_hash(end_commit_hash)

        commit_log = []
        current_commit_node = start_commit_node
        while current_commit_node != end_commit_node:
            commit_log.append(current_commit_node.current)
            current_commit_node = current_commit_node.next_node

        return commit_log

    def _generate_commit_hash(self, commit: Commit) -> str:
        return hashlib.sha1(str(commit)).hexdigest()

    def _get_commit_node_by_hash(self, commit_hash: str) -> CommitNode:
        commit_node = self.history.get(commit_hash, None)
        if commit_node is None:
            raise ValueError(f"Commit hash {commit_hash} does not exist within this branch")
        else:
            return commit_node
