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
        'baseline_dataset': {
            'label': 'Baseline dataset',
            'type': 'dataframe',
            'order': 1,
            'description': 'This is the baseline dataset used to build the model'
        },
        'predictions': {
            'label': 'Predictions',
            'type': ['dict', 'dataframe', 'array'],
            'order': 2,
            'description': 'This is the result of the prediction by using the model',
        }
    },

    # You can also create as many outputs as you want
    'out': {
        'result': {
            'label': 'Recommended movies',
            'type': 'dataframe',
            'order': 1,
            'description': 'Recommended movies',
        }
    },

    # The parameters are shown when double-clicking the module or using the menu on its right while in edit mode.
    'params': {
        # Read the documentation for more details on the kind of parameters and options available in SmartPredict.
        'num_elements': {
            'label': 'Number of elements',
            'type': 'int',
            'order': 1,
            'description': 'Number of elements to recommend to the user',
            'default': 10
        }
    }
}


# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------------------- CUSTOM MODULE FUNCTION --------------------------------------------------

# This is a normalized function, it must take "in_data" , "param", "logger" as parameters.
# The name of this function should also contain "custom_module" in it.
def custom_module_function(in_data: dict, param: dict, logger: Logger) -> dict:
    baseline_dataset = in_data["baseline_dataset"]
    predictions = in_data["predictions"]
    num_elements = param["num_elements"]

    result = predictions[1:num_elements+1]
    result = [i[0] for i in result]
    result = baseline_dataset.iloc[result]

    # The output of your function must be an "out_data" mapping dictionary, each key is as specified in configuration
    out_data = {
        'result': result,
    }

    # Return this map of output data
    return out_data
# ----------------------------------------------------------------------------------------------------------------------
