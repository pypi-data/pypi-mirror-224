from nonebot_plugin_datastore import get_plugin_data
from strenum import StrEnum

CACHE_DIR = get_plugin_data().cache_dir
IMAGE_CACHE_DIR = CACHE_DIR / "images"
RECORD_CACHE_DIR = CACHE_DIR / "records"
VIDEO_CACHE_DIR = CACHE_DIR / "videos"

IMAGE_CACHE_DIR.mkdir(parents=True, exist_ok=True)
RECORD_CACHE_DIR.mkdir(parents=True, exist_ok=True)
VIDEO_CACHE_DIR.mkdir(parents=True, exist_ok=True)


class SupportedAdapter(StrEnum):
    onebot_v11 = "OneBot V11"
    onebot_v12 = "OneBot V12"
    console = "Console"
    kaiheila = "Kaiheila"
    qqguild = "QQ Guild"
    telegram = "Telegram"


class SupportedPlatform(StrEnum):
    qq = "qq"
    console = "console"
    kaiheila = "kaiheila"
    qqguild = "qqguild"
    telegram = "telegram"
    unknown = "unknown"
