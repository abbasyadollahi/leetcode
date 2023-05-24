from typing import Optional

member_index: dict[str, 'Member'] = {}
"""Database with member id (key) to member instance (value)."""


class Member:
    def __init__(self, member_id: str, name: str, child_ids: list[str]):
        self.member_id = member_id
        self.name = name
        self.child_ids = child_ids
        self.children = []

    def attach_children(self) -> None:
        """
        Populate `self.children` using `self.child_ids`.
        Assume this is only called once from the `Member.add_members` method.
        """
        # INCOMPLETE #2
        for child_id in self.child_ids:
            child_member = Member.member_index().get(child_id)
            if child_member:
                self.children.append(child_member)

    def find_name(self, name: str) -> Optional['Member']:
        """
        If the name matches the member's name, then return self.
        Otherwise, find any descendant member that matches the given name.
        """
        # INCOMPLETE #3
        generation = [self]
        while generation:
            next_generation = []
            for member in generation:
                if name == member.name:
                    return member
                next_generation.extend(member.children)
            generation = next_generation
        return None

    @staticmethod
    def add_members(family_tree_text: str) -> None:
        """
        Populate the `member_index` database using the family tree.
        """
        for flat_member in family_tree_text.split("\n"):
            unpack = flat_member.split(";")
            member_id = unpack[0]
            name = unpack[1]
            flat_children = unpack[2] if len(unpack) > 2 else None
            child_ids = flat_children.split(",") if flat_children else []
            # INCOMPLETE #1
            if not Member.find(member_id):
                Member.member_index()[member_id] = Member(member_id, name, child_ids)
        for member in Member.member_index().values():
            member.attach_children()

    @staticmethod
    def member_index() -> dict[str, 'Member']:
        global member_index
        if member_index is None:
            member_index = {}
        return member_index

    @staticmethod
    def find(member_id: str) -> Optional['Member']:
        return Member.member_index().get(str(member_id))


def solution(member_id: str, name: str) -> str:
    family_tree_txt = """1;Bill
2;Alex
3;Phil
4;Mary
5;Michael;1
6;Sam;2,3
7;Ashley;5,6
8;Brian;7,4"""

    Member.add_members(family_tree_txt)
    member = Member.find(member_id)
    found = member.find_name(name)
    return found.member_id if found else "0"
