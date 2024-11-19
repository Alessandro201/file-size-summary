import os
import sys


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def human_readable(num: float) -> str:
    for unit in ("B", "K", "M", "G", "T", "P", "E", "Z"):
        if abs(num) < 1024.0:
            return f"{num:3.1f}{unit}"
        num /= 1024.0

    return f"{num:.1f}Y"


def main() -> int:
    paths = sys.argv[1:]
    if not paths:
        eprint("You need to supply at least a path")
        exit(1)

    exts: dict[str, int] = {}
    for path in paths:
        for root, _dirs, files in os.walk(path):
            for file in files:
                file = os.path.join(root, file)
                try:
                    _, ext = os.path.splitext(file)
                    size = os.path.getsize(file)
                    ext = ext or "<NoExtension>"
                    tot_size = exts.get(ext, 0)
                    tot_size += size
                    exts[ext] = tot_size
                except OSError as e:
                    eprint(f"Error in getting size of {file}: {e}")

    print(f"{human_readable(sum(exts.values()))} \tTotal")
    for ext, size in sorted(exts.items(), key=lambda x: x[1], reverse=True):
        print(f"{human_readable(size)} \t{ext}")

    return 0
