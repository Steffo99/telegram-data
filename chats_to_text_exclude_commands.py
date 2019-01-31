import json
import os
file = open("data/result.json", encoding="utf8")
j = json.load(file)
file.close()

for chat in j["chats"]["list"]:
    if chat.get("name") is not None:
        chat_name = chat["name"]
    else:
        chat_name = "__UNNAMED__"
    filename = "exports/text/{}.txt".format("".join(i for i in chat_name if i not in "\\/:*?<>|!\"\'."))
    counter = 1
    while os.path.exists(filename):
        counter += 1
        filename = "exports/text/{}{}.txt".format("".join(i for i in chat_name if i not in "\\/:*?<>|!\"\'."),
                                                  counter)
    print(filename)
    file = open(filename, "w", encoding="utf8")
    for msg in chat["messages"]:
        if msg["type"] != "message":
            continue
        if isinstance(msg["text"], list):
            text = ""
            for obj in msg["text"]:
                if isinstance(obj, str):
                    text += obj
                if isinstance(obj, dict):
                    text += obj["text"]
        else:
            text = msg["text"]
        if text.startswith("/"):
            continue
        file.write(text.replace("\n", " ") + "\n")
    file.close()
