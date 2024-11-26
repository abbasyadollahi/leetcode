# https://leetcode.com/problems/snapshot-array/


class SnapshotArray:
    def __init__(self, length: int) -> None:
        self.snapshot = 0
        self.array = [{self.snapshot: 0} for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.array[index][self.snapshot] = val

    def snap(self) -> int:
        current_snap = self.snapshot
        self.snapshot += 1
        return current_snap

    def get(self, index: int, snap_id: int) -> int:
        values = self.array[index]
        if snap_id in values:
            return values[snap_id]
        else:
            previous_snap = 0
            for snap in values:
                if snap < snap_id:
                    previous_snap = snap
                else:
                    return values[previous_snap]
            return values[previous_snap]
