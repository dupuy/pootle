#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2009,2013-2013 Zuza Software Foundation
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

""" Dynamic loading of hooks for update and commit """


import logging


def hook(project, hooktype, file, *args, **kwargs):
    """
    project should be the projectcode of any project.
    hooktype should be "initialize", "precommit", "postcommit",
    "pretemplateupdate", "preupdate", or "postupdate".
    file should be the absolute path of the file (project dir for initialize).

    Other arguments depend on the hooktype:
        initialize should have "languagecode" as an additional argument.
        precommit should have "author" and "message" as additional arguments.
        postcommit should have "success" as an additional argument.
        pretemplateupdate, preupdate, postupdate have no additional arguments.

    Return value depends on the hooktype:
        precommit returns an array of strings indicating what files to commit.
        preupdate returns the pathname of the file to update
        initialize, postcommit, and postupdate return is not used.
        pretemplateupdate returns a boolean indicating if the file should be
                          updated from template.

    """
    logger = logging.getLogger('pootle.scripts.hooks')
    try:
        activehook = __import__(project, globals(), locals(), [])
        if (hasattr(activehook, hooktype) and
                callable(getattr(activehook, hooktype))):
            logger.debug("Executing hook %s for project %s on file %s",
                         hooktype, project, path)
            return getattr(activehook, hooktype)(path, *args, **kwargs)
    except ImportError, e:
        raise ImportError(e)
    except StandardError:
        logger.exception("Exception in project (%s) hook (%s) for file (%s)",
                         project, hooktype, path)
    else:
        logger.debug("Imported %s, but it is not a suitable %s hook",
                     activehook.__file__, hooktype)
        raise ImportError("Imported %s, but it is not a suitable %s hook" %
                          (activehook.__file__, hooktype))
