from io import BytesIO
from pathlib import Path
import tempfile
import unittest
from urllib.error import URLError

from brazil_data_map.download import download_public_file


class Response(BytesIO):
    def __enter__(self):
        return self

    def __exit__(self, *_):
        self.close()


class DownloadTests(unittest.TestCase):
    def test_download_retries_and_records_checksum(self) -> None:
        calls = []

        def opener(*_, **__):
            calls.append(True)
            if len(calls) == 1:
                raise URLError("temporary")
            return Response(b"public fixture")

        with tempfile.TemporaryDirectory() as temporary_directory:
            result = download_public_file("https://example.org/source", Path(temporary_directory) / "source.bin", opener=opener)

        self.assertEqual(len(calls), 2)
        self.assertEqual(result["bytes"], 14)

    def test_download_rejects_non_https_urls(self) -> None:
        with self.assertRaisesRegex(ValueError, "HTTPS"):
            download_public_file("http://example.org/source", Path("ignored"))
