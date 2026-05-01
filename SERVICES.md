# Service Inventory

_Auto-generated 2026-05-01 15:18 UTC — do not edit manually._

**17 services** across **12 stacks**

## arr-stack

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `deunhealth` | `deunhealth` | `qmcgaw/deunhealth:v0.3.0` | — | `always` |
| `qbittorrent` | `qbittorrent` | `lscr.io/linuxserver/qbittorrent:5.1.4-r3-ls450` | `8080:8080` `6881:6881` | `unless-stopped` |
| `prowlarr` | `prowlarr` | `lscr.io/linuxserver/prowlarr:2.3.5.5327-ls142` | `9696:9696` | `unless-stopped` |
| `sonarr` | `sonarr` | `lscr.io/linuxserver/sonarr:4.0.17.2952-ls305` | `8989:8989` | `unless-stopped` |
| `radarr` | `radarr` | `lscr.io/linuxserver/radarr:6.1.1.10360-ls299` | `7878:7878` | `unless-stopped` |

## flaresolverr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `flaresolverr` | `flaresolverr` | `ghcr.io/flaresolverr/flaresolverr:v3.4.6` | `${PORT:-8191}:8191` | `unless-stopped` |

## heimdall

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `heimdall` | `heimdall` | `ghcr.io/linuxserver/heimdall:v2.7.6-ls341` | `11080:80` `11443:443` | `always` |

## homarr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `homarr` | `homarr` | `ghcr.io/homarr-labs/homarr:v1.59.3` | `7575:7575` | `unless-stopped` |

## homeassistant

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `homeassistant` | `homeassistant` | `lscr.io/linuxserver/homeassistant:2026.4.4` | `8123:8123` | `unless-stopped` |

## jackett

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `jacket` | `jackett` | `linuxserver/jackett:0.24.1807` | `9117:9117` | `unless-stopped` |

## jellyfin

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `jellyfin` | `jellyfin` | `jellyfin/jellyfin:10.11.8` | `8096:8096` `8920:8920` `7359:7359/udp` `1900:1900/udp` | `unless-stopped` |

## nginx

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `nginx-proxy-manager` | `nginx-proxy-manager` | `jc21/nginx-proxy-manager:2.14.0` | `80:80` `443:443` `81:81` | `unless-stopped` |

## open-webui

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `openwebui` | `open-webui` | `ghcr.io/open-webui/open-webui:v0.9.2` | `3030:8080` | `unless-stopped` |

## overseerr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `overseerr` | `overseerr` | `lscr.io/linuxserver/overseerr:v1.35.0-ls159` | `5055:5055` | `unless-stopped` |

## pihole

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `pihole` | `pihole` | `pihole/pihole:2026.04.1` | `53:53/tcp` `53:53/udp` `80:80/tcp` | `unless-stopped` |

## rustdesk-server

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `rustdesk-hbbs` | `rustdesk-hbbs` | `rustdesk/rustdesk-server:1.1.15` | — | `unless-stopped` |
| `rustdesk-hbbr` | `rustdesk-hbbr` | `rustdesk/rustdesk-server:1.1.15` | — | `unless-stopped` |

