from rest_framework.routers import DefaultRouter
from rest_framework_nested.routers import NestedDefaultRouter

from huscy.project_ethics import views
from huscy.projects.api_urls import project_router


router = DefaultRouter()
router.register('ethicboards', views.EthicBoardViewSet)

project_router.register('ethics', views.EthicViewSet, basename='ethic')

ethic_router = NestedDefaultRouter(project_router, 'ethics', lookup='ethic')
ethic_router.register('ethicfiles', views.EthicsFileViewSet, basename='ethicfile')

urlpatterns = router.urls
urlpatterns += project_router.urls
urlpatterns += ethic_router.urls
