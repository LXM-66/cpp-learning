"""下载：python download.py <url> <out>  —— 写 .part，完成后改名，带重试"""
import sys, time, os, urllib.request

url, out = sys.argv[1], sys.argv[2]
part = out + ".part"
have = os.path.getsize(part) if os.path.exists(part) else 0

for attempt in range(1, 6):
    try:
        hdr = {"User-Agent": "Mozilla/5.0"}
        if have:
            hdr["Range"] = f"bytes={have}-"
        mode = "ab" if have else "wb"
        t = time.time()
        with urllib.request.urlopen(urllib.request.Request(url, headers=hdr), timeout=60) as r:
            total = int(r.headers.get("Content-Length", 0)) + have
            with open(part, mode) as f:
                while True:
                    chunk = r.read(262144)
                    if not chunk:
                        break
                    f.write(chunk)
                    have += len(chunk)
                    if have % (4 << 20) < 262144:
                        sp = (have - (os.path.getsize(part) - have)) / max(time.time() - t, .1) / 1024
                        print(f"\r{have/1048576:7.1f}/{total/1048576:.1f} MB  {sp:6.0f} KB/s", end="", flush=True)
        if total and have < total:
            raise RuntimeError(f"incomplete {have}/{total}")
        os.replace(part, out)
        print(f"\nOK {out}  {have/1048576:.1f} MB  {time.time()-t:.0f}s")
        break
    except Exception as e:
        print(f"\n[try {attempt}/5] {type(e).__name__}: {e}", flush=True)
        have = os.path.getsize(part) if os.path.exists(part) else 0
        time.sleep(3)
else:
    sys.exit("FAILED")
