# Tab5-HA-HMI

# THIS IS FOR THE TAB5 VERSION 1 ONLY! #

ESPHome + LVGL dashboard for the M5Stack Tab5, designed to integrate with Home Assistant.

## What this project is

This repository contains multiple ESPHome YAML configurations and assets for a touchscreen HMI, including:

- Main UI config: `tab5-ha-hmi.yaml`
- Alternate/special configs:
- Custom external component: `external_components/tab5_camera/`
- UI assets: `images/`, `logos/`, `LVGL/`

## Requirements

- M5Stack Tab5 hardware version 1
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

## Screenshots and assets

Current assets included in this repository:

- UI/visual reference:

  ![Heater panel](images/heater.jpg)

- Service/app logos used by the media UI:
  - ![Amazon](logos/amazon.png)
  - ![Apple TV](logos/appletv.png)
  - ![Disney](logos/disney.png)
  - ![Netflix](logos/netflix_logo.png)
  - ![YouTube](logos/youtube.png)

If you want, replace these files with your own assets while keeping the same filenames to avoid YAML changes.

## Troubleshooting

Common ESPHome issues and quick fixes:

1. Build fails with missing secrets
  - Confirm `secrets.yaml` exists in the repo root.
  - Confirm every `!secret` key used in your YAML exists in `secrets.yaml`.

2. Upload fails over network
  - Verify device and computer are on the same network.
  - Try USB upload once, then retry OTA:

```bash
esphome run tab5-ha-hmi.yaml --device /dev/tty.usbmodem*
```

3. Home Assistant entities show as unknown/unavailable
  - Confirm API encryption key matches between ESPHome and Home Assistant.
  - Confirm each `entity_id` exists in Home Assistant and has a valid state.
  - Restart the ESPHome device after major entity/config changes.

4. External component errors
  - Validate `external_components/tab5_camera/manifest.json` is present and valid.
  - Run config check first to catch schema/path issues early:

```bash
esphome config tab5-ha-hmi.yaml
```

5. Missing media files during compile
  - Ensure all referenced local media files exist at the expected paths.
  - Remove or update references to files you do not use.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE).
