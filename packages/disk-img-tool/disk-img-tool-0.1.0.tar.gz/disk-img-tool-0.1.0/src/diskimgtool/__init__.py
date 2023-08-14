#!/usr/bin/env python3
# Copyright (C) 2023 Leandro Lisboa Penz <lpenz@lpenz.org>
# This file is subject to the terms and conditions defined in
# file 'LICENSE', which is part of this source code package.


import logging
import os
import re
import subprocess
import tempfile
from contextlib import contextmanager
from time import sleep
import parted
import shutil


def log():
    if not hasattr(log, "logger"):
        log.logger = logging.getLogger(os.path.basename("diskimgtool"))
    return log.logger


def cmd(c, check=True, capture=False):
    log().info(f'+ {" ".join(c)}')
    if capture:
        return subprocess.check_output(c, encoding="ascii")
    else:
        return subprocess.run(c, check=check)


@contextmanager
def chdir(d):
    log().info(f"+ cd {d}")
    cwd = os.getcwd()
    os.chdir(d)
    try:
        yield
    finally:
        log().info("+ cd -")
        os.chdir(cwd)


@contextmanager
def loopback_setup(image):
    data = cmd(["kpartx", "-a", "-v", image], capture=True)
    for line in data.split("\n"):
        if line:
            log().info(f"  {line}")
    try:
        m = re.search(r"add map (loop[0-9]+)p.*", data)
        if not m:
            raise Exception("regex didnt match")
        loop = f"/dev/mapper/{m.group(1)}"
        yield loop
    finally:
        cmd(["kpartx", "-d", image], check=False)
        cmd(["sync"])


@contextmanager
def mount(src, dst, t="auto", bind=False, args=None):
    if bind:
        t = "none"
    c = ["mount", "-t", t]
    if bind:
        c.extend(["-o", "bind"])
    if args:
        c.extend(args)
    c.extend([src, dst])
    cmd(c)
    try:
        yield
    finally:
        for i in range(5):
            r = cmd(["umount", dst], check=False)
            if r.returncode == 0:
                return
            cmd(["lsof", dst], check=False)
            sleep(1)
        cmd(["umount", "-l", dst])


@contextmanager
def root_mounts(rootdir):
    with mount("dev", f"{rootdir}/dev", t="devtmpfs"):
        with mount("devpts", f"{rootdir}/dev/pts", t="devpts"):
            with mount("tmpfs", f"{rootdir}/dev/shm", t="tmpfs"):
                with mount("proc", f"{rootdir}/proc", t="proc"):
                    with mount("sysfs", f"{rootdir}/sys", t="sysfs"):
                        with mount("tmpfs", f"{rootdir}/run", t="tmpfs"):
                            dirs = [f"{rootdir}/run/lock", f"{rootdir}/run/shm"]
                            cmd(["mkdir", "-p"] + dirs)
                            yield


def chroot(rootdir, c):
    c = ["chroot", rootdir] + c
    return cmd(c)


@contextmanager
def image_fully_mounted(image):
    with tempfile.TemporaryDirectory(dir=os.getcwd()) as rootdir:
        with loopback_setup(image) as loop:
            with mount(f"{loop}p2", rootdir):
                with mount(f"{loop}p1", f"{rootdir}/boot"):
                    yield rootdir
