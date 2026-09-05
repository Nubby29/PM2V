import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

changed = 0
for i, line in enumerate(lines):
    if '05:26 PM' in line and 'date' in line:
        lines[i] = '<div class="date" id="dashboardDate"></div>\n'
        changed += 1
    elif '05:30:22 PM' in line and 'date' in line:
        lines[i] = '<div class="date" id="profileDate"></div>\n'
        changed += 1

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print('Done - ' + str(changed) + ' date IDs added')
