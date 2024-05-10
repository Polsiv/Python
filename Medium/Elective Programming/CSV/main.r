data <- read.csv("Accesouniversal.csv")
print(data)



# # Asignar nombres a las columnas
# colnames(datos) <- c("NOMBRE_COMERCIAL", "DIRECCION", "TELEFONO_CELULAR", "CORREO_ELECTRONICO", "LATITUD", "LONGITUD", "LOCALIZACION_FINAL")

# # Filtrar registros con correo electrónico de PCL
# gmail <- datos[grep("@PCL.COM.CO", datos$CORREO_ELECTRONICO),]

# # Filtrar registros con celular de 7 dígitos
# celular_7_digitos <- datos[nchar(datos$TELEFONO_CELULAR) == 7,"NOMBRE_COMERCIAL"]

# # Filtrar registros con "colombia" en el nombre comercial
# colombia <- datos[grep("colombia", tolower(datos$NOMBRE_COMERCIAL)),"NOMBRE_COMERCIAL"]

# # Mostrar los resultados
# print("Registros con correo electrónico de PCL:")
# print(gmail)
# cat("\n")

# print("Empresas con celular de 7 dígitos:")
# print(celular_7_digitos)
# cat("\n")

# print("Empresas con 'colombia' en el nombre comercial:")
# print(colombia)
# cat("\n")