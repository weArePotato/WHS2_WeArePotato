#!/usr/bin/env python3
import sys

def download(url: str, times: int) -> None:

    import socket
    import ssl
    import urllib.parse

    # import pip._internal.network.session
    # user_agent = pip._internal.network.session.user_agent().encode()

    # Manual user agent, keep it short than what pip uses, to save A LOT of data
    user_agent = b'pip/24.0 {"implementation":{"name":"CPython","version":"3.11.9"},"installer":{"name":"pip","version":"24.0"},"python":"3.11.9","setuptools_version":"68.1.2","system":{"name":"Linux","release":"6.7.12-amd64"}}'


    parsed_url = urllib.parse.urlparse(url)

    assert parsed_url.scheme == 'https'
    hostname = parsed_url.netloc

    rbody = b'GET ' + parsed_url.path.encode() + b' HTTP/1.1\r\n' \
        b'Host: ' + hostname.encode() + b'\r\n' \
        b'User-Agent: ' + user_agent + b'\r\n' \
        b'Accept: */*\r\n' \
        b'Accept-Encoding: gzip, deflate, br\r\n' \
        b'Connection: Keep-Alive\r\n' \
        b'Range: bytes=0-2\r\n' \
        b'\r\n'

    bsize = 2**12
    sent_size = 0
    received_size = 0

    to_send = times

    context = ssl.create_default_context()

    with socket.create_connection((hostname, 443)) as sock:
        with context.wrap_socket(sock, server_hostname=hostname) as ssock:
            ssock.settimeout(1)
            while to_send > 0:
                try:
                    repetitions = 50 if to_send > 50 else to_send
                    sent_size += ssock.send(rbody * repetitions)
                    to_send -= repetitions
                except TimeoutError:
                    print('Receiving responses...')
                    while True:
                        try:
                            data = ssock.recv(bsize)
                            received_size += len(data)
                        except TimeoutError:
                            print('Received')
                            break

                print(f'Sent {times - to_send} requests. {int(((times - to_send) / times) * 100)}%')
    print(f'received={received_size}\nsent={sent_size}')


def main():

    if len(sys.argv) != 3:
        sys.exit(f'Usage: {sys.argv[0]} url times')

    url = sys.argv[1]
    times = int(sys.argv[2])

    download(url, times)


if __name__ == '__main__':
    main()
