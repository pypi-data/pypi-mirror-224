# vbelt: The VASP user toolbelt.
# Copyright (C) 2023  Théo Cavignac
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
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
import re


def parse_tag(line):
    line_ = line
    if "#" in line_:
        line_, *_ = line_.split("#")

    if "!" in line_:
        line_, *_ = line_.split("!")

    if "=" not in line_:
        return None

    tag, val = [e.strip() for e in line_.split("=")]

    return (tag, val)


def get_value(source, tag, default, cast=float):
    for line in source:
        res = parse_tag(line)
        if res and res[0] == tag:
            return cast(res[1])

    return default


def parse_incar(source, tags):
    with open(source) as f:
        lines = f.readlines()

    values = {}

    for tag, params in tags.items():
        values[tag] = get_value(lines, tag, **params)

    return values
