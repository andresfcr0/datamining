# Calculadora de riesgos | Portal Médico ST&T 

Bienvenido a la API de la Calculadora de Riesgo

Esta API proporciona acceso a un sistema de evaluación de riesgo que ayuda a los profesionales médicos y a los pacientes a estimar la probabilidad de mortalidad asociada con una intervención quirúrgica específica. Utilizando datos clínicos, estadísticos y médicos actualizados, nuestra API ofrece una evaluación precisa y basada en evidencia del riesgo de mortalidad antes de una cirugía.


## Características Principales

- **Precisión Basada en Datos:** Nuestra API utiliza un modelo avanzado respaldado por datos clínicos y estadísticos para calcular la probabilidad de mortalidad asociada con una intervención quirúrgica.
- **Personalización:** Los usuarios pueden ingresar una variedad de factores, como la edad del paciente, el tipo de cirugía, el estado de salud general y las comorbilidades, para obtener una estimación personalizada del riesgo de mortalidad.
- **Aplicación Clínica:** Nuestra API está diseñada para ser una herramienta útil en la toma de decisiones clínicas, ayudando a los profesionales médicos a evaluar el riesgo y a los pacientes a tomar decisiones informadas sobre su atención médica.

## Uso de la API

Para utilizar el servicio, simplemente realice solicitudes HTTP, proporcionando los parámetros necesarios para la evaluación del riesgo. La API responderá con la probabilidad estimada de mortalidad asociada con la intervención quirúrgica especificada.

### Ruta del servicio


```
https://c03pz1fzie.execute-api.us-east-1.amazonaws.com/dev/apiresource
```

### Cuerpo de la petición

- `user_id` (string): ID del usuario.
- `attr` (object): Un objeto con los atributos para realizar el calculo asignado.

### Atributo ```attr```

Este atributo debe tener los parámetros necesarios para el cálculo:

```
{
    edadmintervencion: integer(5-100)
    sexopte: boolean
    tabaquismo: boolean
    mtabaco: boolean
    imc: decimal
    hta: boolean
    arritmiacard: boolean
    erc: boolean
    fallacardcron: boolean
    dislipidemia: boolean
    dm: boolean
    epoc: boolean
    transtiroideo: boolean
    diagcovid19: boolean
    covid19menor2: boolean
    esquemavacu: boolean
    estratosocioecono: integer(1-7)
    afiliacionsistema: integer(1-7)
    asascore: integer(1-5)
    complejidadprocedimiento: integer(1-7)
    momntointerven: boolean
    inestabilidadhemodinamica: boolean
    parocardiacopreoperatorio: boolean
    tipocx: integer(2-3000)
    tipodeabordajecx: boolean
}
```

### Response

#### SUCCESS
En caso de éxito, retorna un status `200 OK`, junto con un objeto JSON con los resultados del cálculo.

- `message` (string): Un mensaje relacionado con el resultado del cálculo.
- `mortality` (string): si es un riesgo, bajo/alto de mortalidad.
- `probability` (string): La probabilidad de mortalidad del paciente.

    

#### ERROR
Un `409 Conflict` en caso de error, con un objeto JSON con los siguientes parametros:

- `message` (string): Titulo del error.
- `details` (string): Detalle del error.
- `error` (string): Ubicación del error.
