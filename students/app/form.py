from django import forms 
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

us_help_text='''
    <ul>
        <li>Bắt buộc.</li>
        <li>Tối đa 150 kí tự.</li>
    </ul>
'''

pas1_help_text='''
    <ul>
        <li>Mật khẩu của bạn không được quá giống với thông tin cá nhân khác của bạn.</li>
        <li>Mật khẩu của bạn phải chứa ít nhất 8 ký tự.</li>
        <li>Mật khẩu của bạn không được là mật khẩu thường được sử dụng.</li>
        <li>Mật khẩu của bạn không được hoàn toàn bằng số.</li>
    </ul>
'''

pas2_help_text='''Nhập cùng một mật khẩu như trước, để xác minh.'''
     
class Bieumau_dangky_thanhvien(UserCreationForm):
    email = forms.CharField(max_length=254, 
                          required=True, 
                          widget=forms.EmailInput(),
                          label='Thư điện tử')
  
    def __init__(self, *args, **kwargs):
        super(Bieumau_dangky_thanhvien, self).__init__(*args, **kwargs)
    
        self.fields['username'].label = "Tài khoản"
        self.fields['username'].help_text = us_help_text
    
        self.fields['password1'].label = "Mật khẩu"
        self.fields['password1'].help_text = pas1_help_text
        self.fields['password2'].label = "Xác nhận mật khẩu"
        self.fields['password2'].help_text = pas2_help_text
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')