# Finisher

This is simply an image with the intent to create containers that run for a specific duration (or duration pattern) and successfully complete.

## Prerequisites

* Docker Engine: This particular Dockerfile doesn't do anything special, so you're likely safe going back to something like 1.10.0 or something ancient if you're really into self-harm.  I'm going to recommend version 18.01 for sanity's sake.

## Building

Currently building images using GitHub Actions and publishing to Dockerhub

Building a Local Image:

```bash
docker build -t <image name> .
```

## Running

### Supported Environment Variables

| Name | Values | Description | Default |
| ---- | ---- | ----- | ---- |
| RANDOM | string containing some permution of "yes" or "no" | The container will run: between 1 and LIMIT if "yes", or LIMIT seconds if "no" | "yes" |
| LIMIT | integer | Specifies the current running behavior's time limit | 20 |

Note: The RANDOM environment variable description is actually a lie. It either takes something "yes" like (YES, yES, yeS, etc.) or anything else.  If it's not yes-like, it's a "no".  So if you don't want it to run for a random duration, you can set RANDOM to "Defenestration" and get what you like without knowing how to spell "no".


```bash
docker run -i -e RANDOM=yes -e LIMIT=10 digitalgoetz/finisher:1.0.0
```
