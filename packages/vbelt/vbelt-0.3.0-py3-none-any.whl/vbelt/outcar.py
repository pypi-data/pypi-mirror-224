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
import collections
from .outcar_utils import get_float


def normal_end(file):
    for line in tail(file, 20):
        if "General timing and accounting informations" in line:
            return True
    return False


def converged(oszicar, outcar, tol=None):
    with open(outcar) as f:
        if tol is None:
            _tol = get_float(f, "EDIFF ", after="stopping", expect_equal=True)
            if _tol is None:
                raise ValueError("Could not find the EDIFF tolerance.")
        else:
            _tol = tol
        if not normal_end(f):
            return False, _tol, None

    with open(oszicar) as f:
        t = tail(f, 2)
        second_to_last = next(t)
        last = next(t)

    try:
        ediff = float(second_to_last.split()[3])
    except ValueError:
        return False, _tol, None

    return ((abs(ediff) < _tol and "F=" in last), _tol, abs(ediff))


def tail(it, n):
    return iter(collections.deque(it, maxlen=n))
