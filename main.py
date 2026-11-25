import os
import sys


def main() -> None:
    """Write a specific sentence to $MAKEFUN_OUTPUT_DIR/entry.txt with validation."""
# Entry validated: output is 1-200 chars, exactly one sentence, deterministic.
    LINE = "Abuela pressed a jar of dried beans into my palms at the bus station, murmuring count them slow, mijo — hunger teaches what abundance never bothers to explain."
    content = LINE + "\n"
    
    if not (1 <= len(content) <= 200 and content.strip() and content.count(chr(10)) == 1 and content.endswith(chr(10))):
        raise ValueError("content validation failed")
    
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "entry.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"{output_path} {len(content)}")


if __name__ == "__main__":
    main()
