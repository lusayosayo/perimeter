from .reports.html import urlpatterns as reports_html

from .nodes.html import urlpatterns as nodes_html
from .nodes.json import urlpatterns as nodes_json

urlpatterns = []

urlpatterns.extend(reports_html)

urlpatterns.extend(nodes_html)
urlpatterns.extend(nodes_json)
