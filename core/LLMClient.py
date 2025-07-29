import logging
from typing import Optional
import base64
from pathlib import Path

from google.generativeai.client import configure
from google.generativeai.generative_models import GenerativeModel
from google.generativeai import types

logger = logging.getLogger(__name__)


class LLMClient:
    """
    Google Gemini API client class
    """

    def __init__(self, api_key: str, model: str = "gemini-2.0-flash"):
        """
        Initialize Google Gemini API client
        :param api_key: Google API key
        :param model: Name of the model to use
        """
        self.api_key = api_key
        self.model = model
        configure(api_key=api_key)
        self.client = GenerativeModel(model)

    def completion(
        self,
        user_message: str,
        system_prompt: Optional[str] = None,
        image_paths: Optional[list[str]] = None,
        temperature: float = 0.7,
        max_tokens: int = 8192,
    ) -> str:
        """
        Create chat dialogue (supports multimodal)

        Args:
            user_message: User message content
            system_prompt: System prompt (optional)
            image_paths: List of image paths (optional)
            temperature: Generation temperature
            max_tokens: Maximum number of tokens

        Returns:
            str: Model generated response content
        """
        # Prepare the content
        content_parts = []
        
        # Add system prompt if provided
        if system_prompt:
            content_parts.append(system_prompt + "\n\n")
        
        # Add user message
        content_parts.append(user_message)
        
        # Add images if provided
        if image_paths:
            for img_path in image_paths:
                image_data = self.load_image(img_path)
                content_parts.append(image_data)

        try:
            # Configure generation parameters
            generation_config = types.GenerationConfig(
                temperature=temperature,
                max_output_tokens=max_tokens,
            )
            
            response = self.client.generate_content(
                content_parts,
                generation_config=generation_config
            )
            
            return response.text

        except Exception as e:
            logger.error(f"API request failed: {str(e)}")
            raise e

    def load_image(self, image_path: str):
        """
        Load image for Google Gemini API
        
        Args:
            image_path: Path to the image file
            
        Returns:
            Image object for Gemini API
        """
        import PIL.Image
        
        img = PIL.Image.open(image_path)
        return img
