# ---------------------------------------------------- word_vectors_to_array custom module -------------------------------


# ---------------------------------------------------- IMPORTS ---------------------------------------------------------
# Your import statements can be written here.
# All builtins python package can be imported.
# Popular libraries for ML like tensorflow, sklearn,
# pandas, nltk are also supported.
# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------- CONFIGURATION ------------------------------------------------------
# Follow this convention when specifying the configuration of your module.
# The name of each input and output are up to you, but the structure of each one of them should be the same.
from logging import Logger
import numpy as np

configuration = {
    # You can create as many inputs as you want.
    'in': {
        'input_1': {
            'label': 'Vectorized data',
            'type': 'array',
            'order': 1,
            'description': 'This is the vectorizer data',
        }
    },

    # You can also create as many outputs as you want
    'out': {
        'result': {
            'label': 'Result of the operation',
            'type': 'array',
            'order': 1,
            'description': 'This is the result of the operation.',
        }
    },

    # The parameters are shown when double-clicking the module or using the menu on its right while in edit mode.
    'params': {
        # Read the documentation for more details on the kind of parameters and options available in SmartPredict.
    }
}


# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------------------- CUSTOM MODULE FUNCTION --------------------------------------------------

# This is a normalized function, it must take "in_data" , "param", "logger" as parameters.
# The name of this function should also contain "custom_module" in it.
def custom_module_function(in_data: dict, param: dict, logger: Logger) -> dict:
    data = in_data["input_1"]
    vectorized_genres = list(data["genres"])
    vectorized_genres = [list(element) for element in vectorized_genres]
    vectorized_genres = np.array(vectorized_genres)
    logger.debug("SHAPE: " + str(vectorized_genres.shape))
    out_data = {
        'result': vectorized_genres,
    }

    # Return this map of output data
    return out_data
# ----------------------------------------------------------------------------------------------------------------------
