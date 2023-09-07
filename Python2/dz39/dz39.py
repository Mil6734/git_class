from jinja2 import Template

# ......................................Задача 1...........................................

# html = """
# {%- macro text_input( name, placeholder, type='text') -%}
#     <input type="{{type}}" name="{{name}}" placeholder="{{placeholder}}">
# {%-endmacro%}
# <p>{{text_input('firstname', 'Имя')}}</p>
# <p>{{text_input('lastname', 'Фамилия')}}</p>
# <p>{{text_input('address', 'Адрес')}}</p>
# <p>{{text_input('phone', 'Телефон', 'tel')}}</p>
# <p>{{text_input('email', 'Почта', 'email')}}</p>
# """
#
# tm = Template(html)
# msg = tm.render()
# print(msg)

# ......................................Задача 2...........................................


page = [
    {'mod': '/index', 'name': 'Главная'},
    {'mod': '/news', 'name': 'Новости'},
    {'mod': '/about', 'name': 'О компании'},
    {'mod': '/shop', 'name': 'Магазин'},
    {'mod': '/contacts', 'name': 'Контакты'}
]

html = """<ul>
{% for i in pg -%}
    {% if i.name == 'Главная' -%}
    <li><a href="{{i.mod}}" class="active">{{i.name}}</a></li>
    {% else -%}
    <li><a href="{{i.mod}}">{{i.name}}</a></li>
    {%- endif %}
{%endfor%}
</ul>
"""

tm = Template(html)
msg = tm.render(pg=page)
print(msg)
