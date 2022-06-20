from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CourseEnrollForm
from django.views.generic.list import ListView
from courses.models import Course
from django.views.generic.detail import DetailView
class StudentRegistrationView(CreateView):
        template_name = 'students/student/registration.html'
        form_class = UserCreationForm
        success_url = reverse_lazy('student_course_list')
        def form_valid(self, form):
            result = super(StudentRegistrationView, self).form_valid(form)
            cd = form.cleaned_data
            user = authenticate(username=cd['username'],
                             password=cd['password1'])
            login(self.request, user)
            return result
#  обработчик StudentEnrollCourseView. Он занимается зачислением студен-
# тов на курсы
class StudentEnrollCourseView(LoginRequiredMixin, FormView):
    course = None
    form_class = CourseEnrollForm
    def form_valid(self, form):
        self.course = form.cleaned_data['course']
        self.course.students.add(self.request.user)
        return super(StudentEnrollCourseView, self).form_valid(form)
    def get_success_url(self):
        return reverse_lazy('student_course_detail', args=[self.course.id])
# наследуется от класса ListView, чтобы отображать объекты модели 
# Course в виде списка
#  Чтобы получить только курсы, связанные с текущим поль-
# зователем, мы переопределили метод get_queryset() и отфильтровали QuerySet 
# курсов по связи ManyToManyField со студентом.
class StudentCourseListView(LoginRequiredMixin, ListView):
    model = Course
    template_name = 'students/course/list.html'
    def get_queryset(self):
        qs = super(StudentCourseListView, self).get_queryset()
        return qs.filter(students__in=[self.request.user])
# переопределили метод get_query-
# set(), чтобы ограничить QuerySet курсов и работать только с теми, на которые 
# записан текущий пользователь
# переопределили метод get_query-
# set(), чтобы ограничить QuerySet курсов и работать только с теми, на которые 
# записан текущий пользователь
class StudentCourseDetailView(DetailView):
        model = Course
        template_name = 'students/course/detail.html'
     
        def get_queryset(self):
            qs = super(StudentCourseDetailView, self).get_queryset()
            return qs.filter(students__in=[self.request.user])
        def get_context_data(self, **kwargs):
            context = super(StudentCourseDetailView, self).get_context_data(**kwargs)
        # Получаем объект курса.
            course = self.get_object()
            if 'module_id' in self.kwargs:
            # Получаем текущий модуль по параметрам запроса.
               context['module'] = course.modules.get(id=self.kwargs['module_id'])
            else:
                # Получаем первый модуль.
                context['module'] = course.modules.all()[0]
            return context