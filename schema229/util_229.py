import copy
import os
import yaml

'''
Utility functions specific to the 229 project
'''

def remove_file(path):
    '''Removes a file with the given path if it exists'''
    if os.path.exists(path):
        os.remove(path)

def strip_extra_data_element_fields_from_yaml(extra_keys, src_path, dest_path):
    """Remove specified data elements from all Data Groups in a schema source yaml file

    Parameters
    ----------
    extra_keys : [str]
        A list of keys in the Data Group, Data Elements that are to be removed
    src_path : string
        Path to a schema-source yaml file
    dest_path : string
        Path to the yaml file to store the result

    """
    with open(src_path, 'r') as src_file:
        src_dict = yaml.safe_load(src_file)
    stripped_dict = strip__extra_data_element_fields_from_dict(extra_keys, src_dict)
    with open(dest_path, 'w') as dest_file:
        yaml.dump(stripped_dict, dest_file, sort_keys=False)



def strip__extra_data_element_fields_from_dict(extra_keys, schema_source_dict):
    """Remove specified data elements from all Data Groups

    Parameters
    ----------
    extra_keys : [str]
        A list of field names in data elements that are to be removed
    schema_source_dict : dict
        The dictionary generated from a /schema-source yaml file.

    Returns
    -------
    dict
        A new dictionary that is a copy of the original schema_source_dict
        with the specified fields removed
    """
    # Perform a deep copy to avoid mutating the passed obj
    new_schema_source_dict = copy.deepcopy(schema_source_dict)

    for top_key in new_schema_source_dict:
        # Assumes that new_obj is a dictionary of dictionaries that have "Object Type" fields
        top_dict = new_schema_source_dict[top_key]
        if top_dict["Object Type"] == "Data Group":
            # Assumes that Data Groups have a "Data Elements" field that is a dict
            data_elements = top_dict["Data Elements"]
            for data_element_key in data_elements:

                # Filter out the fields of the data element with keys in extra_keys
                new_data_element = {
                    key: val for key, val in
                        data_elements[data_element_key].items()
                        if key not in extra_keys
                }
                top_dict["Data Elements"][data_element_key] = new_data_element

    return new_schema_source_dict
