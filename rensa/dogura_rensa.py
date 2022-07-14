import markovify
import pandas as pd
import re


def df_for_text(data):
    text = ""

    for w in data:
        w = re.sub(r"[【】≪≫「」『』＠（）～＿・]", "", w)
        w = re.sub(r"[()\[\]@_~\"\'|]", "", w)
        w = re.sub(r"\u3000", "", w)
        w = re.sub(r" ", "", w)
        w = re.sub(r"。", "。\n", w)
        w += " "
        text += w

    # print(text)
    return text

def markoving(text):
    text_model = markovify.NewlineText(text, state_size=3)
    print(re.sub(" ", "", text_model.make_short_sentence(100, tries=100)))

    with open("model/text_model.json", "w") as f:
        f.write(text_model.to_json())

df = pd.read_csv("2093_28841.csv")
# print(df)
text = df_for_text(df.iloc[:, 3])
markoving(text)
