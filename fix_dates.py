#!/usr/bin/env python3
"""Fix dynamic date IDs in index.html - regex based for special chars"""
import re

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

# Replace dashboard static date with dynamic ID
# Match: <div class="date"> followed by special chars until </div> on the dashboard page
c = re.sub(
    r'(<div class="date")>([^<]*<span class="sep">\|</span>[^<]*)</div>',
    r'\1 id="dashboardDate"></div>',
    c,
    count=1
)

# Check what's left
remaining = re.findall(r'<div class="date">[^<]*<span class="sep">\|</span>[^<]*</div>', c)
print(f"Remaining old-style dates: {len(remaining)}")
for r in remaining:
    print(f"  Found: {r[:80]}...")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print('Done')

