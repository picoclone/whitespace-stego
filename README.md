# Whitespace Stego (`whitespace-stego`)

**Category:** steganography · **Difficulty:** easy · **Points:** 150

Trailing spaces and tabs on each line encode a base64 blob in binary.

## Run it

```bash
docker build -t picoclone/whitespace-stego .
# `picoclone start whitespace-stego` (or the web UI) prints the docker run line with your
# PICOCLONE_SERVER + PICOCLONE_INSTANCE_TOKEN
```

## Recover the flag

The delivery blob is base64-encoded. Decode it to recover the flag.

The plaintext flag is never written to disk or served — only the encoded delivery blob
is. When you have it:

```bash
picoclone submit whitespace-stego 'picoclone{...}'
```

## Hints

- Map space/tab patterns to bits, then to ASCII.
- Decode the resulting base64.
