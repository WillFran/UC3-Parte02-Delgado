from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

layaut = """
        <hr>
            <ul>
                <li><a href="/inicio"> Inicio </a></li>
                <li><a href="/primos"> Mostrar números [a, b] </a></li>
                <li><a href="/examen"> Mensaje de saludo </a></li>
            </ul>
        </hr>
        """

def inicio(request):

    return render(request, 'inicio.html')

def primos(request):
    a=10
    b=20
    resultado=f"""
            <h2>Números de [{a}, {b}] </h2>
            Resultado: <br>
            <ul>    
            """
    while a<=b:
        resultado += f"<li>{a}</li>"
        a+=1
    resultado += "</ul>"
    return HttpResponse(layaut + primos)

def examen(request):

    return render(request, 'examen.html')