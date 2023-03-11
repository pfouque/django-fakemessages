from __future__ import annotations

from django.conf import settings
from django.core.management import call_command


def test_simple():
    call_command("makemessages", "--locale", settings.LANGUAGE_CODE)
    call_command("fakemessages")
    call_command("compilemessages", "--locale", settings.LANGUAGE_CODE)
    call_command("compilemessages", "--locale", settings.FAKE_LANGUAGE_CODE)
