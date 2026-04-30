#!/usr/bin/env python3
"""Generate SERVICES.md from all compose.yaml files in the repo."""

from datetime import datetime, timezone
from pathlib import Path
import yaml


def find_compose_files(root="."):
    return sorted(Path(root).rglob("compose.yaml"))


def format_ports(ports):
    if not ports:
        return "—"
    out = []
    for p in ports:
        if isinstance(p, (str, int)):
            out.append(f"`{p}`")
        elif isinstance(p, dict):
            pub = p.get("published", "")
            tgt = p.get("target", "")
            proto = p.get("protocol", "")
            entry = f"{pub}:{tgt}" if pub else str(tgt)
            if proto and proto != "tcp":
                entry += f"/{proto}"
            out.append(f"`{entry}`")
    return " ".join(out)


def main():
    rows = []
    for compose_file in find_compose_files():
        stack = compose_file.parent.name
        if stack in (".", "Homelab_Containers"):
            stack = "root"

        with open(compose_file) as f:
            data = yaml.safe_load(f) or {}
        services = data.get("services") or {}

        for name, svc in services.items():
            if not svc:
                continue
            rows.append(
                {
                    "stack": stack,
                    "service": name,
                    "container": svc.get("container_name", "—"),
                    "image": svc.get("image", "—"),
                    "ports": format_ports(svc.get("ports", [])),
                    "restart": svc.get("restart", "—"),
                    "network": svc.get("network_mode", "bridge"),
                }
            )

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    stacks = sorted(set(r["stack"] for r in rows))

    with open("SERVICES.md", "w") as f:
        f.write("# Service Inventory\n\n")
        f.write(f"_Auto-generated {now} — do not edit manually._\n\n")
        f.write(f"**{len(rows)} services** across **{len(stacks)} stacks**\n\n")

        for stack in stacks:
            stack_rows = [r for r in rows if r["stack"] == stack]
            f.write(f"## {stack}\n\n")
            f.write("| Service | Container | Image | Ports | Restart |\n")
            f.write("|---------|-----------|-------|-------|---------|\n")
            for r in stack_rows:
                f.write(
                    f"| `{r['service']}` | `{r['container']}` | `{r['image']}` "
                    f"| {r['ports']} | `{r['restart']}` |\n"
                )
            f.write("\n")

    print(f"Generated SERVICES.md: {len(rows)} services across {len(stacks)} stacks.")


if __name__ == "__main__":
    main()
