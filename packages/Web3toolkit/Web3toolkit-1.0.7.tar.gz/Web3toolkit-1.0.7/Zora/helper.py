import importlib
import inspect
import pkgutil


def get_zora_helper():
    package_name = 'Zora'
    module_contents = {}
    package = importlib.import_module(package_name)
    for _, module_name, _ in pkgutil.walk_packages(package.__path__, package_name + "."):
        module = importlib.import_module(module_name)

        module_info = {
            "functions_names": [],
            "classes_info": []
        }

        for name, obj in inspect.getmembers(module):
            if inspect.isfunction(obj):
                module_info["functions_names"].append(name)
            elif inspect.isclass(obj):
                class_info = {"methods": []}

                for class_name, class_obj in inspect.getmembers(obj):
                    if inspect.isfunction(class_obj) and class_obj.__qualname__.startswith(obj.__name__ + '.'):
                        class_info["methods"].append(class_name)

                module_info["classes_info"].append({
                    "name": name,
                    "methods": class_info["methods"]
                })

        module_contents[module_name] = module_info

    return module_contents
