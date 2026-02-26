from __future__ import annotations

import pathlib
import sys
from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand
from translate.tools import podebug

LOCALE_PATH = pathlib.Path(settings.LOCALE_PATHS[0])


class Command(BaseCommand):
    help = (
        "Generate fake translation files for settings.FAKE_LANGUAGE_CODE\n\n"
        "Based on podebug from translate-toolkit, it replaces all characters by '▮'"
        "(like if the NSA 'classified'), in order to spot easily untranslatied strings."
    )

    def handle(self, *args: Any, **options: Any) -> None:
        self.stdout.write(
            f"Generating fake locale {settings.FAKE_LANGUAGE_CODE} from {settings.LANGUAGE_CODE}"
        )
        argv = sys.argv
        try:
            sys.argv = [
                "podebug",
                "--rewrite=classified",
                str(LOCALE_PATH / settings.LANGUAGE_CODE),
                str(LOCALE_PATH / settings.FAKE_LANGUAGE_CODE),
            ]
            podebug.main()
        finally:
            sys.argv = argv
