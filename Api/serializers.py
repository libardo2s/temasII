from rest_framework.serializers import ModelSerializer
from .models import Colegio,Estudiante,Puntuacion,Docente,User

class UsuarioSerialerzs(ModelSerializer):
    class Meta:
        model = User
        fields = ('username','password')


class ColegioSerialerzs(ModelSerializer):
    usuario = UsuarioSerialerzs(many=False,read_only=True)

    class Meta:
        model = Colegio
        fields = ('codigo','nombre','direccion','telefono','estado','usuario')


class EstudianteSerialerzs(ModelSerializer):

    usuario=UsuarioSerialerzs(many=False,read_only=True)

    class Meta:
        model= Estudiante
        fields=('tipo_documento','documento','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','sexo','fecha_nacimiento','usuario','correo')


class DocenteSerialerzs(ModelSerializer):
    usuario=UsuarioSerialerzs(many=False, read_only=True)
    class Meta:
        model = Docente
        fields = ('tipo_documento','documento','primer_nombre','segundo_nombre','primer_apellido','segundo_apellido','sexo','fecha_nacimiento','usuario','correo')


class PuntuacionSerialerzs(ModelSerializer):
    estudiante = EstudianteSerialerzs(many=False, read_only=True)
    class Meta:
        model = Puntuacion
        fields = ('estudiante','puntuacion','fecha')

