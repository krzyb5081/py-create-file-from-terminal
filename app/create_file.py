import os
import sys
from datetime import datetime


def main() -> None:
    args = sys.argv[1:]
    dir_parts = []
    file_name = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and args[i] not in ("-d", "-f"):
                dir_parts.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args) and args[i] not in ("-d", "-f"):
                file_name = args[i]
                i += 1
        else:
            i += 1

    target_dir = os.path.join(*dir_parts) if dir_parts else ""
    if target_dir:
        os.makedirs(target_dir, exist_ok=True)

    if file_name:
        target_file = os.path.join(target_dir, file_name) if target_dir else file_name

        lines = []
        while True:
            line = input("Enter content line: ")
            if line == "stop":
                break
            lines.append(line)

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry_blocks = [timestamp]
        for index, text in enumerate(lines, 1):
            entry_blocks.append(f"{index} {text}")
        payload = "\n".join(entry_blocks) + "\n"

        file_has_data = os.path.exists(target_file) and os.path.getsize(target_file) > 0
        with open(target_file, "a", encoding="utf-8") as f:
            if file_has_data:
                f.write("\n")
            f.write(payload)


if __name__ == "__main__":
    main()
