#
# unkeyUnlimitedPrm.py
#
def unlimitadd(*values):
   if values:
     if isinstance(values[0], (int, float)):
       result = 0
     elif isinstance(values[0], str):
       result = ''
     for val in values:
        result += val
   else:
     result = 0
   return result
#
