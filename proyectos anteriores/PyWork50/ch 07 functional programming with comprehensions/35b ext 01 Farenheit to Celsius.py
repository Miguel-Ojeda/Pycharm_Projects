"""
Create a dict whose keys are city names, and whose values are temperatures in Fahrenheit.
Now use a dict comprehension to transform this dict into a new one,
keeping the old keys but turning the values into the temperature in degrees Celsius.
"""
# temperatures_C ={'Las Palmas': 26, 'La Laguna': 18, 'Los Llanos': 22, 'Madrid': 14, 'Gijón': 12, 'Ávila': 5}
temperatures_F = {'Las Palmas': 79, 'La Laguna': 65, 'Los Llanos': 72, 'Madrid': 57, 'Gijón': 54, 'Ávila': 41}

# La fórmula es C = (F - 32) / 1.8

def F_to_C(temperatures_F):
    return {ciudad: (value - 32) / 1.8
            for ciudad, value in temperatures_F.items()}

resultado = F_to_C(temperatures_F)
print(resultado)