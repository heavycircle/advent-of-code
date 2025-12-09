import collections as cl
import pathlib
import re

from .logger import get_logger

logger = get_logger()

LANG_MAP = {".py": "Python", ".c": "C", ".bash": "Bash", ".asm": "ASM"}

ROOT = pathlib.Path(".")
README = ROOT / "README.md"


def count_solves() -> dict[str, int]:
    counts = cl.defaultdict(int)
    ext = set(LANG_MAP.keys())

    for path in ROOT.rglob("*"):
        if path.suffix in ext:
            name = LANG_MAP[path.suffix]
            counts[name] += 1

    return dict(counts)


def update_readme():
    if not README.exists():
        logger.error(f"{README} not found!")
        return
    content = README.read_text()

    counts = count_solves()
    langs = list(LANG_MAP.values())
    new_content = content

    for lang, count in counts.items():
        if lang in langs:
            pattern = re.compile(rf"(\|\s*{re.escape(lang)}\s*\|\s*)\d+(\s*\|)", re.IGNORECASE)
            replace = rf"\1{count}\2"

            tmp_content = re.sub(pattern, replace, new_content)
            if new_content == tmp_content:
                logger.warning(f"Could not update solve count for {lang}")

            new_content = tmp_content

    README.write_text(new_content)
    logger.info("README Updated")
