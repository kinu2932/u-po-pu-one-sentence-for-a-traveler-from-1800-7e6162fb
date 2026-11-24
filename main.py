import os

ENTRY = "Imagine every post office, library, and market square in the world joined by one road, so a letter, a book, or a spoken word can reach anyone, anywhere, before the ink dries."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
print("wrote entry.txt")
