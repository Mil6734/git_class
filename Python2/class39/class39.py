#  ............................Шаблонизатор.....................
#  Jinja
# pip install jinja2

# from jinja2 import Template
#

# name = 'Игорь'
# age = 28
#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#     def get_age(self):
#         return self.age
#
#
# per = Person("Игорь", 28)
#
# tm = Template("Привет {{ p.get_name() }}. Тебе {{p.get_age()}} лет?")
# msg = tm.render(p=per)
#
# print(msg)


from jinja2 import Template

# per = [9, 3, 5, 5, 1, 7, 6]
# link = """{% for i in p -%}
#     {{i}}
# {%- endfor %}
# """
# tm = Template(link)
# msg = tm.render(p=per)
# print(msg)


# cities = [
#     {'id': 1, 'city': 'Москва'},
#     {'id': 2, 'city': 'Смоленск'},
#     {'id': 3, 'city': 'Минск'},
#     {'id': 4, 'city': 'Ялта'},
#     {'id': 5, 'city': 'Ярославль'},
# ]
# link = """<select name="sities ">
# {% for c in cities -%}
#     {% if c.id > 3 %}
#     <option value="{{c.id}}">{{c.city}}</option>
#     {% endif -%}
# {% endfor %}
# </select>
# """
# tm = Template(link)
# msg = tm.render(cities=cities)
# print(msg)


# cars = [1, 2, 3, 4, 5, 6]
# tpl = "{{cs|random}}"
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)


# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.3},
# ]
# tpl = """
# {%- for u in users %}
#     {% filter upper %} {{u.name}} {% endfilter %}
# {%- endfor %}
# """
# tm = Template(tpl)
# msg = tm.render(users=persons)
# print(msg)


html = """
{% macro text_input(name, value='', type='text', size=20) %}
    <input type="{{type}}" name="{{name}}" value="{{value}}" size="{{size}}">
{%endmacro%}
<p>{{text_input('username')}}</p>
<p>{{text_input('email')}}</p>
<p>{{text_input('password', 'Пароль', 'password')}}</p>
"""

tm = Template(html)
msg = tm.render()
print(msg)
