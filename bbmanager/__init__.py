# Importing directly from __init__ is never good practice, but in the case of
# application portability using Pyramid - this is the best option.
from .gateways.portability import include_me

# :(
