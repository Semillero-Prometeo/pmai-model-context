from pydantic import BaseModel, Field
from typing import Any

class GlobalObjectForContext(BaseModel):
    
    """A single re-identified object
    """
    
    id_global: str = Field(description="Global ReID identity")
    etiqueta: str = Field(description="Detection class label")
    confianza: float = Field(ge=0.0, le=1.0, description="Best confidence across views")
    contexto: str | None = Field(default=None, description="Natural-language context from LLM")
    sensores: dict[str, Any] = Field(default_factory=dict)
    cameras_seen: list[str] = Field(
        default_factory=list, description="Camera IDs that see this identity",
    )
    camera_id: str | None = Field(
        default=None, description="Representative camera (e.g. highest confidence)",
    )
    bbox: tuple[int, int, int, int] | None = Field(
        default=None,
        description="Representative bbox (xmin, ymin, xmax, ymax) from best view",
    )
    image_base64: str | None = Field(
        default=None,
        description="Base64-encoded image from best view",
    )


def context_info(objeto: GlobalObjectForContext, contexto: str):
    """
    """
    
    objeto.contexto = contexto
    return objeto.contexto


