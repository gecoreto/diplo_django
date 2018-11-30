from django.http import HttpResponse
from django.shortcuts import render
from django.http import JsonResponse 
from bokeh.sampledata.iris import flowers
import pandas as pd
import json
import numpy as np
#graficas
from bokeh.plotting import figure, output_file, save



def paintGraficaUno(products):
    basepath = 'http://127.0.0.1:8000/graficas/'
    # output to static HTML file
    output_file("./graficas/templates/grafica_uno.html")
    # create a new plot
    p = figure(
    tools="pan,box_zoom,reset,save",
    y_axis_type="log", title="Tendencia",
    x_axis_label='Años', y_axis_label='Cantidad (KG)',
    plot_width=450, plot_height=450
    )
    # Colores
    colores = ["#7B1FA2", "#00342d", "#3F51B5", "#4DB6AC", "#0091EA", "#33691E", "#FF6F00", "#795548", "#66BB6A", "#BA68C8"]    
    # Responses productos
    resProducts = {}
    # prepare some data
    for product in products:
        for product, label in product.items():
            pathData = '/Users/david/Documents/desarrollo/universidad/diplomado/project_django/exportData/graficas/datasets/' + product + '.csv'
            # Read the data from a csv into a dataframe
            data = pd.read_csv(pathData)
            # Summary stats for the column of interest  
            anios = list(set(data['Anio']))
            anios = np.sort(anios)
            meses = list(set(data['Mes']))
            cantidadUnidades = []
            infoProduct = {}
            for anio in anios:
                cantidades= data[data['Anio'] == anio]['CantidadUnidades']
                promedio = np.average(cantidades)
                cantidadUnidades.append(promedio)
                infoMeses = {}
                for mes in meses:
                    cantidadesMes = data[(data['Anio'] == anio) & (data['Mes'] == mes)]['CantidadUnidades']
                    infoMeses[str(mes)] = {'cantidadesTotales' : np.sum(cantidadesMes)}
                infoProduct[str(anio)] = infoMeses
            resProducts[product] = infoProduct
            # print(anios)
            # print(cantidadUnidades)

            # add some renderers
            color = colores.pop()
            p.line(anios, cantidadUnidades, legend=label, line_color=color)
            p.circle(anios, cantidadUnidades, legend=label, fill_color="white", line_color=color, size=8)
    # show the results
    save(p)
    print(resProducts)
    return JsonResponse({
                            'urlImg' : basepath + 'uno',
                            # 'products' : json.dumps(resProducts)
                            'products' : resProducts
                        })

def paintGraficaDos():
    # output to static HTML file
    output_file("./graficas/templates/grafica_dos.html")

    fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
    counts = [5, 3, 4, 2, 4, 6]

    p = figure(x_range=fruits, plot_height=250, title="Fruit Counts",
           toolbar_location=None, tools="")

    p.vbar(x=fruits, top=counts, width=0.9)

    p.xgrid.grid_line_color = None
    p.y_range.start = 0

    save(p)
    return "Se crea el html de la grafica."

def generarGrafica(request):
    data = json.loads(request.body)
    products = data['products']
    numberGraph = data['numberGraph']
    basepath = 'http://127.0.0.1:8000/graficas/'
    response = JsonResponse({'error' : 'Numero de grafica no encontrado'})
    if numberGraph == 1:
        response = paintGraficaUno(products) #Generar html de la grafica
    if numberGraph == 2:
        paintGraficaDos() #Generar html de la grafica
        response = JsonResponse({'urlImg' : basepath + 'dos'})
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response

def graficauno(request):
    return render(request, 'grafica_uno.html')

def graficados(request):
    return render(request, 'grafica_dos.html')

def graficadosOK(request):
    pathData = '/Users/david/Documents/desarrollo/universidad/diplomado/project_django/exportData/graficas/datasets/flores.csv'
    # Read the data from a csv into a dataframe
    data = pd.read_csv(pathData)
    # Summary stats for the column of interest
    # codigoPais = data[data['CodigoPais'] == 23]['CodigoPais']    
    codigoPais = data['CodigoPais']    
    cantidadUnidades = data[data['CantidadUnidades'] < 100]['CantidadUnidades']

    # output to static HTML file
    output_file("./graficas/templates/grafica_dos.html")
    # create a new plot
    plot = figure(
        title="Probando ando",
        y_axis_label='Codigo pais', x_axis_label='Cantidad unidades'
    )
    # Crear lineas
    # plot.line(codigoPais, cantidadUnidades, line_width=3)
    plot.circle(cantidadUnidades, codigoPais, fill_color='white', size=10)
    # show the results
    save(plot)
    return render(request, 'grafica_dos.html')

def paintGraficaBASEEEEE():
    # prepare some data
    x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
    y0 = [i**2 for i in x]
    y1 = [10**i for i in x]
    y2 = [10**(i**2) for i in x]

    # output to static HTML file
    output_file("./graficas/templates/grafica_uno.html")
    # create a new plot
    p = figure(
    tools="pan,box_zoom,reset,save",
    y_axis_type="log", y_range=[0.001, 10**11], title="log axis example",
    x_axis_label='sections', y_axis_label='particles',
    plot_width=450, plot_height=450
    )

    #Tamaño ajustado
    # p.sizing_mode = 'scale_width'

    # add some renderers
    p.line(x, x, legend="y=x")
    p.circle(x, x, legend="y=x", fill_color="white", size=8)
    p.line(x, y0, legend="y=x^2", line_width=3)
    p.line(x, y1, legend="y=10^x", line_color="red")
    p.circle(x, y1, legend="y=10^x", fill_color="red", line_color="red", size=6)
    p.line(x, y2, legend="y=10^x^2", line_color="orange", line_dash="4 4")

    # show the results
    save(p)
    return "Se crea el html de la grafica."

