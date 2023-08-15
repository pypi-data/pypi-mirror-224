# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    ektp_number = fields.Char(
        string="E-KTP",
        compute=lambda s: s._compute_identification(
            "ektp_number",
            "ektp",
        ),
        inverse=lambda s: s._inverse_identification(
            "ektp_number",
            "ektp",
        ),
        search=lambda s, *a: s._search_identification("ektp", *a),
    )
    kartu_keluarga_number = fields.Char(
        string="Kartu Keluarga",
        compute=lambda s: s._compute_identification(
            "kartu_keluarga_number",
            "kk",
        ),
        inverse=lambda s: s._inverse_identification(
            "kartu_keluarga_number",
            "kk",
        ),
        search=lambda s, *a: s._search_identification("kk", *a),
    )
    passport_number = fields.Char(
        string="Passport",
        compute=lambda s: s._compute_identification(
            "passport_number",
            "pp",
        ),
        inverse=lambda s: s._inverse_identification(
            "passport_number",
            "pp",
        ),
        search=lambda s, *a: s._search_identification("pp", *a),
    )
