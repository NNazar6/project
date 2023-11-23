from django.shortcuts import render
from django.http import HttpResponse

def full_name(request, name, age, interesting):
    return HttpResponse(f"""
            <h2>Меня зовут : {name} {age} {interesting}</h2>
""")

def about(request, from_town, grade, school):
    return HttpResponse(f'''
            <h3>I from: {from_town}, {grade}, I {school}</h3>
''')

def contacts(request, contacts):
    return HttpResponse(f'''
            <h4>My number: {contacts}</h4>
''')