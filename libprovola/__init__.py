#
# This file is part of libprovola Python library (https://github.com/io-no/libprovola).
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#

from .libprovola import Provola as __Provola
from .libaging.libaging import libaging

try:
    from rich.traceback import install
except ImportError:
    pass
else:
    install()

__all__ = ["libaging"]
__Provola.provola()
