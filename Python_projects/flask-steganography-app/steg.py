from stegano.lsb import hide, reveal

def hide_text_in_image(image_path, secret_text, output_path):
    """Hide secret text inside an image"""
    secret_img = hide(image_path, secret_text)
    secret_img.save(output_path)
    return output_path

def extract_text_from_image(image_path):
    """Extract hidden text from an image"""
    try:
        hidden_text = reveal(image_path)
        return hidden_text if hidden_text else "No hidden text found"
    except Exception as e:
        return f"Error extracting text: {e}"
