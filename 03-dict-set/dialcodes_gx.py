# BEGIN DIALCODES
# dial codes of the top 10 most populous countries
import sys
import re

DIAL_CODES = [
    (86, 'China'),
    (91, 'India'),
    (1, 'United States'),
    (62, 'Indonesia'),
    (55, 'Brazil'),
    (92, 'Pakistan'),
    (880, 'Bangladesh'),
    (234, 'Nigeria'),
    (7, 'Russia'),
    (81, 'Japan'),
]
d1 = dict(DIAL_CODES)
print('d1:', d1.keys())
# print('d1:', d1.items())
d2 = dict(sorted(DIAL_CODES))
print('d2:', d2.keys())
# print('d2:', d2.items())
d3 = dict(sorted(DIAL_CODES, key=lambda x: x[1]))
print('d3:', d3.keys())
# print('d3:', d3.items())
# END DIALCODES
"""
# BEGIN DIALCODES_OUTPUT
d1: dict_keys([880, 1, 86, 55, 7, 234, 91, 92, 62, 81])
d2: dict_keys([880, 1, 91, 86, 81, 55, 234, 7, 92, 62])
d3: dict_keys([880, 81, 1, 86, 55, 7, 234, 91, 92, 62])
# END DIALCODES_OUTPUT
"""

WORD_RE = re.compile(r'\w+')
index = {}
with open("README.rst", encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):
        for match in WORD_RE.finditer(line):
            word = match.group()
            column_no = match.start() + 1
            location = (line_no, column_no)
            index.setdefault(word, []).append(location)

for word in sorted(index, key=str.upper):
    print(word, index[word])

