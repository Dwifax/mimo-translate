#!/usr/bin/env python3
"""MiMo Translate - Multi-language translator using Xiaomi MiMo API."""
import os, argparse
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def translate(text, target_lang):
    resp = client.chat.completions.create(model="mimo-v2.5", messages=[
        {"role": "system", "content": f"Translate to {target_lang}. Preserve formatting. Only output translation."},
        {"role": "user", "content": text}])
    return resp.choices[0].message.content

if __name__ == "__main__":
    p = argparse.ArgumentParser(); p.add_argument("--text"); p.add_argument("--file"); p.add_argument("--to", required=True); p.add_argument("-o")
    a = p.parse_args()
    if a.text: print(translate(a.text, a.to))
    elif a.file:
        with open(a.file) as f: content = f.read()
        out = a.o or f"{a.file}.{a.to}"
        with open(out, "w") as f: f.write(translate(content, a.to))
        print(f"Translated -> {out}")
