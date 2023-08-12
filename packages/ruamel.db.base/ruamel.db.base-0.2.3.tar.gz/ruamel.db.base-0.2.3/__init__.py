# coding: utf-8

from __future__ import print_function
from __future__ import absolute_import

_package_data = dict(
    full_package_name='ruamel.db.base',
    version_info=(0, 2, 3),
    __version__='0.2.3',
    version_timestamp='2023-04-13 08:59:05',
    author='Anthon van der Neut',
    author_email='a.van.der.neut@ruamel.eu',
    description='base for db handling',
    entry_points=None,
    install_requires=[],
    # py26= ["ruamel.ordereddict"],
    # py27= ["ruamel.ordereddict"],
    license='Copyright Ruamel bvba 2007-2016',
    # status="α",
    # data_files="",
    universal=1,
)


version_info = _package_data['version_info']
__version__ = _package_data['__version__']

from .diffdict import diff_dict, revert_dict                           # noqa
from .microsecstamp import micro_sec_stamp, micro_sec_stamp_to_time    # noqa
from .key_nr import key4_nr, nr_key4, key4_ge                          # noqa
from .log import no_log, debug                                         # noqa
