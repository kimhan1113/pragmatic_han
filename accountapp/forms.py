from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *arg, **kwargs):
        super().__init__(*arg, **kwargs)

        self.fields['username'].disabled = True