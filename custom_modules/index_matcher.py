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
import pandas as pd

configuration = {
    # You can create as many inputs as you want.
    'in': {
        'baseline_dataset': {
            'label': 'Baseline dataset',
            'type': 'dataframe',
            'order': 1,
            'description': 'Baseline dataset for mapping index and movieId'
        },
        'request_input': {
            'label': 'Input',
            'type': ['dataframe','array','dict'],
            'order': 2,
            'description': 'Request input',
        },
    },

    # You can also create as many outputs as you want
    'out': {
        'result': {
            'label': 'index',
            'type': 'dataframe',
            'order': 1,
            'description': 'Cosine similarity matrix index',
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
    baseline_dataset = in_data["baseline_dataset"]
    indices = pd.Series(baseline_dataset.index, index=baseline_dataset["movieId"]).drop_duplicates()

    request_input = in_data["request_input"]
    movieId = request_input.iloc[0]["movieId"]

    idx = indices[movieId]

    # The output of your function must be an "out_data" mapping dictionary, each key is as specified in configuration
    out_data = {
        'result': idx,
    }

    # Return this map of output data
    return out_data
# ----------------------------------------------------------------------------------------------------------------------
