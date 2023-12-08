import json
 
with open("./test.json", "rt", encoding="utf-8") as file:
    settings = json.load(file)
 
settings["eyes_pos"][0]["x"] = "pass"
 
with open("./test.json", "wt", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)

with open("./sw_templates.json", "rt", encoding="utf-8") as file:
    settings = json.load(file)
 
settings["test_2"] = "pass"
 
with open("./sw_templates.json", "wt", encoding="utf-8") as file:
    json.dump(settings, file, indent=4)