hr, cc, ts = map(int, input().split())

if hr > 50 and ts > 500 and cc > 7:
    print("grade=10")
else:
    print("grade=0")

if ts > 500 and cc > 7:
    print("grade=8")
else:
    print("grade=0")

if hr > 50 and cc > 7 and ts <= 500:
    print("grade=9")
else:
    print("grade=7")

