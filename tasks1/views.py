from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import Datetimeserializer
from datetime import datetime
from django.http import JsonResponse


def CustomAPI(request):
    current_datetime = datetime.now()
    formatted_date = current_datetime.strftime("%Y-%m-%d")
    formatted_time = current_datetime.strftime("%H:%M:%SZ")
    response_data={
        'current_date':formatted_date,
        'current_time': formatted_time
    }

    return JsonResponse(response_data)


class CustomAPI(APIView):
    def get(self, request):
        param_value = request.query_params.get("slack_name=olatunde&track=backend")
        current_datetime = datetime.now()
        utc_time = Datetimeserializer({'current_date': current_datetime.time()})

        response = { "slack_name": "olatunde", "current_day": "Friday", "utc_time": utc_time.data, "track": "backend", "github_file_url": "https://github.com/olatunde/TASK1-.git", "github_repo_url": "https://github.com/olatunde2/TASK1-/blob/main/tasks1/views.py", "status_code": 200}
   
        return Response(response)
