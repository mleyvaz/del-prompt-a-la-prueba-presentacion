import json, os, concurrent.futures as cf
import types
R=types.SimpleNamespace()
src=open("run_nac.py",encoding="utf-8").read().split("done = set()")[0]
R.__dict__["__file__"]="run_nac.py"; exec(src,R.__dict__)
OUT="confirmacion.jsonl"
tasks=[("openai/gpt-5-mini","B_nota",es,en,r) for es,en in R.NATS for r in range(20)] + \
      [("openai/gpt-4o-mini","A_es",es,en,r) for es,en in R.NATS for r in range(10)]
with cf.ThreadPoolExecutor(24) as ex, open(OUT,"w",encoding="utf-8") as f:
    for res in ex.map(R.job,tasks): f.write(json.dumps(res,ensure_ascii=False)+"\n")
print("fin",len(tasks))
