import pytest
from cart import Cart, EmptyCartError
import sys


def test_save_report(tmp_path):
    
    f = tmp_path / "report.txt"
    f.write_text("매출 1000", encoding="utf-8")
    assert f.read_text(encoding="utf-8").startswith("매출")

def test_env(monkeypatch):

    monkeypatch.setenv("ENV", "test")
    import os
    assert os.getenv("ENV") == "test"