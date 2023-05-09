# Copyright (c) Kuba Szczodrzyński 2023-05-09.

from glob import glob
from os import makedirs
from shutil import rmtree, copyfile
from os.path import dirname, join, basename, exists, isfile

extra_dir = join(dirname(__file__), "examples")

for file in glob("example/*.c"):
    if not file.endswith(".c"):
        continue
    if file in ["panu_demo.c", "sco_demo_util.c", "ant_test.c"]:
        continue

    example = basename(file)[:-2]
    example_dir = join("examples", example)
    src_dir = join(example_dir, "src")

    if isfile(file.replace(".c", ".gatt")):
        print("Skipping", example, "as it uses a GATT DB (not supported yet)")
        continue

    if exists(example_dir):
        rmtree(example_dir)
    makedirs(src_dir, exist_ok=True)

    copyfile(file, join(src_dir, basename(file)))
    copyfile(join(extra_dir, "main.c"), join(src_dir, "main.c"))
    copyfile(join(extra_dir, "platformio.ini"), join(example_dir, "platformio.ini"))

    if example in ["hfp_ag_demo", "hfp_hf_demo", "hsp_ag_demo", "hsp_hs_demo"]:
        copyfile(join("example", "sco_demo_util.c"), join(src_dir, "sco_demo_util.c"))
        copyfile(join("example", "sco_demo_util.h"), join(src_dir, "sco_demo_util.h"))
