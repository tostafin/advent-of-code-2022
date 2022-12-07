from __future__ import annotations

from dataclasses import dataclass, field
from typing import List


@dataclass
class DirFile:
    size: int
    name: str


@dataclass
class DirNode:
    name: str
    parent: DirNode = None
    sub_dirs: List[DirNode] = field(default_factory=list)
    files: List[DirFile] = field(default_factory=list)
    subdir_size: int = 0

    def get_sub_dirs_sizes(self) -> None:
        for s in self.sub_dirs:
            s.get_sub_dirs_sizes()
            self.subdir_size += s.subdir_size

        for f in self.files:
            self.subdir_size += f.size

    def get_smallest_dir_to_delete(self, space_needed: int, curr_smallest_space: int = float("inf")) -> int:
        for s in self.sub_dirs:
            if s.subdir_size >= space_needed:
                curr_smallest_space = min(
                    curr_smallest_space, s.get_smallest_dir_to_delete(space_needed, curr_smallest_space)
                )

        return min(self.subdir_size, curr_smallest_space)


with open("input", "r") as commands:
    root_dir: DirNode = DirNode("/")
    curr_dir: DirNode = root_dir
    for c in filter(None, commands.read().split("\n")):
        command: List[str] = c.split()
        if command[0] == "$" and command[1] == "cd":
            if command[2] == "/":
                curr_dir = root_dir
            elif command[2] == "..":
                curr_dir = curr_dir.parent
            else:
                new_dir: DirNode = DirNode(command[-1], curr_dir)
                curr_dir.sub_dirs.append(new_dir)
                curr_dir = new_dir

        elif command[0].isdigit():
            curr_dir.files.append(DirFile(int(command[0]), command[1]))

    root_dir.get_sub_dirs_sizes()
    print(root_dir.get_smallest_dir_to_delete(30_000_000 - (70_000_000 - root_dir.subdir_size)))
