#!/usr/bin/env python3
"""
Entry point for the bounty. Writes a specific line to the output directory.
"""
import os
# Round 2 entry: output is 1-200 chars, exactly one line, deterministic.

LINE = ("My brother leaned against the hospital doorway, cigarettes forgotten, and said, "
        "'You don't stay because it's brave — you stay because the chair next to the bed is still warm.'\n")

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    content = LINE
    if not (1 <= len(content) <= 200 and content.strip() and content.count(chr(10)) == 1 and content.endswith(chr(10))):
        raise ValueError("Validation failed")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Output path: {output_path}")
    print(f"Character count: {len(content)}")

if __name__ == "__main__":
    main()
