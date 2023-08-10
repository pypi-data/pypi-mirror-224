import sys
import time
import requests
from logging import critical as log

requests.packages.urllib3.disable_warnings()


def main():
    url = 'https://{}'.format(sys.argv[1])

    ts = time.time()
    log('sending request - {}'.format(url))
    res = requests.get(url, verify=False)
    log('status : {}'.format(res.status_code))

    if 200 != res.status_code:
        print(res.content.decode())
        exit(1)

    print('bucket   : {}'.format(res.headers['x-bucket']))
    print('key      : {}'.format(res.headers['x-key']))
    print('version  : {}'.format(res.headers['x-version']))
    print('length   : {}'.format(res.headers['content-length']))
    print('mimetype : {}'.format(res.headers['content-type']))

    content = res.content
    print('time_ms  : {}'.format(int((time.time() - ts) * 1000)))

    print('')
    print(content)


if '__main__' == __name__:
    main()
