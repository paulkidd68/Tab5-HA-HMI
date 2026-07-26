# Tab5 Camera Custom Component

This is a custom ESPHome component for the M5Stack Tab5's SC2356 (SC202CS) camera sensor.

## Overview

The M5Stack Tab5 uses a MIPI-CSI camera interface which is not natively supported by ESPHome's standard `esp32_camera` component. This custom component provides a bridge between ESPHome and the ESP-IDF `esp_video` API included in the `espressif/m5stack_tab5` BSP component.

## Hardware Details

- **Camera Sensor**: SC2356 (also called SC202CS)
- **Interface**: MIPI-CSI, 2-lane
- **Maximum Resolution**: 1600x1200 (UXGA)
- **Reset Pin**: Controlled by GPIO expander (pi4ioe5v6408 #1, pin 6)
- **Image Formats**: RAW10, YUV422, RGB565

## Configuration

The required ESP-IDF components are already added to your configuration:

```yaml
esp32:
  framework:
    type: esp-idf
    components:
      - espressif/m5stack_tab5^1.2.0~1
      - espressif/esp_cam_sensor^2.1.0
      - espressif/esp_video^2.0.1
    sdkconfig_options:
      CONFIG_CAMERA_SC2336: "y"
      CONFIG_CAMERA_SC2336_AUTO_DETECT: "y"
      CONFIG_CAMERA_SC2336_AUTO_DETECT_MIPI_INTERFACE_SENSOR: "y"
      CONFIG_ESP_VIDEO_ENABLE: "y"
      CONFIG_MIPI_CSI_ISR_IRAM_SAFE: "y"
```

Then add the camera component to your ESPHome YAML:

```yaml
tab5_camera:
  id: tab5_cam
  frame_size: UXGA  # UXGA, SXGA, HD, XGA, SVGA, VGA
  jpeg_quality: 10  # 0-63, lower is better quality
  vertical_flip: false
  horizontal_mirror: false
```

## Available Frame Sizes

- **UXGA**: 1600x1200
- **SXGA**: 1280x960
- **HD**: 1280x720
- **XGA**: 1024x768
- **SVGA**: 800x600
- **VGA**: 640x480

## API Services

The component registers the following services in Home Assistant:

- `esphome.<device_name>_capture_snapshot`: Capture a snapshot from the camera

## Current Status

⚠️ **This is a skeleton implementation that requires completion.**

### What's Implemented
- ✅ Component structure and ESPHome integration
- ✅ Configuration schema
- ✅ API service registration
- ✅ Basic setup and configuration

### What Needs to be Completed

1. **ESP-IDF Video API Integration**
   - Initialize camera using `esp_cam_sensor` API
   - Configure MIPI-CSI controller using `esp_cam_ctlr_csi`
   - Set up video pipeline with `esp_video` API

2. **Frame Capture**
   - Implement actual frame capture from camera
   - Handle RAW to RGB/YUV conversion
   - JPEG encoding of captured frames

3. **Memory Management**
   - Proper buffer allocation for PSRAM
   - Frame buffer management
   - Memory cleanup

4. **Home Assistant Integration**
   - Send captured frames to Home Assistant
   - Implement camera entity in Home Assistant
   - Stream support (optional)

## Development Notes

### ESP-IDF Components (Already Configured)

The following components are now included in your configuration:
- ✅ `espressif/m5stack_tab5^1.2.0~1` - M5Stack Tab5 BSP
- ✅ `espressif/esp_cam_sensor^2.1.0` - Camera sensor drivers including SC2356
- ✅ `espressif/esp_video^2.0.1` - Video processing pipeline

These components provide all the necessary drivers and APIs for the camera.

### Key ESP-IDF APIs to Use

```cpp
// Camera sensor initialization
esp_cam_sensor_detect()
esp_cam_sensor_set_format()
esp_cam_sensor_start_stream()

// Video pipeline
esp_video_init()
esp_video_read()

// MIPI-CSI controller
esp_cam_ctlr_csi_new_sensor()
```

### References

- [ESP Camera Sensor Component](https://components.espressif.com/components/espressif/esp_cam_sensor)
- [M5Stack Tab5 BSP](https://components.espressif.com/components/espressif/m5stack_tab5)
- [ESP-IDF Camera Example](https://github.com/espressif/esp-bsp/tree/master/bsp/m5stack_tab5/examples/camera)

## Testing

To test the component:

1. Flash the ESPHome firmware to your Tab5
2. Call the service from Home Assistant:
   ```yaml
   service: esphome.tab5_ha_hmi_capture_snapshot
   ```

## Contributing

This component is a work in progress. Contributions to complete the ESP-IDF video API integration are welcome!

## License

Apache-2.0 (same as ESPHome)
