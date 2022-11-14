from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
 
urlpatterns=[
    path('bookshelf/',views.bookshelf),
    path('bookshelf/<title>',views.book_read)
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)