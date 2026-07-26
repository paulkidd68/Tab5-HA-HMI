# Tab5-HA-HMI

ESPHome + LVGL dashboard for the M5Stack Tab5, designed to integrate with Home Assistant.

## What this project is

This repository contains multiple ESPHome YAML configurations and assets for a touchscreen HMI, including:

- Main UI config: `tab5-ha-hmi.yaml`
- Alternate/special configs:
  - `camera 2 display.yaml`
  - `day schedule.yaml`
  - `night_shedule.yaml`
  - `debug update bin.yaml`
  - `update WC next bin.yaml`
- Custom external component: `external_components/tab5_camera/`
- UI assets: `images/`, `logos/`, `LVGL/`

## Requirements

- M5Stack Tab5 hardware
- Home Assistant instance (API integration)
- ESPHome (recommended with Python virtual environment)

## Quick start

1. Clone the repo.
2. Create your local secrets file (not committed):
   - `secrets.yaml`
3. Add required secrets used by your YAML, for example:

```yaml
wifi_ssid: "YOUR_WIFI_SSID"
wifi_password: "YOUR_WIFI_PASSWORD"
tab5_api_encryption_key: "YOUR_API_KEY"
tab5_ota_password: "YOUR_OTA_PASSWORD"
```

4. Build/validate:

```bash
esphome config tab5-ha-hmi.yaml
esphome compile tab5-ha-hmi.yaml
```

5. Flash or upload:

```bash
esphome upload tab5-ha-hmi.yaml
```

## Notes

- `.esphome/`, virtual environments, and local secrets are intentionally ignored in git.
- Keep `secrets.yaml` local only.
- The main branch is configured as `main`.

## License

No license file is currently included. If you want this project to be open source, add a license (for example MIT).
