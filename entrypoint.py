#!/usr/bin/env python3
"""Whitespace Stego — real mini-challenge (whitespace-stego)."""
import base64, hashlib, json, os, struct, sys, zlib, wave, io, math, random, re, textwrap
sys.path.insert(0, "/challenge/_shared")
from fetch_material import fetch_material

CHALLENGE_KEY = os.environ.get("CHALLENGE_KEY", None)


def main():
    mat = fetch_material()
    with open("/challenge/flag.enc", "w") as f:
        f.write(mat["delivery_blob"])
    msg = CHALLENGE_KEY or "BASE64"
    poem = "Roses are red,\nViolets are blue,\nSteganography hides,\nA clue for you.\n"
    ws = []
    for ch in msg:
        for i in range(7, -1, -1):
            ws.append("\t" if (ord(ch) >> i) & 1 else " ")
    poem = poem.replace("\n", " \n").rstrip() + "".join(ws) + "\n"
    with open("/challenge/poem.txt", "w") as f:
        f.write(poem)
    print("Whitespace Stego: poem.txt trailing whitespace spells BASE64 or key; decode flag.enc.")


if __name__ == "__main__":
    main()
