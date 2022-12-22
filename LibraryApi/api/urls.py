from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.bookshelf),
    path('add/', views.book_create),
    path('<title>', views.book_read),
    path('update/<title>', views.book_update),
    path('delete/<title>', views.book_delete),
    path('signup/',views.register),
    path('waiting/',views.wait,name='wait'),
    path('signup/<token>',views.confirmation)
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
