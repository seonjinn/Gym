#!/bin/bash
# SPDX-FileCopyrightText: Copyright (c) 2026 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

set -euo pipefail

host_arch="${1:-$(uname -m)}"

case "$host_arch" in
    x86_64|amd64)
        echo "amd64"
        ;;
    aarch64|arm64)
        echo "arm64"
        ;;
    *)
        echo "Unsupported architecture: $host_arch" >&2
        exit 1
        ;;
esac
