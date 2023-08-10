import sys
import json
import time
import requests
from logging import critical as log

requests.packages.urllib3.disable_warnings()


def main():
    data = sys.stdin.read()

    url = 'https://{}'.format(sys.argv[1])

    ts = time.time()
    log('sending request - {}'.format(url))
    try:
        res = requests.put(url, data=data, verify=False)
    except Exception as e:
        log('could not connect : {}'.format(e))
        exit(1)

    log('status : {}'.format(res.status_code))

    if 200 != res.status_code:
        print(res.content.decode())
        exit(1)

    content = res.json()
    content['time_ms'] = int((time.time() - ts) * 1000)
    print(json.dumps(content, indent=4, sort_keys=True))


if '__main__' == __name__:
    main()
