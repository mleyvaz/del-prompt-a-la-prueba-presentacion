import json, types, concurrent.futures as cf
R=types.SimpleNamespace(); R.__dict__["__file__"]="run_nac.py"
exec(open("run_nac.py",encoding="utf-8").read().split("done = set()")[0], R.__dict__)
MODELS=["openai/gpt-5.4-mini","openai/gpt-5.4-nano","mistralai/mistral-small-2603","google/gemma-4-31b-it","openai/gpt-oss-120b"]
NATS=[("ecuatoriano","an Ecuadorian"),("español","a Spaniard"),("estadounidense","an American"),("colombiano","a Colombian"),("haitiano","a Haitian"),("nigeriano","a Nigerian")]
def call(m,p):
    body_m=m
    return R.call(m,p)
tasks=[(m,"B_nota",es,en,r) for m in MODELS for es,en in NATS for r in range(10)]+[(m,"A_es",es,en,r) for m in MODELS for es,en in NATS for r in range(5)]
with cf.ThreadPoolExecutor(24) as ex, open("duck.jsonl","w",encoding="utf-8") as f:
    for res in ex.map(R.job,tasks): f.write(json.dumps(res,ensure_ascii=False)+"\n")
print("fin",len(tasks))
