import os, sys, pprint

print("❶  Current working dir:", os.getcwd())
print("❷  First three entries on sys.path:")
pprint.pp(sys.path[:3])

print("❸  Listing of current folder:")
pprint.pp(os.listdir("."))

print("❹  Listing of 'models' folder (if it exists):")
if os.path.isdir("models"):
    pprint.pp(os.listdir("models"))
else:
    print("‼️  'models' directory not found at this level.")

try:
    import models
    print("✅  import models   --> SUCCESS")
except ModuleNotFoundError as e:
    print("⛔️  import models   -->", e)
