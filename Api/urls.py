from django.conf.urls import url
from .views import ColegioApi,EstudianteApi,DocenteApi,PuntuacionApi,CursoApi
urlpatterns = [
    url(r'^api/colegio/$',ColegioApi.as_view(),name='apicolegio'),
    url(r'^api/colegio/(?P<cod>\w+)/$',ColegioApi.as_view(),name='apicolegio'),
    url(r'^api/estudiante/$',EstudianteApi.as_view(),name='apiestudiante'),
    url(r'^api/estudiante/(?P<ced>\w+)/$',EstudianteApi.as_view(),name='apiestudiante'),
    url(r'^api/docente/$',DocenteApi.as_view(),name='apidocente'),
    url(r'^api/docente/(?P<ced>\w+)/$',DocenteApi.as_view(),name='apidocente'),
    url(r'^api/puntuacion/$',PuntuacionApi.as_view(),name='apipuntuacion'),
    url(r'^api/curso/$',CursoApi.as_view(), name='apicurso'),
    url(r'^api/curso/(?P<id>\w+)/$',CursoApi.as_view(), name='apicurso'),
]
