from rest_framework.views import APIView
from rest_framework.response import Response
from .models import User

class LogInView(APIView):
    def post(self, request):
        mail = request.data.get("mail")
        password = request.data.get("password")

        try:
            token_key = User.objects.log_in(mail, password)

            return Response({"token": token_key})

        except Exception as e:
            return Response({"Error": str(e)})

class SignInView(APIView):
    def post(self, request):
        mail = request.data.get("mail")
        name = request.data.get("name")
        surname = request.data.get("surname")
        password = request.data.get("password")

        try:
            User.objects.sign_in(mail, name, surname, password)

            return Response({"Mensaje": "Usuario creado con exito."})

        except Exception as e:
            return Response({"Error": str(e)})


