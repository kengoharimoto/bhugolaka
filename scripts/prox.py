import re,os,sys,unicodedata
a=re.compile(sys.argv[1]); b=re.compile(sys.argv[2]); D=int(sys.argv[3]); W=int(sys.argv[4])
roots=sys.argv[5:] or ['1_sanskr']
seen=set()
for R in roots:
 for root,_,fs in os.walk(R):
  for f in sorted(fs):
    if not f.endswith('.txt'): continue
    p=os.path.join(root,f)
    t=re.sub(r'\s+',' ',unicodedata.normalize('NFC',open(p,encoding='utf-8',errors='replace').read()))
    for m in a.finditer(t):
      win=t[max(0,m.start()-D):m.end()+D]
      if not b.search(win): continue
      ctx=t[max(0,m.start()-W):m.end()+W]
      k=re.sub(r'[^a-zāīūṛṅñṭḍṇśṣṃḥ]','',ctx[W-30:W+50])
      if k in seen: continue
      seen.add(k); print('###',p,'\n',ctx,'\n')
