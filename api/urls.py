from django.urls import path
from api import views


urlpatterns = [
    path('',views.listing_data),
    path('add-blog/',views.add),
    path('delete/<int:num>/',views.delete),
    # £path('Home/<num>/',views.HomeClassView.as_view()),

]

