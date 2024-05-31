"""Views for the server_guardian_api app."""
from django.views.generic import View
from django.http import HttpResponseForbidden
from django_libs.views_mixins import JSONResponseMixin
from django_libs.loaders import load_member
from .constants import SERVER_STATUS
from .default_settings import PROCESSORS, SECURITY_TOKEN


class ServerGuardianAPIView(JSONResponseMixin, View):
    """
    This view gathers and returns API metrics, that can be returned to the
    ``django-server-guardian``.

    """

    def get(self, request, *args, **kwargs):
        if request.GET.get('token') != SECURITY_TOKEN:
            return HttpResponseForbidden()
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        ctx = []
        for processor_path in PROCESSORS:
            processor = load_member(processor_path)
            try:
                ctx.append(processor())
            except Exception as ex:
                response = {
                    'label': 'error',
                    'status': SERVER_STATUS['DANGER'],
                    'info': (
                        'The server encountered an error while running this'
                        ' processor: "{0}"'.format(ex)
                    )
                }
                ctx.append(response)
        return ctx
