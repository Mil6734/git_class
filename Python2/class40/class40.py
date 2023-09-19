# from jinja2 import Template

# persons = [
#     {'name': 'Алексей', 'year': 18, 'weight': 78.5},
#     {'name': 'Никита', 'year': 28, 'weight': 82.0},
#     {'name': 'Виталий', 'year': 33, 'weight': 94.3}
# ]
#
# html = """
# {%- macro list_users(list_of_user) %}
#     <ul>
#         {%- for u in list_of_user %}
#         <li>{{u.name}} {{caller(u)}} </li>
#         {%endfor%}
#     </ul>
# {%endmacro%}
#
# {% call(user) list_users(users)%}
#     <ul>
#     <li>age: {{user.age}}</li>
#     <li>weigh: {{user.weight}}</li>
#     </ul>
# {% endcall %}
# """
#
# tm = Template(html)
# msg = tm.render(users=persons)
# print(msg)


from jinja2 import Environment, FileSystemLoader

persons = [
    {'name': 'Алексей', 'year': 18, 'weight': 78.5},
    {'name': 'Никита', 'year': 28, 'weight': 82.0},
    {'name': 'Виталий', 'year': 33, 'weight': 94.3}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('main.html')
msg = tm.render(users=persons, title="About Jinja")
print(msg)


subs = ["Культура", "Наука", "Политика", "Спорт"]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

tm = env.get_template('about.html')
msg = tm.render(list_table=subs)
print(msg)

