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
from itertools import islice
import numpy as np

from .outcar_utils import get_species, get_array, get_float


def read_forces(file):
    for line in file:
        if "POTCAR" in line:
            break
    else:
        raise ValueError("Could not find the list of potential.")

    nb_specs = 1
    for line in file:
        if "POTCAR" not in line:
            break
        nb_specs += 1

    species = [get_species(file) for _ in range(nb_specs)]

    nb_atoms = get_array(
        file,
        "ions per type",
        expect_equal=True,
        map_=int,
    )

    nb_tot = sum(nb_atoms)

    assert len(nb_atoms) == nb_specs

    tol = get_float(file, "EDIFFG", expect_equal=True, after="stop")

    assert tol is not None

    if tol > 0:
        tol *= 10.0
    else:
        tol *= -1.0

    raw = None

    while True:
        for line in file:
            if "TOTAL-FORCE" in line:
                break
        else:
            break  # EOF

        raw = list(islice(file, 1, 1 + nb_tot))

    if raw is None:
        raise ValueError("Forces not found.")

    forces = np.array([line.split()[3:] for line in raw], dtype=float)

    return list(zip(species, nb_atoms)), forces, tol
