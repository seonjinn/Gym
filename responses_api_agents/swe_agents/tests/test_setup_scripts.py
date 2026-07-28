# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import subprocess
from pathlib import Path

import pytest


SETUP_SCRIPTS_DIR = Path(__file__).resolve().parent.parent / "setup_scripts"
RESOLVE_JQ_ARCH = SETUP_SCRIPTS_DIR / "resolve_jq_arch.sh"


@pytest.mark.parametrize(
    ("host_arch", "jq_arch"),
    [
        ("x86_64", "amd64"),
        ("aarch64", "arm64"),
        ("arm64", "arm64"),
    ],
)
def test_resolve_jq_arch_maps_supported_linux_architectures(
    host_arch: str, jq_arch: str
) -> None:
    result = subprocess.run(
        ["bash", str(RESOLVE_JQ_ARCH), host_arch],
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode == 0
    assert result.stdout.strip() == jq_arch


def test_resolve_jq_arch_rejects_unsupported_architecture() -> None:
    result = subprocess.run(
        ["bash", str(RESOLVE_JQ_ARCH), "riscv64"],
        capture_output=True,
        check=False,
        text=True,
    )

    assert result.returncode != 0
    assert "Unsupported architecture: riscv64" in result.stderr
