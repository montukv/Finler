from django import forms
from expense_tracker.models import expense

class expenseform(forms.ModelForm):
	class Meta:
		model = expense
		fields =['name','cost']