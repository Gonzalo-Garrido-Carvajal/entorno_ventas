import pandas as pd
import matplotlib.pyplot as plt

# carga los datos desde el archivo csv
df = pd.read_csv('ventas_productos.csv')

#Calcual el precio total por producto

df['Precio_Total']= df['Çantidad']* df['Precio' ]
                                       
print(df.head())

#Crea Grafic0 barra
plt.bar(df['Producto'],df['Precio Total'])
plt.xlabel('Prodcuto')
plt.ylabel('Precio Total')
plt.title('Precio Total por Productop')
plt.title('Grafico_precios.png')
plt.show()
        
        
                          
