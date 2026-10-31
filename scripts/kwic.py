import re,sys,os,unicodedata
pat=re.compile(sys.argv[1],re.I)
skip=re.compile(sys.argv[2]) if len(sys.argv)>2 and sys.argv[2] else None
W=int(sys.argv[3]) if len(sys.argv)>3 else 160
seen=set()
for root,_,fs in os.walk('1_sanskr'):
  for f in sorted(fs):
    if not f.endswith('.txt'): continue
    p=os.path.join(root,f)
    if skip and skip.search(p): continue
    t=unicodedata.normalize('NFC',open(p,encoding='utf-8',errors='replace').read())
    t2=re.sub(r'\s+',' ',t)
    for m in pat.finditer(t2):
      ctx=t2[max(0,m.start()-W):m.end()+W]
      key=re.sub(r'[^a-zāīūṛṝḷṅñṭḍṇśṣṃḥ]','',ctx[W-40:W+60].lower())
      if key in seen: continue
      seen.add(key)
      print(f"### {p}\n{ctx}\n")
