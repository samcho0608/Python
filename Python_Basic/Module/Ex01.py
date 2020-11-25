# import theater_module

# theater_module.price(3) # 3 ppl. price to watch the movie
# theater_module.price_morning(4)
# theater_module.price_soldier(5)

# import theater_module as mv

# mv.price(3)
# mv.price_morning(4)
# mv.price_soldier(5)

# below lets us use the imported functions without the module name
# from theater_module import *
# price(3)
# price_morning(4)
# price_soldier(5)

# from theater_module import price, price_morning
# price(3)
# price_morning(4)
# price_soldier(5) erroneous bc not imported

from theater_module import price_soldier as price
price(3)
# even though we're calling price function
# it's actually talking abt price_soldier function
# bc we assigned that function the nickname price