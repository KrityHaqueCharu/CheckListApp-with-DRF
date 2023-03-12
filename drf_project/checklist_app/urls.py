from django.urls import path
from checklist_app.views import test_api,TestAPIView,CheckListsAPIView,CheckListAPIView,CheckListItemCreateAPIView,CheckListItemAPIView
urlpatterns = [
    path('fbs/',test_api,name='test_api'),
    path('cbv/', TestAPIView.as_view()),
    path('api/checklists/', CheckListsAPIView.as_view()),
    path('api/checklists/<int:pk>/', CheckListAPIView.as_view()),
    path('api/checklistItem/create/', CheckListItemCreateAPIView.as_view()),
    path('api/checklistItem/<int:pk>/', CheckListItemAPIView.as_view()),
]