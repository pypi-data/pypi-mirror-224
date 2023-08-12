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
from vbelt.outcar_utils import get_species, get_val


class Potcar:
    """A small subset of the informations stored in POTCAR.

    Only for reading purpose, most of the information is ignored.
    """

    def __init__(self, species):
        self.species = species

    @classmethod
    def from_file(self, path):
        species_info = []

        with open(path) as f:
            while True:
                name = get_species(f)

                if name is None:
                    break

                pomass_and_zval = get_val(
                    f, before="POMASS", after="mass", expect_equal=True
                )
                a, b = pomass_and_zval.split(";")
                mass = float(a.strip())
                zval = float(b.split("=")[1].strip())

                enlimits = get_val(f, before="ENMAX", after="eV", expect_equal=True)

                a, b = enlimits.split(";")
                enmax = float(a.strip())
                enmin = float(b.split("=")[1].strip())

                species_info.append(
                    {
                        "name": name,
                        "mass": mass,
                        "valence": zval,
                        "enmin": enmin,
                        "enmax": enmax,
                    }
                )

        return Potcar(species_info)


def predict_nelect(poscar, potcar):
    return sum(sp["valence"] * len(poscar.species[sp["name"]]) for sp in potcar.species)
