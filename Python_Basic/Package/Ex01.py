# use this with travel folder

# package is a collection of modules
# with import, the very last path after . 
# should be either module or package

# import travel.thailand
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# with from keyword, you can have the class
# as the last word of the command
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamePackage()
# trip_to.detail()



from travel import *
# trip_to = vietnam.VietnamePackage()
# trip_to.detail()

# the above is erroneous bc we didn't define __all__
# programmer can decide what can and cannot be included in __all__

trip_to = vietnam.VietnamPackage()
trip_to.detail()

# the lines below malfunction bc __all__ does not include thailand
# trip_to = thailand.ThailandPackage()
# trip_to.detail()