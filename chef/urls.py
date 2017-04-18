from django.conf.urls import url
import views
urlpatterns = [
	url(r'update_order_status/(?P<order_id>\d+)/$', views.update, name='update'),
	url(r'^$', views.chefview, name='chefview'),
]