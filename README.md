# Asistentes a boda

## Descripción
Estás creando una empresa con un socio, esta empresa se dedicará a 
organizar eventos y, precisamente en esta ocasión, les tocó ser los 
organizadores de una boda, y tienen tres listas importantes:

1. **Lista de invitados**: personas que fueron invitadas a la fiesta.
2. **Lista de confirmados**: personas que confirmaron que asistirían a la fiesta.
3. **Lista de asistentes**: personas que efectivamente llegaron a la fiesta.

Tu tarea es crear un reporte que contenga lo siguiente:

1. **Colados**: personas que llegaron, pero no estaban en la lista de invitados.
2. **Faltantes**: personas que fueron invitadas, pero no llegaron, sin importar si confirmaron o no.
3. **Confirmados que llegaron**: personas que confirmaron asistencia y realmente asistieron.
4. **Invitados que llegaron**: personas que estaban en la lista de invitados y llegaron (hayan confirmado o no).

Deberás regresar el total de personas para cada lista del reporte en el orden dado (colados, faltantes, confirmados, asistentes).

## Restricciones
- Las listas de confirmados y asistentes pueden estar 
vacías.
- La lista de invitados siempre contendrá elementos.
- Todos los elementos en las listas son nombres de personas (es decir cadenas de texto).
- Las listas de invitados, confirmados y asistentes no contienen nombres duplicados.
- Todos los confirmados estarán en la lista de invitados, ya que una persona no puede confirmar si no fue invitada.

## Entradas
Se darán 3 listas como entrada:
- **Invitados**: Personas que fueron formalmente invitadas a la fiesta.
    - Contiene uno o más nombres de invitados (cadenas de texto en minúsculas y sin acentos).
- **Confirmados**: Personas que confirmaron su asistencia a la fiesta.
    - Contiene cero o más nombres de confirmados (cadenas de texto en minúsculas y sin acentos).
- **Asistentes**: Personas que realmente asistieron a la fiesta.
    - Contiene cero o más nombres de confirmados (cadenas de texto en minúsculas y sin acentos).

## Salidas
La salida deberán ser cuatro líneas, cada una con un número entero, que representan, en orden, la cantidad de: **colados**, **faltantes**, **confirmados que llegaron** e **invitados que llegaron**.

## Entradas y salidas de ejemplo

### Ejemplo 1
Entrada | Salida 
--------|--------
`["ana", "luis", "carlos", "maria", "ramon"]`<br>`["carlos"]`<br>`["maria", "ramon", "carlos", "miguel", "sofia"]` | `2`<br>`2`<br>`1`<br>`3`

#### Explicación
- **Colados**: miguel y sofia llegaron, pero no están en la lista de invitados. Por lo tanto, hay 2 colados.
- **Faltantes**: ana y luis estaban invitados, pero no llegaron: 2 faltantes.
- **Confirmados que llegaron**: carlos confirmó asistencia y también llegó: 1 confirmado que llegó.
- **Invitados que llegaron**: ramon, carlos y maria estaban invitados y llegaron: 3 invitados que llegaron.

### Ejemplo 2
Entrada | Salida 
--------|--------
`["pedro", "juan"]`<br>`["juan"]`<br>`["pedro", "juan"]`<br><br> | `0`<br>`0`<br>`1`<br>`2`

#### Explicación
- **Colados**: Todos los que llegaron están en la lista de invitados, por lo tanto, no hay colados: 0 colados.
- **Faltantes**: Ninguno de los invitados faltó, ya que ambos, pedro y juan, llegaron: 0 faltantes.
- **Confirmados que llegaron**: juan confirmó asistencia y llegó: 1 
confirmado que llegó.
- **Invitados que llegaron**: pedro y juan fueron invitados y llegaron. 2 invitados que llegaron.

### Ejemplo 3
Entrada | Salida 
--------|--------
`["laura", "marta"]`<br>`["marta"]`<br>`["marta", "elena"]`<br><br> | `1`<br>`1`<br>`1`<br>`1`

#### Explicación
- **Colados**: elena llegó, pero no estaba invitada: 1 colado.
- **Faltantes**: laura estaba invitada pero no llegó: 1 faltante.
- **Confirmados que llegaron**: marta confirmó asistencia y llegó: 1 confirmado que llegó.
- **Invitados que llegaron**: marta estaba invitada y llegó: 1 invitado que llegó.

### Ejemplo 4
Entrada | Salida 
--------|--------
`["laura", "marta"]`<br>`[]`<br>`[]`<br><br> | `0`<br>`2`<br>`0`<br>`0`

#### Explicación
- **Colados**: nadie llegó a la fiesta: 0 colados.
- **Faltantes**: como laura y marta faltaron a la fiesta: 2 faltantes.
- **Confirmados que llegaron**: nadie confirmó ni llegó. 0.
- **Invitados que llegaron**: ningún invitado llegó: 0.

### Ejemplo 5
Entrada | Salida 
--------|--------
`["juan", "arturo", "maria", "rosa", "alberto", "rocio", "jose"]`<br>`["arturo", "maria", "rosa", "jose"]`<br>`["ramon", "roberto", "arturo", "rosa", "nicolas", "benito", "rebeca", "jacinto"]` | `6`<br>`5`<br>`2`<br>`2`
