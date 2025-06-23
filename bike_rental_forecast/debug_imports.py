import os, sys, pprint

print("Current working dir:", os.getcwd())
print("First three entries on sys.path:")
pprint.pp(sys.path[:3])

print("Listing of current folder:")
pprint.pp(os.listdir("."))

print("Listing of 'models' folder (if it exists):")
if os.path.isdir("models"):
    pprint.pp(os.listdir("models"))
else:
    print("'models' directory not found at this level.")

try:
    import models
    print("import models   --> SUCCESS")
except ModuleNotFoundError as e:
    print("import models   -->", e)
