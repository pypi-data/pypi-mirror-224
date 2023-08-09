# pylint: disable-msg=W0622
"""cubicweb-company application packaging information"""

modname = 'company'
distname = 'cubicweb-%s' % modname

numversion = (0, 9, 0)
version = '.'.join(str(num) for num in numversion)

license = 'LGPL'
description = 'company component for the CubicWeb framework'

author = 'Logilab'
author_email = 'contact@logilab.fr'
web = 'http://www.cubicweb.org/project/%s' % distname
classifiers = [
    'Environment :: Web Environment',
    'Framework :: CubicWeb',
    'Programming Language :: Python',
    'Programming Language :: JavaScript',
    ]

__depends__ = {'cubicweb': '>= 3.38.0,<3.39',
               'cubicweb-addressbook': None}
