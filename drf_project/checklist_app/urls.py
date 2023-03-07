from django.urls import path
from checklist_app.views import test_api,TestAPIView,CheckListAPIView
urlpatterns = [
    path('fbs/',test_api,name='test_api'),
    path('cbv/', TestAPIView.as_view()),
    path('api/checklists/', CheckListAPIView.as_view()),
]