import re
from sys import stdin

lines = stdin.readlines()

for line in lines:
    if 'LATENCY_CHECK' in line:
        result = re.search('id=([^,]+), version=([^]]+)] @ (\d+)', line)
        cid, version, timestamp = result.groups()
        # print('UPDATED', cid, version, timestamp)
        for line in lines:
            eviction_result = re.search(f"Evicting 'onecms:{cid}:{version}' from aspectsHangerCache: (\d+)", line)
            if eviction_result:
                delay = int(eviction_result.group(1)) - int(timestamp)
                print(delay)
