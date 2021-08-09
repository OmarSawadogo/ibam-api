from django.urls import path
from server import views

urlpatterns = [
    path("",views.ListCoursAPIView.as_view(),name="cours_list"),
    path("create/", views.CreateCoursAPIView.as_view(),name="cours_create"),
    path("update/<int:pk>/",views.UpdateCoursAPIView.as_view(),name="cours_todo"),
    path("delete/<int:pk>/",views.DeleteCoursAPIView.as_view(),name="cours_todo")
]