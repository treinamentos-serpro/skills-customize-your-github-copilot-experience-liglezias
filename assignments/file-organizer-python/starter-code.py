from pathlib import Path
import shutil

SOURCE_DIR = Path("sample-files")
DESTINATION_DIR = Path("organized-files")


def get_category(file_path):
    raise NotImplementedError


def build_plan():
    raise NotImplementedError


def show_plan(plan):
    raise NotImplementedError


def execute_plan(plan):
    raise NotImplementedError


def main():
    plan = build_plan()
    show_plan(plan)
    execute_plan(plan)


if __name__ == "__main__":
    main()
