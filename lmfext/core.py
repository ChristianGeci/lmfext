from pathlib import Path
import numpy as np
import lmfit as lmf
import pandas as pd


def params_to_dict(params):
    param_dict = {}
    for name, param in params.items():
        param_dict[name] = {
            'value': param.value,
            'min': param.min,
            'max': param.max,
            'vary': param.vary,
            'expr': param.expr
        }
    return param_dict

def param_dict_to_df(param_dict):
    return pd.DataFrame.from_dict(param_dict, orient='index')

def write_params(params, filepath):
    param_dict = params_to_dict(params)
    df = param_dict_to_df(param_dict)
    df.to_csv(filepath, index_label='Parameter', sep='\t')

def make_params_file(model, filepath, prevent_overwriting = True, **kwargs):
    if Path(filepath).exists() and prevent_overwriting:
        print(f"file at {filepath} already exists")
        return
    params = model.make_params(**kwargs)
    write_params(params, filepath)


def read_params(filepath):
    parameters = lmf.Parameters()
    df = pd.read_csv(filepath, sep='\t')
    parameters_dict = df.to_dict()

    names = list(parameters_dict['Parameter'].values())
    hit_exception = False
    for index, name in enumerate(names):
        value = parameters_dict['value'][index]
        min = parameters_dict['min'][index]
        max = parameters_dict['max'][index]
        vary = parameters_dict['vary'][index]
        expr = parameters_dict['expr'][index]
        if type(expr) == float and np.isnan(expr):
            expr = None
        param = lmf.Parameter(name,
                              value = value,
                              min = min,
                              max = max,
                              vary = vary,
                              expr = expr,
                             )
        try:
            parameters.add(param)
        except Exception as e:
            print(f"failed to add parameter {name}: {e}")
            hit_exception = True
            continue

    if hit_exception:
        raise(Exception("Hit one or more errors, see above"))

    return parameters