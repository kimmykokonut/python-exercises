'''This calculates time to bake a lasagna'''

EXPECTED_BAKE_TIME = 40
ONE_LAYER = 2

def bake_time_remaining(elapsed_bake_time):
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    '''time to prepare each layer is 2 minutes'''
    return number_of_layers * ONE_LAYER
    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    '''Calculate total elapsed cooking time (prep + bake)
    returns the total number of minutes of active cooktime
    '''
    return preparation_time_in_minutes(number_of_layers) + elapsed_bake_time

print(EXPECTED_BAKE_TIME) #should be 40
print(bake_time_remaining(5)) #should be 35
print(preparation_time_in_minutes(5)) #should be 10
print(elapsed_time_in_minutes(5, 10)) #should be 20