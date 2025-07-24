import pytest
from dash._utils import create_callback_id
from app import app # Assuming your Dash app instance is named 'app' in app.py

@pytest.fixture
def dash_app(dash_duo):
    """
    Starts the Dash app in a test server and provides a DashValidator client.
    dash_duo is a fixture from dash.testing that manages the Dash server.
    """
    dash_duo.start_server(app)
    return dash_duo

def test_h1_title_is_present(dash_app):
    """
    Checks if the main H1 title element is present in the layout.
    """
    # Wait for the element to be visible.
    dash_app.wait_for_element("#main-app-title", timeout=10)

    # Check the title is showing the correct content
    assert dash_app.find_element("#main-app-title").text == "Pink Morsel: Cross Regional Sales History"

def test_visualisation_is_present(dash_app):
    """
    Checks if the line chart element is present in the layout.
    """
    dash_app.wait_for_element("#visualisation", timeout=10)

def test_radio_btns_are_present(dash_app):
    """
    Checks if the radio buttons element is present in the layout.
    """
    dash_app.wait_for_element("#region-radio-buttons", timeout=10)