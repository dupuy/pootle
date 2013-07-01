# -*- coding: utf-8 -*-
#
# Copyright 2013 Zuza Software Foundation
#
# This file is part of Pootle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

"""
This file implements some tests using Django's unittest module. These will pass
when you run "manage.py test".
"""

from pootle_translationproject.models import TranslationProjectManager

from django.test import TestCase


class SimpleTest(TestCase):
    def test_basic_tagging(self):
        """
        Test tagging
        """
        enza = TranslationProjectManager.get_by_natural_key("en_ZA/pootle")

