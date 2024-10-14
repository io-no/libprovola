#
# This file is part of libprovola Python library (https://github.com/io-no/libprovola).
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#

from __future__ import annotations
from libprovola.libaging.libaging import libaging

class StreamWrapper:
    """A class to wrap a stream and make debugging more provolous"""

    def __init__(self: StreamWrapper, original_stream: object) -> None:
        """Initialize the StreamWrapper with the original stream
        
        Args:
            original_stream (object): The original stream to wrap
            
        Returns:
            None
        """
        self.original_stream = original_stream

    def write(self: StreamWrapper, message: str) -> None:
        """Overwrite the write method of the original stream
        
        Args:
            message (str): The message to write
            
        Returns:
            None
        """
        if message != "\n" and message != "":
            message = libaging.get_age() + "\n" + message
        self.original_stream.write(message)

    def __getattr__(self: StreamWrapper, attr: str) -> object:
        """Forward all other method calls to the original stream
        
        Args:
            attr (str): The attribute to get
        
        Returns:
            object: The attribute of the original stream
        """
        return getattr(self.original_stream, attr)
