from odoo import api, fields, models

class Rescity(models.Model):
        _name = 'res.city.ksc'
        _description = 'city information'


        name = fields.Char(string="Name ggg Of City")
        state_id = fields.Many2one(comodel_name='res.state.ksc', string='State Name ')


#
#         ◦ City
#         Name
#
#         ◦ State - M2O(res.state.ksc)
#
# • Action
#
# • Menu
#
# ◦ City
#
# ◦ Parent Menu - Localization -> Localization
#
# • View
#
# ◦ Tree, Search
#
# • Tree - Make tree editable, we don’t need form view
#
# • Search View
#
# ◦ One should be able to search be city name
#
# ◦ One should be able to search by state
#
# ◦ Group by state