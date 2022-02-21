from unicodedata import name
from . import views
from django.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('notes',views.get_notes, name= 'notes'),
    path('notes/create/', views.create_note, name="create-note"),
    path('notes/<str:pk>/update/',views.update_note, name= 'update-note'),
    path('notes/<str:pk>/delete/',views.delete_note, name= 'delete-note'),
    path('notes/<str:pk>/',views.get_note, name= 'note'),



]
