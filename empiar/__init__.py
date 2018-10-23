# **************************************************************************
# *
# * Authors:     Yaiza Rancel (cyrancel@cnb.csic.es)
# *              Yunior C. Fonseca Reyna (cfonseca@cnb.csic.es)
# *
# * Unidad de  Bioinformatica of Centro Nacional de Biotecnologia , CSIC
# *
# * This program is free software; you can redistribute it and/or modify
# * it under the terms of the GNU General Public License as published by
# * the Free Software Foundation; either version 2 of the License, or
# * (at your option) any later version.
# *
# * This program is distributed in the hope that it will be useful,
# * but WITHOUT ANY WARRANTY; without even the implied warranty of
# * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# * GNU General Public License for more details.
# *
# * You should have received a copy of the GNU General Public License
# * along with this program; if not, write to the Free Software
# * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA
# * 02111-1307  USA
# *
# *  All comments concerning this program package may be sent to the
# *  e-mail address 'scipion@cnb.csic.es'
# *
# **************************************************************************

"""
This package contains the protocols and data for EMPIAR
"""
#from plugin import _plugin
#from empiar.protocols.protocol_empiar_submission import EmpiarDepositor

import os
import pyworkflow.em

from pyworkflow.utils import Environ
from empiar.constants import *
from bibtex import _bibtex


_references = ['Voss2009']
_logo = 'EMPIAR_logo.png'


class Plugin(pyworkflow.em.Plugin):
    _homeVar = EMPIAR_HOME
    _pathVars = [EMPIAR_HOME]
    _supportedVersions = V1_0_0

    @classmethod
    def _defineVariables(cls):
        cls._defineEmVar(EMPIAR_HOME, 'empiar-1.0.0')
        cls._defineEmVar(ASCP_PATH,  os.path.expanduser('~/.aspera/connect/bin/ascp'))
        cls._defineEmVar(ASPERA_PASS, '')
        cls._defineEmVar(EMPIAR_TOKEN, '')

    @classmethod
    def getEnviron(cls):
        """ Setup the environment variables needed to launch Empiar. """
        environ = Environ(os.environ)
        environ.update({
            'PATH': Plugin.getHome(),
            'ASCP_PATH': os.path.expanduser('~/.aspera/connect/bin/ascp'),
        }, position=Environ.BEGIN)

        return environ

    @classmethod
    def isVersionActive(cls):
        return cls.getActiveVersion().startswith(V1_0_0)

    @classmethod
    def defineBinaries(cls, env):

        empiar_cmd = [('./aspera-connect-3.7.4.147727-linux-64.sh',
                       [cls.getVar(ASCP_PATH)])]
        env.addPackage('ascp',
                       url='https://download.asperasoft.com/download/sw/connect/3.7.4/aspera-connect-3.7.4.147727-linux-64.tar.gz',
                       default=True,
                       buildDir='ascp',
                       createBuildDir=True,
                       target='ascp/aspera-connect-3.7.4.147727-linux-64.sh',
                       commands=empiar_cmd)


pyworkflow.em.Domain.registerPlugin(__name__)




