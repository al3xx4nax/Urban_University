import inspect


def introspection_info(obj):
    info = {}

    info['type'] = str(type(obj)).split("'")[1]
    info['attributes'] = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['methods'] = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['module'] = obj.__class__.__module__
    if inspect.isclass(obj):
        info['bases'] = [base.__name__ for base in obj.__bases__]

    return info


class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Привет, меня зовут {self.name}!"


my_instance = MyClass("Alice")


instance_info = introspection_info(my_instance)
print(instance_info)


number_info = introspection_info(42)
print(number_info)