# in this tutorial, you will learn about python static methods and hopw to use them to creat ea utility class

# the instance methods can access and modify the state of the bound object, and the class methods can access and modify the class state.
# unlike instance methods, static methods are not bound to an object, in other word, static methods cannot access and modify an object state
# in addition, python doesn't implicitly pass the cls parameter(or the self parameter) to static methods, therefore, static methods cannnot access and modify the class's state

# you can use the @staticmethod decorator to define a static method:
class classname:
    @staticmethod
    def static_method_name(param_list):
        pass
# to call a static method, you use this syntax:
classname.static_method_name(1)

# take an example:
class TemperatureConverter:
    KEVIN = 'K',
    FAHRENHEIT = 'F'
    CELSIUS = 'C'

    @staticmethod
    def celsius_to_fahrenheit(c):
        return 9*c/5 + 32

    @staticmethod
    def fahrenheit_to_celsius(f):
        return 5*(f-32)/9

    @staticmethod
    def celsius_to_kelvin(c):
        return c + 273.15

    @staticmethod
    def kelvin_to_celsius(k):
        return k - 273.15

    @staticmethod
    def fahrenheit_to_kelvin(f):
        return 5*(f+459.67)/9

    @staticmethod
    def kelvin_to_fahrenheit(k):
        return 9*k/5 - 459.67

    @staticmethod
    def format(value, unit):
        symbol = ''
        if unit == TemperatureConverter.FAHRENHEIT:
            symbol = '°F'
        elif unit == TemperatureConverter.CELSIUS:
            symbol = '°C'
        elif unit == TemperatureConverter.KEVIN:
            symbol = '°K'

        return f'{value}{symbol}'
    
f = TemperatureConverter.celsius_to_fahrenheit(35)
print(TemperatureConverter.format(f, TemperatureConverter.FAHRENHEIT))