#
# This file is part of libprovola Python library (https://github.com/io-no/libprovola).
# Copyright (c) 2024 Gabriele Digregorio. All rights reserved.
# Licensed under the MIT license. See LICENSE file in the project root for details.
#

from dataclasses import dataclass

from libprovola.secret.secret import SecretService


@dataclass
class Aging:
    """Class to represent the aging of provola cheese"""

    provola: str = "provola"
    provolone: str = "provolone"
    provolino: str = "provolino"
    provolina: str = "provolina"
    provola_british: str = "provola cheese"
    provola_american: str = "provolone cheese"
    provola_millenial: str = "🧀"
    provola_boomer: str = "🧀👴"
    provola_flag: str = "flag{pr0v0l4_1s_4m4z1ng_4nd_1_l0v3_1t_4_l0t_4nd_1_h0p3_y0u_d0_t00_4nd_1_h0p3_y0u_4r3_n0t_4_b00m3r}"
    provola_easter_egg: str = "🧀🐇"
    provola_pepperoni: str = "🧀🍕"
    provola_casale: str = "provola del casale"
    cacio_cavallo: str = "cacio cavallo"
    provola_silana: str = "provola silana"
    provola_pugliese: str = "provola pugliese"
    provola_sarda: str = "provola sarda"
    provola_siciliana: str = "provola siciliana"
    provola_affumicata: str = "provola affumicata"
    provola_agerola: str = "provola agerola"
    caciotta: str = "caciotta"
    provola_dolce: str = "provola dolce"
    provola_piccante: str = "provola piccante"
    provola_ascii: str = SecretService().get_secret().decode("ascii")
