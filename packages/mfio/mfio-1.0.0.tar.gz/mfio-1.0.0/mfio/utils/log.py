import sys
from loguru import logger

logger.configure(handlers=[
    {
        "sink": sys.stderr,
        "format": "<lvl>{message}</>",
        "colorize": True,
        "level":"INFO"
    },
    {
        "sink": '{time:YYYY-MM-DD-HH-mm}.log',
        "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} - {name}:{module}:{line:4} - {level:7} : {message}",
        "colorize": True,
        "level":"DEBUG"
    },
])
