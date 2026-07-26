#pragma once

#include "esphome/core/component.h"
#include "esphome/core/automation.h"
#include "esphome/core/helpers.h"

namespace esphome {
namespace tab5_camera {

class Tab5Camera : public Component {
 public:
  void setup() override;
  void loop() override;
  void dump_config() override;
  float get_setup_priority() const override { return setup_priority::HARDWARE; }

  void set_frame_size(uint16_t width, uint16_t height);
  void set_jpeg_quality(uint8_t quality);
  void set_vertical_flip(bool flip);
  void set_horizontal_mirror(bool mirror);

 protected:
  bool init_camera_();
  void capture_frame_();
  void send_snapshot_to_ha_(const std::vector<uint8_t> &data);

  uint16_t frame_width_{1600};
  uint16_t frame_height_{1200};
  uint8_t jpeg_quality_{10};
  bool vertical_flip_{false};
  bool horizontal_mirror_{false};
  bool camera_initialized_{false};
  
  void *camera_handle_{nullptr};
  void *video_handle_{nullptr};
};

}  // namespace tab5_camera
}  // namespace esphome
