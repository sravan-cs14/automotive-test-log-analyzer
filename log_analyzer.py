
import re
from collections import Counter

def analyze_log(file_path):
    """Analyze a text log and count common error levels."""

    counts = Counter()
    errors = []

    with open(file_path, "r", encoding="utf-8", errors="replace") as file:
        for line_number, line in enumerate(file, start=1):
            match = re.search(r"\b(ERROR|WARNING|INFO)\b", line, re.I)

            if match:
                level = match.group(1).upper()
                counts[level] += 1

                if level == "ERROR":
                    errors.append({
                        "line": line_number,
                        "message": line.strip()
                    })

    print("AUTOMOTIVE LOG ANALYSIS")
    print("-----------------------")
    print(f"Errors: {counts['ERROR']}")
    print(f"Warnings: {counts['WARNING']}")
    print(f"Info: {counts['INFO']}")

    for error in errors:
        print(f"ERROR at line {error['line']}: {error['message']}")


if __name__ == "__main__":
    analyze_log("sample.log")
