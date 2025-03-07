#  This file is part of Alea-Bot (https://github.com/AMA2018/ALEA.AI)
#  Copyright (c) 2025 AMA2018, All rights reserved.
#
#  Alea is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either
#  version 3.0 of the License, or (at your option) any later version.
#
#  Alea is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#  General Public License for more details.
#
#  You should have received a copy of the GNU General Public
#  License along with Alea-Bot. If not, see <https://www.gnu.org/licenses/>.

PROJECT_NAME = "Alea-Bot"
AUTHOR = "AMA2018"
VERSION = "1.0.0"  # major.minor.revision => don't forget to also update the setup.py version


def _use_module_local_tentacles():
    import sys
    import os
    import appdirs
    if os.getenv("USE_CUSTOM_TENTACLES", "").lower() == "true":
        # do not use alea_bot/imports tentacles
        # WARNING: in this case, all the required tentacles imports still have to work
        # and therefore be bound to another tentacles folder
        return
    # import tentacles from user-appdirs/imports directory
    dirs = appdirs.AppDirs(PROJECT_NAME, AUTHOR, VERSION)
    internal_import_path = os.path.join(dirs.user_data_dir, "imports")
    sys.path.insert(0, internal_import_path)


# run this before any other code as only alea_bot module-local tentacles should be used
_use_module_local_tentacles()

try:
    # import tentacles from alea_bot/imports directory after "_use_local_tentacles()" call
    from tentacles.Meta.Keywords import *
    # populate tentacles config helpers
    import octobot_tentacles_manager.loaders as loaders
    import alea_bot.internal.octobot_mocks as octobot_mocks
    loaders.reload_tentacle_by_tentacle_class(
        tentacles_path=octobot_mocks.get_imported_tentacles_path()
    )
    # do not expose those when importing this file
    loaders = octobot_mocks = None

except ImportError:
    # tentacles not available during first install
    pass

from alea_bot.constants import *
from alea_bot.api import *
from alea_bot.model import *
from alea_bot.ai import *
