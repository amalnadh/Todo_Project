
from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.add,name='add'),
    # path('delete/<int:taskid>/',views.delete,name='delete'),
    # path('update/<int:id>/', views.update, name='update'),
    path('classview/',views.Tasklistview.as_view(),name='classview'),
    path('clsdtl/<int:pk>/',views.Taskdetailview.as_view(),name='clsdtl'),
    path('cbvupdate/<int:pk>/',views.Updateview.as_view(),name="cbvupdate"),
    path('cbvdelete/<int:pk>/',views.Deleteview.as_view(),name="cbvdelete"),


]
