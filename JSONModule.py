# Write a Python program to convert JSON data to Python object.
# import json
# json_object='{"Name":"Ansh","Class":"Grad","Age":"17"}'
# python_obj=json.loads(json_object)
# print("\nJSON_data:")
# print(python_obj)
# print("\nName: ",python_obj["Name"])
# print("Class: ",python_obj["Class"])
# print("Age: ",python_obj["Age"])




# Write a Python program to convert Python object to JSON data.
# import json
# py_dict={"Name":"Ansh","Class":"Grad","Age":"27"}
# j_data=json.dumps(py_dict)
# print(j_data)




# Write a Python program to convert Python objects into JSON strings. Print all the values.
# import json
# py_obj={"Name":"Ansh","Std":"Grad","Age":"27"}
# js_data=json.dumps(py_obj)
# print(js_data)


# Write a Python program to convert Python dictionary object (sort by key) to JSON data.
# Print the object members with indent level 4.
# import json
# py_object={"Name":"Ansh","Age":"27","Std":"Grad"}
# print(json.dumps(py_object,indent=4))



# Write a Python program to check whether an instance is complex or not.
# import json
# def encode_complex(object):
#     # check using isinstance method
#     if isinstance(object, complex):
#         return [object.real, object.imag]
#     # raised error if object is not complex
#     raise TypeError(repr(object) + " is not JSON serialized")
#
# complex_obj = json.dumps(2 + 3j, default=encode_complex)
# print(complex_obj)



#








