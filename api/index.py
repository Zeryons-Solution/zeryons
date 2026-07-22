#!/usr/bin/env python
"""
Vercel serverless function entry point for Django application.

This handles all HTTP requests on Vercel's serverless platform.
Requests are routed through Django's WSGI application.
"""

import os
import sys
from pathlib import Path

# Add project root to Python path for module imports
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Zeryons.settings')

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application

# Create WSGI application instance
app = get_wsgi_application()

# Vercel serverless function handler
def handler(request):
    """
    Handle incoming HTTP requests on Vercel.
    
    Vercel calls this function with a request object and expects
    a response object. The WSGI app handles the actual request.
    """
    return app(request.environ, request.start_response)
