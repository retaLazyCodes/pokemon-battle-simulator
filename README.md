## Pokemon Battle Simulator

#### Tabla de contenidos

- [Logica de la App](#Logica-de-la-App)
- [Requisitos para ejecutar](#Requisitos-para-ejecutar)
- [Cómo ejecutar](#Cómo-ejecutar)



### Lógica de la App

#### 1. Obtener Información de los Pokémon
- Leer el archivo `batallas.json` para obtener la información de los Pokémon de la primera batalla.
- Consumir la PokeAPI para obtener los detalles necesarios.

#### 2. Instanciar Pokémon
- Crear instancias de los dos Pokémon involucrados en la batalla.
- Asignarles sus respectivos stats, tipos, y cadenas evolutivas.

#### 3. Desarrollar la Batalla
- **Orden de Movimiento:** 
  - El Pokémon con mayor velocidad ataca primero.
  - Si ambos tienen la misma velocidad, el orden se decide al azar.
- **Cálculo de Daño:**
  - El daño se calcula con la fórmula:
    Daño = Ataque del atacante * Relación del daño según el tipo – (30% * Defensa del Defensor)
  - Considerar los tipos de cada Pokémon para determinar la relación de daño.
- **Finalización del Combate:**
  - Si los HP del Pokémon rival llegan a 0 en el primer movimiento, el combate termina.
  - La batalla dura un solo turno; al final, el Pokémon con menos HP pierde.
- **Evolución:**
  - Si un Pokémon gana 200 puntos de experiencia, puede evolucionar.

#### 4. Finalización y Repetición
- Indicar el ganador al final de la batalla.
- Repetir el proceso desde el paso 1 con la siguiente batalla.



#### Requisitos para ejecutar
Tener instalado:

- Python ^3.11
- Git

#### Cómo ejecutar

Primero, clona este repositorio en tu máquina local:

```bash
git clone https://github.com/retaLazyCodes/pokemon-battle-simulator.git
```

Navega hasta el directorio del repositorio clonado:
```bash
cd pokemon-battle-simulator
```

En Linux/macOS

1. Haz que el script `setup.sh` sea ejecutable:
```bash
chmod +x setup.sh
```
2. Ejecuta el script para configurar el entorno y correr el programa:
```bash
./setup.sh
```

En Windows
1. Ejecuta el script `setup.bat`:
```bat
setup.bat
```

Este script:

* Crea un entorno virtual.
* Instala Poetry dentro del entorno virtual.
* Instala las dependencias necesarias.
* Ejecuta el programa ubicado en src/main.py.


