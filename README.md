# Memoria Práctica 2 FSI – Visión Artificial

### Fundamentos de los Sistemas Inteligentes
**Curso**: Segundo  
**Grado**: Grado en Ciencia e Ingeniería de Datos  
**Escuela**: Escuela de Ingeniería Informática  
**Universidad**: Universidad de Las Palmas de Gran Canaria (ULPGC)  
**Autores**: Luis Guillén Servera, José Mataix Pérez

# Person Tracking Project

## Descripción
Este proyecto implementa un sistema de seguimiento de personas en videos utilizando OpenCV en Python. Combina detección con Haar Cascade, seguimiento con `cv2.TrackerKCF_create`, y re-identificación usando Template Matching.

## Uso
1. **Configuración Inicial**: Cargar el clasificador Haar y configurar los parámetros del video.
2. **Procesamiento de Video**: Leer el video frame a frame, reduciendo su resolución para mejorar el rendimiento.
3. **Detección y Seguimiento**: Aplicar Haar Cascade y KCF Tracker en cada frame.
4. **Re-identificación**: Utiliza un clasificador Haar Cascade para la detección de cuerpos completos
5. **Visualización**: Dibujar rectángulos y mostrar ID para cada persona detectada.

## Tecnologías Utilizadas
- Python
- OpenCV
## Recursos Utilizados
Se han empleado documentación y material proporcionado por la asignatura, así como herramientas de desarrollo de software, algunos de estos recursos son:
- https://medium.com/@MrBam44/object-tracking-with-opencv-and-python-7db8b233fab6
- https://docs.opencv.org/4.8.0/d4/dc6/tutorial_py_template_matching.html
- [Chat de OpenAI](https://chat.openai.com)

