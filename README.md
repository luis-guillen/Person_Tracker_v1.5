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

## Funcionalidades
- **Detección con Haar Cascade**: Identifica personas en un video utilizando el clasificador Haar.
- **Seguimiento con KCF Tracker**: Rastrea personas detectadas a lo largo del tiempo.
- **Re-identificación con Template Matching**: En caso de pérdida de seguimiento, utiliza Template Matching para relocalizar a la persona.
- **Gestión de Trackers**: Mantiene y actualiza trackers basándose en su "vida".
- **Identificación Visual**: Cada persona es identificada con un color único y un ID.

## Uso
1. **Configuración Inicial**: Cargar el clasificador Haar y configurar los parámetros del video.
2. **Procesamiento de Video**: Leer el video frame a frame, reduciendo su resolución para mejorar el rendimiento.
3. **Detección y Seguimiento**: Aplicar Haar Cascade y KCF Tracker en cada frame.
4. **Re-identificación**: Utilizar Template Matching cuando el tracker falla.
5. **Visualización**: Dibujar rectángulos y mostrar ID para cada persona detectada.

## Tecnologías Utilizadas
- Python
- OpenCV
