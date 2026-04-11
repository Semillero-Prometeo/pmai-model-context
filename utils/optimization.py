from utils.model import import_Blip_model
from utils import model
import torch
from utils import model

DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
MODEL_NAME = "Salesforce/blip-image-captioning-base"


def optimize_model(model):
    """
    """
    model_quantized = torch.quantization.quantize_dynamic(
        model.cpu(), {torch.nn.Linear}, dtype=torch.qint8
    )
    return model_quantized


def optimize_model_fp16(model_fp16):
    """
    esto no se ya que no necesitamos gpu pero por si acaso lo dejo
    """
    model_fp16 = None
    if DEVICE == "cpu":
        model_fp16 = AutoModelForVision2Seq.from_pretrained(MODEL_NAME).half().to(DEVICE)
    return model_fp16

