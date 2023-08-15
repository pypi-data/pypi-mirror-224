# Copyright 2023 OpenSynergy Indonesia
# Copyright 2023 PT. Simetri Sinergi Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    bpjs_kesehatan_number = fields.Char(
        string="BPJS Kesehatan",
        compute=lambda s: s._compute_identification(
            "bpjs_kesehatan_number",
            "BPJS-KES",
        ),
        inverse=lambda s: s._inverse_identification(
            "bpjs_kesehatan_number",
            "BPJS-KES",
        ),
        search=lambda s, *a: s._search_identification("BPJS-KES", *a),
    )
    bpjs_ketenagakerjaan_number = fields.Char(
        string="BPJS Ketenagakerjaan",
        compute=lambda s: s._compute_identification(
            "bpjs_ketenagakerjaan_number",
            "BPJS-KER",
        ),
        inverse=lambda s: s._inverse_identification(
            "bpjs_ketenagakerjaan_number",
            "BPJS-KER",
        ),
        search=lambda s, *a: s._search_identification("BPJS-KER", *a),
    )
