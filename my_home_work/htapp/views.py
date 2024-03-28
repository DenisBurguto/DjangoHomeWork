import logging

from django.shortcuts import render
from django.http import HttpResponse

logger = logging.getLogger(__name__)

main_html = """
<h1>MAIN<h1/>
"""

about_html = """
<h1>ABOUT<h1/>
"""

def main(request):
    logger.info('Main page accessed')
    return HttpResponse(main_html)


def about(request):
    logger.info('About page accessed')
    return HttpResponse(about_html)

# Create your views here.

