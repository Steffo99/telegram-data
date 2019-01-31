import markovify
import os

filenames = list(os.walk("./exports/text"))[0][2]

for filename in filenames:
    with open(f"./exports/text/{filename}", encoding="utf8") as f:
        data = f.read()
    try:
        model = markovify.NewlineText(data, state_size=1)
        print(f"{filename} | {model.make_sentence()}")
    except Exception:
        continue
    json_string = model.to_json()
    with open(f"./exports/models/{filename.replace('.txt', '.json')}", "w", encoding="utf8") as f:
        f.write(json_string)
