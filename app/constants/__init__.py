"""
Constant Module
"""
USERNAME_RULE="""
1) Username must be 6-30 characters long\n
2) Username may only contain:\n
- Uppercase and lowercase letters\n
- Numbers from 0-9 and\n
- Special characters _ .\n
3) Username may not:\n
- Begin or finish with characters _ - .\n
- Have more than one sequential character _ - . inside
"""

NAME_RULE="""
1) Name must be max 50 characters long\n
2) Name may only contain:\n
- Uppercase and lowercase letters\n
- Numbers from 0-9 and\n
- Special characters _\n
3) Name may not:\n
- Begin or finish with characters _\n
- Have more than one sequential character _ inside
"""

ENV_FILE = '.env'

INVOICE_RULE="""
- Invoice is a list of order's products with its price format:
- json.dumps(Dict of {"product_id": amount})
- examples: order of 4 adidas (Product 11) and 2 samsung phone (Product 8)
should have Invoice string like "{"11": 4, "8": 2}"
"""