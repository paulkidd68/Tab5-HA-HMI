import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.const import (
    CONF_ID,
)

CODEOWNERS = ["@pakiddier"]

tab5_camera_ns = cg.esphome_ns.namespace("tab5_camera")
Tab5Camera = tab5_camera_ns.class_("Tab5Camera", cg.Component)

CONF_FRAME_SIZE = "frame_size"
CONF_JPEG_QUALITY = "jpeg_quality"
CONF_VERTICAL_FLIP = "vertical_flip"
CONF_HORIZONTAL_MIRROR = "horizontal_mirror"

FRAME_SIZES = {
    "UXGA": (1600, 1200),
    "SXGA": (1280, 960),
    "HD": (1280, 720),
    "XGA": (1024, 768),
    "SVGA": (800, 600),
    "VGA": (640, 480),
}

CONFIG_SCHEMA = cv.Schema(
    {
        cv.GenerateID(): cv.declare_id(Tab5Camera),
        cv.Optional(CONF_FRAME_SIZE, default="UXGA"): cv.enum(FRAME_SIZES, upper=True),
        cv.Optional(CONF_JPEG_QUALITY, default=10): cv.int_range(min=0, max=63),
        cv.Optional(CONF_VERTICAL_FLIP, default=False): cv.boolean,
        cv.Optional(CONF_HORIZONTAL_MIRROR, default=False): cv.boolean,
    }
).extend(cv.COMPONENT_SCHEMA)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    
    # Set frame size
    frame_size = FRAME_SIZES[config[CONF_FRAME_SIZE]]
    cg.add(var.set_frame_size(frame_size[0], frame_size[1]))
    
    # Set other parameters
    cg.add(var.set_jpeg_quality(config[CONF_JPEG_QUALITY]))
    cg.add(var.set_vertical_flip(config[CONF_VERTICAL_FLIP]))
    cg.add(var.set_horizontal_mirror(config[CONF_HORIZONTAL_MIRROR]))
