from typing import List, Union
from pydantic import BaseModel

# Function to convert Pydantic model into sidebar menu structure
def generate_sidebar_menu(model: BaseModel) -> dict:
    root_menu = {
        "title": model.__class__.__name__,
        "sub_menu": [{"title": field, "value": getattr(model, field)} for field in model.dict().keys()]
    }
    return root_menu


class Banner:
    def __init__(self, title: str, subtitle: str, action_url: str):
        self.title = title
        self.subtitle = subtitle
        self.action_url = action_url

class Card:
    def __init__(self, title: str, description: str, image_url: str, actions: List[str]):
        self.title = title
        self.description = description
        self.image_url = image_url
        self.actions = actions

class FormField:
    def __init__(self, name: str, type: str, required: bool, placeholder: str):
        self.name = name
        self.type = type
        self.required = required
        self.placeholder = placeholder

class Form:
    def __init__(self, fields: List[FormField], submit_url: str):
        self.fields = fields
        self.submit_url = submit_url

# Additional functions to generate these components based on specific input can be added here
