#
# This file is part of libprovola Python library (https://github.com/io-no/libprovola).
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#

from __future__ import annotations

from dataclasses import dataclass

from libprovola.libaging.aging import Aging


@dataclass
class LibAging:
    """A class to manage the aging of provola cheese"""

    aging: str = Aging.provola
    """The aging of the provola cheese"""

    def __new__(cls) -> LibAging:
        """Singleton pattern"""
        if not hasattr(cls, "instance"):
            cls.instance = super(LibAging, cls).__new__(cls)
        return cls.instance

    def set_age(self: LibAging, age: str) -> None:
        """Make the provola cheese age"""
        self.aging = getattr(Aging, age)

    def get_age(self: LibAging) -> str:
        """Get the provola cheese age"""
        return self.aging
    
libaging = LibAging()
