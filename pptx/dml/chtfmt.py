# encoding: utf-8

"""
|ChartFormat| and related objects. |ChartFormat| acts as proxy for the `spPr`
element, which provides visual shape properties such as line and fill for
chart elements.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from .fill import FillFormat
from ..shared import ElementProxy
from ..util import lazyproperty


class ChartFormat(ElementProxy):
    """
    Provides access to visual shape properties such as line and fill.
    """

    __slots__ = ('_fill',)

    @lazyproperty
    def fill(self):
        """
        |FillFormat| instance for this object, providing access to fill
        properties such as fill color.
        """
        spPr = self._element.get_or_add_spPr()
        return FillFormat.from_fill_parent(spPr)
