"""Utility functions.

This module contains utility functions for the palm-models package.
"""
import os
from dotenv import load_dotenv, find_dotenv


def get_api_key():
    """Get the Google API key from the local .env file.

    Returns:
        str: The Google API key.
    """
    _ = load_dotenv(find_dotenv())  # read local .env file
    return os.getenv("GOOGLE_API_KEY")
