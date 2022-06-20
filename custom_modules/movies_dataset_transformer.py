# --------------------------- movies_dataset_transformer custom module ------------------------------------------------


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

configuration = {
    # You can create as many inputs as you want.
    'in': {
        'input_1': {
            'label': 'Input dataset',
            'type': 'dataframe',
            'order': 1,
            'description': 'This is the dataset to process',
        },
    },

    # You can also create as many outputs as you want
    'out': {
        'result': {
            'label': 'Resulting dataframe',
            'type': 'dataframe',
            'order': 1,
            'description': 'This is the resulting dataframe',
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
    data["genres"] = [genre.replace("|", " ") for genre in data["genres"]]

    # The output of your function must be an "out_data" mapping dictionary, each key is as specified in configuration
    out_data = {
        'result': data,
    }

    # Return this map of output data
    return out_data
# ----------------------------------------------------------------------------------------------------------------------
