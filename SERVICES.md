# Service Inventory

_Auto-generated 2026-06-25 13:57 UTC — do not edit manually._

**17 services** across **12 stacks**

## arr-stack

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `deunhealth` | `deunhealth` | `qmcgaw/deunhealth:v0.3.0` | — | `always` |
| `qbittorrent` | `qbittorrent` | `lscr.io/linuxserver/qbittorrent:5.2.1_v2.0.13-ls460` | `8080:8080` `6881:6881` | `unless-stopped` |
| `prowlarr` | `prowlarr` | `lscr.io/linuxserver/prowlarr:2.4.0.5397-ls149` | `9696:9696` | `unless-stopped` |
| `sonarr` | `sonarr` | `lscr.io/linuxserver/sonarr:4.0.17.2952-ls313` | `8989:8989` | `unless-stopped` |
| `radarr` | `radarr` | `lscr.io/linuxserver/radarr:6.2.1.10461-ls305` | `7878:7878` | `unless-stopped` |

## flaresolverr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `flaresolverr` | `flaresolverr` | `ghcr.io/flaresolverr/flaresolverr:v3.5.0` | `${PORT:-8191}:8191` | `unless-stopped` |

## heimdall

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `heimdall` | `heimdall` | `ghcr.io/linuxserver/heimdall:v2.7.6-ls341` | `11080:80` `11443:443` | `always` |

## homarr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `homarr` | `homarr` | `ghcr.io/homarr-labs/homarr:v1.67.0` | `7575:7575` | `unless-stopped` |

## homeassistant

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `homeassistant` | `homeassistant` | `lscr.io/linuxserver/homeassistant:2026.6.4` | `8123:8123` | `unless-stopped` |

## jackett

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `jacket` | `jackett` | `linuxserver/jackett:0.24.2122` | `9117:9117` | `unless-stopped` |

## jellyfin

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `jellyfin` | `jellyfin` | `jellyfin/jellyfin:10.11.11` | `8096:8096` `8920:8920` `7359:7359/udp` `1900:1900/udp` | `unless-stopped` |

## nginx

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `nginx-proxy-manager` | `nginx-proxy-manager` | `jc21/nginx-proxy-manager:2.15.1` | `80:80` `443:443` `81:81` | `unless-stopped` |

## open-webui

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `openwebui` | `open-webui` | `ghcr.io/open-webui/open-webui:v0.9.6` | `3030:8080` | `unless-stopped` |

## overseerr

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `overseerr` | `overseerr` | `lscr.io/linuxserver/overseerr:v1.35.0-ls159` | `5055:5055` | `unless-stopped` |

## pihole

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `pihole` | `pihole` | `pihole/pihole:2026.06.0` | `53:53/tcp` `53:53/udp` `80:80/tcp` | `unless-stopped` |

## rustdesk-server

| Service | Container | Image | Ports | Restart |
|---------|-----------|-------|-------|---------|
| `rustdesk-hbbs` | `rustdesk-hbbs` | `rustdesk/rustdesk-server:1.1.15` | — | `unless-stopped` |
| `rustdesk-hbbr` | `rustdesk-hbbr` | `rustdesk/rustdesk-server:1.1.15` | — | `unless-stopped` |

