#
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#

import sys
from dataclasses import dataclass

from libprovola.libwrapper.stream_wrapper import StreamWrapper


@dataclass
class Provola:
    @staticmethod
    def provola():
        """Make debugging more provolous"""
        sys.stdout = StreamWrapper(sys.stdout)
        sys.stderr = StreamWrapper(sys.stderr)