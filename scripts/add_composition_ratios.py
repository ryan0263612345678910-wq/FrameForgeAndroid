from pathlib import Path
import re
path = Path("app/src/main/java/com/frameforge/editor/MainActivity.kt")
source = path.read_text(encoding="utf-8")
lines = source.splitlines()
print("MainActivity.kt lines:", len(lines))
print("Composable/function declarations:")
for i, line in enumerate(lines, 1):
    if re.search(r'^\s*(?:@Composable\s*)?(?:private\s+|public\s+|internal\s+)?fun\s+', line):
        print(f"{i}: {line.strip()}")
print("Candidate project-related lines:")
for i, line in enumerate(lines, 1):
    if re.search(r'project|projeto|editor|timeline|compos', line, re.I):
        print(f"{i}: {line.strip()[:200]}")
