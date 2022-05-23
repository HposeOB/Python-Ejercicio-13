class Vehiculo:
    color = "Blanco"
    ruedas = 4
    puertas = 3

class Coche(Vehiculo):
    velocidad = 225
    cilindrada = "150cv"

d = Coche()
print(f"Color: {d.color}, Ruedas: {d.ruedas}, Puertas: {d.puertas}, Velocidad: {d.velocidad}, Cilindrada: {d.cilindrada}")
