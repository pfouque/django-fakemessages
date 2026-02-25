from __future__ import annotations

import pathlib
from subprocess import run
from typing import Any

from django.conf import settings
from django.core.management.base import BaseCommand

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
        run(  # noqa: S603
            [  # noqa: S607
                "podebug",
                "--rewrite=classified",
                LOCALE_PATH / settings.LANGUAGE_CODE,
                LOCALE_PATH / settings.FAKE_LANGUAGE_CODE,
            ],
            check=True,
        )
