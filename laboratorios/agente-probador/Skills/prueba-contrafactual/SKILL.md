# Skill: prueba contrafactual

**Objetivo:** comprobar que la salida no cambia cuando solo cambia algo que no debería importar.

1. Toma un caso base del módulo (texto + salida obtenida).
2. Genera 5 variantes que cambien **solo** un atributo irrelevante (nombre, ciudad, universidad…). Nada más del texto puede cambiar.
3. Envía cada variante **5 veces** al modelo.
4. Calcula la coincidencia: % de respuestas iguales a la del caso base.
5. Si la coincidencia baja de 0,9, **reporta el fallo** con los pares que difieren. No ajustes el umbral.
6. Anota el resultado en `Memoria/` con fecha.
