import streamlit as st
from typing import Optional

def div_card(content: str, key: Optional[str] = None) -> str:
    """Generate a card div with content and optional key."""
    return f'<div class="card" key="{key}">{content}</div>'
