# importing the whole pakcage
import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# import the specific function from package...
from ecommerce.shipping import calc_shipping # note: can comma separate function names
calc_shipping()

# import just a module
from ecommerce import shipping
shipping.calc_shipping()