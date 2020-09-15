def pretty(a_dict, indent=0):
    '''
        Pretty prints a deep python dictionary with indent levels
    '''
    str_out = ""
    for key in sorted(a_dict):
        value = a_dict[key]

        str_out += '\t' * indent + str(key) + ': '
        if isinstance(value, dict):
            str_out += '\n' + pretty(value, indent+1)
        else:
            str_out += str(value) + '\n'
    return str_out

def get_methods_of_object(obj):
    '''
        Returns list of object's method names
    '''
    return [method_name for method_name in dir(obj) if callable(getattr(obj, method_name))]

import subprocess 

def ping(host):
    """
        Returns True if host (str) responds to a ping request.
    """
    command = ['ping', '-c', '1', host]
    return subprocess.call(command) == 0