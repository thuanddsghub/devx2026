"""Tests for the devx command-line interface."""

import io
import unittest
from contextlib import redirect_stdout

from devx.cli import main


class CliTest(unittest.TestCase):
    """Tests for the devx CLI."""

    def test_main_prints_ready_message(self) -> None:
        """The CLI prints the expected readiness message."""
        output = io.StringIO()
        with redirect_stdout(output):
            main()

        self.assertEqual(output.getvalue(), "devx is ready\n")
