#!/usr/bin/env python3
"""Weekly image audit: lists all pinned images, flags :latest tags, checks Docker Hub for newer versions."""

import glob
import os
import sys
import time
import yaml
import requests
from pathlib import Path


def find_compose_files(root="."):
    return sorted(Path(root).rglob("compose.yaml"))


def extract_images(compose_file):
    with open(compose_file) as f:
        data = yaml.safe_load(f) or {}
    services = data.get("services") or {}
    return {name: svc["image"] for name, svc in services.items() if svc and "image" in svc}


def parse_image_ref(ref):
    if ":" in ref:
        image, tag = ref.rsplit(":", 1)
    else:
        image, tag = ref, "latest"
    return image, tag


def get_registry(image):
    first = image.split("/")[0]
    if "." in first or ":" in first:
        return first
    return "docker.io"


def dockerhub_latest_tag(image):
    """Return the most-recently-pushed non-meta tag from Docker Hub, or None on failure."""
    try:
        repo = image if "/" in image else f"library/{image}"
        url = f"https://hub.docker.com/v2/repositories/{repo}/tags?page_size=20&ordering=last_updated"
        resp = requests.get(url, timeout=10)
        if resp.status_code != 200:
            return None
        skip = {"latest", "edge", "beta", "nightly", "dev", "master", "main", "stable"}
        tags = [t["name"] for t in resp.json().get("results", []) if t["name"] not in skip]
        return tags[0] if tags else None
    except Exception:
        return None


def main():
    rows = []
    for compose_file in find_compose_files():
        stack = compose_file.parent.name if compose_file.parent.name != "." else "root"
        for service, ref in extract_images(compose_file).items():
            image, tag = parse_image_ref(ref)
            registry = get_registry(image)

            latest = None
            if registry == "docker.io":
                latest = dockerhub_latest_tag(image)
                time.sleep(0.2)  # be polite to Docker Hub rate limits

            rows.append(
                {
                    "stack": stack,
                    "service": service,
                    "image": image,
                    "tag": tag,
                    "registry": registry,
                    "latest": latest,
                    "unpinned": tag == "latest",
                    "update_available": bool(latest and latest != tag and tag != "latest"),
                }
            )

    summary_path = os.environ.get("GITHUB_STEP_SUMMARY", "/dev/stdout")
    with open(summary_path, "a") as out:
        out.write("# Weekly Image Audit\n\n")

        unpinned = [r for r in rows if r["unpinned"]]
        if unpinned:
            out.write("## Using `:latest` Tag\n\n")
            out.write("These services have unpinned versions — Renovate can't track them:\n\n")
            out.write("| Stack | Service | Image |\n|-------|---------|-------|\n")
            for r in unpinned:
                out.write(f"| `{r['stack']}` | `{r['service']}` | `{r['image']}` |\n")
            out.write("\n")

        updates = [r for r in rows if r["update_available"]]
        if updates:
            out.write("## Possible Updates (Docker Hub)\n\n")
            out.write("| Stack | Service | Current Tag | Latest Seen |\n|-------|---------|-------------|-------------|\n")
            for r in updates:
                out.write(f"| `{r['stack']}` | `{r['service']}` | `{r['tag']}` | `{r['latest']}` |\n")
            out.write("\n")
        elif not unpinned:
            out.write("All Docker Hub images appear up to date.\n\n")

        out.write("## Full Inventory\n\n")
        out.write("| Stack | Service | Image | Tag | Registry |\n")
        out.write("|-------|---------|-------|-----|----------|\n")
        for r in rows:
            flag = " ⚠️" if r["unpinned"] else (" ↑" if r["update_available"] else "")
            out.write(
                f"| `{r['stack']}` | `{r['service']}` | `{r['image']}` "
                f"| `{r['tag']}`{flag} | `{r['registry']}` |\n"
            )

    total = len(rows)
    problems = len(unpinned) + len(updates)
    print(f"Audit complete: {total} services checked, {problems} issue(s) flagged.")
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
