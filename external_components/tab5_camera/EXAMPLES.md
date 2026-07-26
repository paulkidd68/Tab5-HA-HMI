# Example: Using Tab5 Camera with Home Assistant Automations

## Capture Snapshot Service

Once the Tab5 camera component is set up, you can call the capture snapshot service from Home Assistant:

### Service Call Example

```yaml
service: esphome.tab5_ha_hmi_capture_snapshot
data: {}
```

## Home Assistant Automation Example

### Capture on Motion Detection

```yaml
automation:
  - alias: "Capture Tab5 Camera on Motion"
    trigger:
      - platform: state
        entity_id: binary_sensor.motion_detector
        to: 'on'
    action:
      - service: esphome.tab5_ha_hmi_capture_snapshot
        data: {}
      - delay: '00:00:02'
      - service: notify.mobile_app
        data:
          message: "Motion detected - camera snapshot captured"
```

### Periodic Snapshot Capture

```yaml
automation:
  - alias: "Tab5 Camera Periodic Snapshot"
    trigger:
      - platform: time_pattern
        minutes: '/30'  # Every 30 minutes
    action:
      - service: esphome.tab5_ha_hmi_capture_snapshot
        data: {}
```

### Manual Capture Button

Add a button to your Home Assistant dashboard:

```yaml
type: button
name: Capture Camera Snapshot
tap_action:
  action: call-service
  service: esphome.tab5_ha_hmi_capture_snapshot
  data: {}
icon: mdi:camera
```

## Display Snapshot on Tab5 Screen

You can also capture and display the snapshot directly on the Tab5's LVGL display. This would require extending the component to:

1. Capture frame from camera
2. Convert to RGB565 format
3. Update LVGL image widget with the captured data

Example function to add:

```cpp
void Tab5Camera::display_on_lvgl() {
  // Capture frame
  std::vector<uint8_t> frame_data;
  // ... capture logic ...
  
  // Convert to RGB565
  // ... conversion logic ...
  
  // Update LVGL widget
  // lv_img_set_src(img_widget, frame_buffer);
}
```

## Integration with Other Home Assistant Features

### Send to Telegram

```yaml
automation:
  - alias: "Send Tab5 Snapshot to Telegram"
    trigger:
      - platform: state
        entity_id: binary_sensor.doorbell
        to: 'on'
    action:
      - service: esphome.tab5_ha_hmi_capture_snapshot
        data: {}
      - delay: '00:00:02'
      - service: telegram_bot.send_photo
        data:
          target: !secret telegram_chat_id
          caption: "Doorbell pressed"
```

### Security System Integration

```yaml
automation:
  - alias: "Tab5 Camera Security Capture"
    trigger:
      - platform: state
        entity_id: alarm_control_panel.home
        to: 'triggered'
    action:
      - repeat:
          count: 5
          sequence:
            - service: esphome.tab5_ha_hmi_capture_snapshot
              data: {}
            - delay: '00:00:05'
```
