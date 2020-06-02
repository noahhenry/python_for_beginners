# A module is simply a file that containes code...
import converters_module
# note: we can import specific functions from a module
from converters_module import lbs_to_kg

print(converters_module.kg_to_lbs(70))

print(lbs_to_kg(100))