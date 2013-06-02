from django.forms import ModelForm

class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        fields = ['user', 'school', 'grade', 'following', 'address', 'bio']
