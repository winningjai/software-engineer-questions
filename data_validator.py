import json

# It will check and return whether the data is duplicate or not
# Input: data_json[dict], data_key_values[dict]
# Output: [Boolean]
def check_duplicate(data_json, data_key_values):
    for key in data_key_values.keys():
        if data_key_values[key].count(data_json[key]) > 1:
            return True
    return False

# It will check whether the data is invalid or not: data will be invalid if, its key is not present, null or blank. Also for zip key, its size should br 5(valid US postal code).
# Input: data_json[dict], keys[List]
# Output: [Boolean]
def check_invalid(data_json, keys):
    for key in keys:
        if not key in data_json.keys():
            return True
        elif data_json[key] is None:
            return True
        elif data_json[key] == "":
            return True
        elif key == 'zip' and len(data_json[key]) != 5:
            return True
    return False

# It will merge all the values for a key in the list of dicts
# Input: data_json[dict], key[String]
# Output: key_list[List]
def merge_all(data_json, key):
    key_list = []
    for data in data_json:
        if key in data.keys():
            key_list.append(data[key])
    return key_list

# It will identify and return the duplicate and invalid data
# Input: data_json[dict], keys[list]
# Output: invalidAndDuplicateId[list]
def get_duplicate_date(data_json,keys):
    invalidAndDuplicateId = []
    full_list = {}
    for key in keys:
        full_list[key] = merge_all(data_json, key)
    for emp_data in data_json:
        if check_invalid(emp_data, keys) == True:
            invalidAndDuplicateId.append(emp_data['id'])
            continue
        if check_duplicate(emp_data, full_list) == True:
            invalidAndDuplicateId.append(emp_data['id'])
    return invalidAndDuplicateId

# Open the data file and return parsed json variable
# Input: filename[File]
# Output: data_json[dict]
def read_file(filename):
    with open(filename) as f:
        data_json = json.load(f)
    return  data_json

# reading the file
data_json = read_file('data.json')
# collecting the keys that require for validation
validator_keys_list = ['name','address','zip']
# Call validation fucntion
invalidAndDuplicateId = get_duplicate_date(data_json,validator_keys_list)
# print invalid keys
print(*invalidAndDuplicateId, sep = "\n")