#!/usr/bin/env python
"""
Vercel serverless function entry point for Django application.

Uses serverless-wsgi to adapt Django's WSGI application
for Vercel's serverless Python runtime.
"""

import os
import sys
from pathlib import Path

# Add project root to Python path for module imports
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Zeryons.settings')

# Import serverless-wsgi handler to adapt WSGI for Vercel
from serverless_wsgi import handle

# Vercel serverless function handler
def handler(request, context):
    """
    Handle incoming HTTP requests on Vercel via serverless-wsgi.

    serverless-wsgi translates between Vercel's event/context
    format and Django's WSGI interface.
    """
    return handle(request, context)

