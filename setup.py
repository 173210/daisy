#!/usr/bin/env python
# Copyright (C) 2016  173210 <root.3.173210@live.com>
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

import glob
import setuptools
import sys

setuptools.setup(
	name = "daisy",
	version = "0",
	description = "A companion of Kagucho, a club in Tokyo University of Science",
	url = "http://kagucho.net/",
	author = "173210",
	license = "GPLv3+",
	classifiers = [
		"Development Status :: 1",
		"Environment :: X11 Applications :: Qt",
		"Intended Audience :: End Users/Desktop",
		"License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
		"Natural Language :: Japanese",
		"Operating System :: OS Independent",
		"Programming Language :: Python :: 3.5",
		"Programming Language :: Python :: 3 :: Only"
	],
	packages = ["daisy"],
	entry_points = { "console_scripts": ["daisy=daisy:main"] },
	data_files = [(sys.prefix + "/share/daisy", glob.glob("share/daisy/*"))]
)
