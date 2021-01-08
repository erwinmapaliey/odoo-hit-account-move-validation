from odoo import api, fields, models
from odoo.exceptions import UserError

class AccountMove(models.Model):
   _inherit = 'account.move'

   @api.model
   def create(self, vals):
      lines = vals.get('line_ids',[])
      
      if not lines:
         raise UserError("You must insert line items before save")
      else:
         return super(AccountMove, self).create(vals)
   
