"""测速：各取 2MB，算 KB/s。用法 python speedtest.py <url> [url2 ...]"""
import sys, time, urllib.request

UA = {'User-Agent': 'Mozilla/5.0', 'Range': 'bytes=0-2097151'}


def probe(url):
    t = time.time()
    try:
        req = urllib.request.Request(url, headers=UA)
        data = urllib.request.urlopen(req, timeout=30).read()
        dt = time.time() - t
        return f"{len(data)/1024/dt:8.1f} KB/s   {dt:5.1f}s   {url}"
    except Exception as e:
        return f"{'FAIL':>8}          {type(e).__name__}: {e}   {url}"


for u in sys.argv[1:]:
    print(probe(u), flush=True)
