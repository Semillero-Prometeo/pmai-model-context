   #https://www.aprender21.com/blog/estructura-de-un-prompt-perfecto 
   
   
def build_prompt(objeto: GlobalObjectForContext):
    """
    Construye un prompt optimizado para generar descripciones detalladas de objetos en escenas.
    Sigue mejores prácticas de prompt engineering para máxima calidad de salida.
    """
    return (
        f"# Tu objetivo es realizar una descripcion detallada de una imagen\n\n"
  
        f"Eres un experto en percepción visual y descripción de escenas. Tu tarea es crear una descripción "
        f"precisa y envolvente de un objeto detectado en un ambiente.\n\n"
    
   
        f"Proporciona una descripción completa del objeto que incluya:\n"
        
        
        f"1. **Apariencia**: Color, textura, forma, tamaño relativo, detalles físicos visibles\n"
        f"2. **Estado Emocional** (si aplica): Expresión facial, lenguaje corporal, estado de ánimo percibido\n"
        f"3. **Posición**: Ubicación en la escena, altura, profundidad, orientación espacial\n"
        f"4. **Interacciones**: Cómo interactúa con otros objetos, personas u elementos del ambiente\n"
        f"5. **Contexto Ambiental**: Elementos circundantes que proporcionan contexto\n\n"
     
     
     
        f"- Usa lenguaje claro, descriptivo y natural (como hablaría un humano)\n"
        f"- Evita especulaciones infundadas; describe solo lo observable\n"
        f"- Si el objeto es una persona, incluye edad aparente, ropa, accesorios visibles\n"
        f"- Sé específico con colores, materiales y texturas\n"
        f"- Mantén un tono objetivo pero envolvente\n\n"
   
   
        f"Proporciona la descripción en un único párrafo coherente y fluido, "
        f"sin usar viñetas ni numeraciones en la respuesta final."
        
        
        f"No incluyas lenguaje ofensivo, inapropiado o discriminatorio."
        f"Mantén un enfoque respetuoso y profesional en todo momento."
    )
   