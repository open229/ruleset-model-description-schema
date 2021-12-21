from schema229.util_229 import strip__extra_data_element_fields_from_dict

TEST_SCHEMA_SOURCE_DICT = {
    "Integer": {"Object Type": "Data Type", "Description": "Keep this one"},
    "FluidLoop": {
        "Object Type": "Data Group",
        "Data Elements": {
            "id": {
                "Description": "Keep this"
            },
            "pump_power_per_flow_rate": {
                "Description": "Keep this",
                "foo": "Remove this",
                "bar": "Remove this"
            },
        },
    },
}

EXTRA_KEYS = ["foo", "bar"]


def test__strip__extra_data_element_fields_from_dict():
    assert strip__extra_data_element_fields_from_dict(EXTRA_KEYS, TEST_SCHEMA_SOURCE_DICT) == {
        "Integer": {"Object Type": "Data Type", "Description": "Keep this one"},
        "FluidLoop": {
            "Object Type": "Data Group",
            "Data Elements": {
                "id": {"Description": "Keep this"},
                "pump_power_per_flow_rate": {
                    "Description": "Keep this"
                },
            }
        }
    }
