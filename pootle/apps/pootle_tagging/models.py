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

import locale

from django.db import models
from django.utils.translation import ugettext_lazy as _

from taggit.models import GenericTaggedItemBase

from pootle_misc.baseurl import l


'''
class PootleTaggedItem(GenericTaggedItemBase):


class PootleTag(models.Model):
    directory = models.ForeignKey('pootle_app.Directory', db_index=True)
    content_object = models.ForeignKey('tag')
    name = models.TextField(_('Tagname'))

    def __unicode__(self):
        return self.name

    def get_absolute_url(self):
        return l(self.directory.pootle_path + 'tags/%d' % self.id)
'''
