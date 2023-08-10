"""
Custom Template Tags for Private Content Handling in the simulateuser app.

This module provides template tags that protect private content from being displayed during a user simulation.

Attributes:
- `register`: This is a decorator that registers custom tags with Django.
- `private`: A simple tag that replaces content if the user is in a simulation.
- `do_privateblock`: A tag decorator that supports block-level privacy checks.
- `PrivateBlockNode`: A node that represents the block-level privacy tag.

Usage:
In Django templates, you can use the `{% load private_tags %}` directive to import these tags.
Then, use `{% private "content" %}` for single line content protection, or use
`{% privateblock %}...{% endprivateblock %}` for multi-line content protection.
"""

from django import template
from ..app_settings import app_settings


register = template.Library()


@register.simple_tag(takes_context=True)
def private(context, content):
    """
    A simple tag that checks if the user is in a simulation.
    If so, it replaces the provided content with the PRIVATE_CONTENT_REPLACEMENT setting value.
    """
    if context['request'].user != context['request'].real_user:
        return app_settings.PRIVATE_CONTENT_REPLACEMENT
    return content


@register.tag(name="privateblock")
def do_privateblock(parser, token):
    """
    Begins a block-level privacy check. Content inside this block will be replaced if the user is in a simulation.
    Usage:
        {% privateblock %}
            ... protected content ...
        {% endprivateblock %}
    """
    nodelist = parser.parse(('endprivateblock',))
    parser.delete_first_token()
    return PrivateBlockNode(nodelist)


class PrivateBlockNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        """
        Renders the block content and replaces it with PRIVATE_CONTENT_REPLACEMENT if the user is in a simulation.
        """
        output = self.nodelist.render(context)
        if context['request'].user != context['request'].real_user:
            return app_settings.PRIVATE_CONTENT_REPLACEMENT
        return output
