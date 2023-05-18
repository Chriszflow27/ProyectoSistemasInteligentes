import openai
import config

openai.api_key = config.api_key

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )
    return response.choices[0].text

messages = [{'role': "ChatIA",
             'content' : "Bienvenido a nuestro nutricionista virtual. ¿En qué puedo ayudarte?"}]

goal = input("¿Cuál es tu objetivo? (p. ej., perder peso, ganar masa muscular, mejorar la salud, etc.) ")
messages.append({'role': "Objetivo",
                 'content' : goal})

weight = input("¿Cuál es tu peso actual en kilogramos? ")
messages.append({'role': "Peso",
                 'content' : weight})

height = input("¿Cuál es tu altura en centímetros? ")
messages.append({'role': "Altura",
                 'content' : height})

age = input("¿Cuál es tu edad? ")
messages.append({'role': "Edad",
                 'content' : age})

# Calcular el IMC
height_in_meters = float(height) / 100
weight_in_kg = float(weight)
imc = weight_in_kg / (height_in_meters ** 2)
imc_str = f"{imc:.1f}"

# Identificar el patrón corporal
if imc < 18.5:
    pattern = "delgado"
elif imc < 25:
    pattern = "saludable"
elif imc < 30:
    pattern = "con sobrepeso"
else:
    pattern = "obeso"

# Utilizar la función `generate_response` para generar recomendaciones de comida y recetas personalizadas
prompt = f"Mi objetivo es {goal}. Actualmente peso {weight} kilogramos, mido {height} centímetros y tengo {age} años. Mi IMC es {imc_str}, lo que indica que tengo un cuerpo {pattern}. ¿Qué ejercicios y recetas (tambien como prepararlas) me recomiendas y en qué días y horarios debo consumirlas?"
response = generate_response(prompt)

messages.append({'role': "Nutricionista lucIA",
                 'content' : response})

for message in messages:
    print("")
    print(f"{message['role']}: {message['content']}")    




