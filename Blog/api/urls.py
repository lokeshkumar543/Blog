from django.urls import path
from django.conf.urls.static import static
from Blog import settings
from api import views
from Blog.settings import *

urlpatterns = [
    path('',views.listing_data),
    path('add-blog/',views.add),
    path('delete/<int:num>/',views.delete),
    # £path('Home/<num>/',views.HomeClassView.as_view()),

]

