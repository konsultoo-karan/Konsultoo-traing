#
# <!--◦ Name of the country - Char-->
# <!--        ◦ Short Code of the country - Char-->
#
# <!--        ◦ States - One2many - res.state.ksc-->
#
# <!--    • Action-->
#
# <!--    • Menu-->
#
# <!--        ◦ Countries-->
#
# <!--        ◦ Parent Menu - Localization -> Localization-->
#
# <!--    • View-->
#
# <!--        ◦ Tree, Form, Search-->
#
# <!--    • Search View-->
#
# <!--        ◦ One should be able to search by country name-->
#
# <!--        ◦ One should be able to search by country code-->
#
# <!--    • Security - Create appropriate security group-->

from odoo import fields, models, api
from odoo.exceptions import ValidationError

class ResCountryKsc(models.Model):
    _name = "res.country.ksc"
    _description = 'Country KSC'

    name = fields.Char("Name of the country")
    code = fields.Char("Short Code of the country")
    state_ids = fields.One2many(comodel_name='res.state.ksc', inverse_name='country_id', string='States')