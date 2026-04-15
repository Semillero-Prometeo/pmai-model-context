from transformers import AutoProcessor, BlipForConditionalGeneration


def import_Blip_model():
    """
    
    """
    try:
        processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base", use_fast=True)
    except ImportError:
        processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model
    
    