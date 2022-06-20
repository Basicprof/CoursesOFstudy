serializers.py
    SubjectSerializer = Это сериализатор для Subject
siews.py                     urls.py  
    SubjectListView     subjects/список всех                       
         предметов, ложении, в формате JSON.
    SubjectDetailView subjects/<pk>/ http://127.0.0.1:8000/  
         api/subjects/1/. Подробности о предмете.
  
    создали  объект  DefaultRouter  и  зарегистрировали  набор  обработчиков с префиксом courses
        router = routers.DefaultRouter()
        router.register('courses', views.CourseViewSet)
    CourseViewSet(viewsets.ReadOnlyModelViewSet): реализует только для чтения через методы retrieve() и list()
                          path('', include(router.urls))
views.py 
    CourseSerializer = Сериализатор модели Курс    
    ModuleSerializer = Сериализатор модуля 
    //Теперь зачисление на курс реализованао спомодью маршрутизатора 
    <!-- CourseEnrollView = зачисляет студентов на курсы.
                       courses/<pk>/enroll/' -->
                    http://127.0.0.1:8000/api/courses/
                    http://127.0.0.1:8000/api/courses/1

