# your_app/templatetags/__init__.py

from .custom_filters import get_item
  # Import your custom template tag function

# This line is necessary to let Django know that this directory contains custom template tags
# and that they should be available for use in templates.
__all__ = ['get_item']
 # Add the names of your custom tags here
