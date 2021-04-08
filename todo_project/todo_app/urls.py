from django.urls import path

from todo_app import views

urlpatterns = [
    path('',views.taskview,name='taskview'),
    path('deletetask/<int:taskid>',views.delete,name='deletetask'),
    path('updatetask/<int:updateid>',views.update,name='updatetask'),
    path('tasklist/',views.Tasklistview.as_view(),name='tasklist'),
    path('taskdetail/<int:pk>',views.Taskdetailview.as_view(),
         name='taskdetail'),
    path('taskupdate/<int:pk>',views.Taskupdateview.as_view(),
         name='taskupdate'),
    path('taskdelete/<int:pk>',views.Taskdeleteview.as_view(),
         name='taskdelete'),
    ]