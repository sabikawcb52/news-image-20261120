"""Entry for make.fun "Sum up 20 November's world news in one image".

Writes the front-page image of Friday 20 November 2026 to /output/entry.png.
The image is drawn in the repository (entry.png, 1024x1024, PNG); this
program only copies it, so it runs with no network and writes the same
bytes on every run.
"""

import os
import shutil  # copyfile keeps the image bytes identical on every run

HERE = os.path.dirname(os.path.abspath(__file__))


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(os.path.join(HERE, "entry.png"), "/output/entry.png")
    os.chmod("/output/entry.png", 0o644)


if __name__ == "__main__":
    main()
