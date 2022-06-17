

def validate_max_length(instance, attribute, value):

    if(len(value) > 255 or len(value) < 0):
        raise ValueError(f"{attribute} must be less than 255 characters.")