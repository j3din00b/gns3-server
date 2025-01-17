#
# Copyright (C) 2015 GNS3 Technologies Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


class NodeError(Exception):
    def __init__(self, message, original_exception=None):
        super().__init__(message)
        if isinstance(message, Exception):
            message = str(message)
        self._message = message
        self._original_exception = original_exception

    def __repr__(self):
        return self._message

    def __str__(self):
        return self._message


class ImageMissingError(Exception):
    """
    Raised when an image is missing
    """

    def __init__(self, image):
        super().__init__(f"The image '{image}' is missing")
        self.image = image
