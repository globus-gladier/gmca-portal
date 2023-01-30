import os
# from django.conf import settings
from django.apps import AppConfig

from gmca_portal import fields

APP_DIR = os.path.join(os.path.dirname(__file__))


class GMCAIndexConfig(AppConfig):
    name = 'gmca_portal'


SEARCH_INDEXES = {
    'gmca': {
        'uuid': '808dc518-511a-4de0-af6f-fcf41da4767b',
        'name': 'GMCA Index',
        'group': 'f08083f3-db94-11ec-9616-51db4d10f5bd',
        'base_templates': 'globus-portal-framework/v2/',
        'tabbed_project': False,
        'access': 'private',
        'template_override_dir': 'gmca',
        'description': (
            'X-ray Photon Correlation Spectroscopy (XPCS) is a technique to '
            'study dynamics in materials at nanoscale by identifying '
            'correlations in time series of area detector images'
        ),
        'fields': [
            ('title', fields.title),
            ('globus_app_link', fields.globus_app_link),
            'dc',
            ('copy_to_clipboard_link', fields.https_url),
            ('search_results', fields.search_results),
        ],
        'facets': [
            {
                "name": "Creator",
                "field_name": "dc.creators.creatorName",

            },
            {
                "name": "Dates",
                "field_name": "dc.dates.date",
                "type": "date_histogram",
                "date_interval": "day",
            },
        ]
    }
}
