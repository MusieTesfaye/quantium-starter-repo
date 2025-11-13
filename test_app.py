import pytest
from app import app
from dash import dcc
import dash_mantine_components as dmc

def find_component(layout, condition):
    """Find component by condition function"""
    if condition(layout):
        return layout
    if hasattr(layout, 'children'):
        children = layout.children if isinstance(layout.children, list) else [layout.children] if layout.children else []
        for child in children:
            result = find_component(child, condition)
            if result:
                return result
    return None

def test_header_present():
    header = find_component(app.layout, lambda x: hasattr(x, 'id') and x.id == 'header-title')
    assert header is not None, "Header not found"

def test_visualization_present():
    graph = find_component(app.layout,lambda x: hasattr(x, 'id') and x.id == 'graph-wrapper')
    assert graph is not None, "Graph wrapper not found"

def test_region_picker_present():
    picker = find_component(app.layout, lambda x: hasattr(x, 'id') and x.id == 'region-selector')
    assert picker is not None, "Region picker not found"