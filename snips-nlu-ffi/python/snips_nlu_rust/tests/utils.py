from __future__ import unicode_literals

from pathlib import Path

ROOT_PATH = Path(__file__).parent.parent.parent.parent.parent
TEST_DATA_PATH = ROOT_PATH / "data" / "tests"
SAMPLE_ENGINE_DIR = TEST_DATA_PATH / "models" / "trained_engine"
SAMPLE_ENGINE_ZIP_PATH = TEST_DATA_PATH / "models" / "trained_engine.zip"

with SAMPLE_ENGINE_ZIP_PATH.open(mode='rb') as f:
    SAMPLE_ENGINE_ZIP_BYTES = bytearray(f.read())
