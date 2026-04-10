    
def build_prompt(objeto: GlobalObjectForContext):
    """
    toca hacer muy bien el promp
    """
    return (
        f"Objeto: {objeto.etiqueta}. "
        f"Cámaras: {', '.join(objeto.cameras_seen) if objeto.cameras_seen else 'ninguna'}. "
        f"Describe la escena."
    )
   