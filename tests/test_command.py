from __future__ import annotations

from pathlib import Path

from django.conf import settings
from django.core.management import call_command


def test_simple():
    locale_dir = Path(settings.LOCALE_PATHS[0])
    fake_locale_dir = locale_dir / settings.FAKE_LANGUAGE_CODE / "LC_MESSAGES"
    fake_po = fake_locale_dir / "django.po"
    fake_mo = fake_locale_dir / "django.mo"

    fake_po.unlink(missing_ok=True)
    fake_mo.unlink(missing_ok=True)

    call_command("makemessages", "--locale", settings.LANGUAGE_CODE)
    call_command("fakemessages")
    assert fake_po.exists()
    assert fake_po.stat().st_size > 0

    call_command("compilemessages", "--locale", settings.LANGUAGE_CODE)
    call_command("compilemessages", "--locale", settings.FAKE_LANGUAGE_CODE)
    assert fake_mo.exists()
    assert fake_mo.stat().st_size > 0
