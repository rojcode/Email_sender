from django import forms


class ShareForm(forms.Form):
    subject = forms.CharField(widget=forms.TextInput(attrs={'id': 'name-59db',
                                                            'class': 'u-border-1 u-border-grey-80 u-border-radius-10 u-grey-70 u-input u-input-round u-input-1',
                                                            'placeholder': 'Enter your subject'}),label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id': 'email-59db',
                                                            'class': 'u-border-1 u-border-grey-80 u-border-radius-10 u-grey-70 u-input u-input-round u-input-2',
                                                            'placeholder': 'Enter email'}),label='')
    body = forms.CharField(widget=forms.Textarea(attrs={'id': 'message-59db',
                                                        'class': 'u-border-1 u-border-grey-80 u-border-radius-10 u-grey-70 u-input u-input-round u-input-3',
                                                        'placeholder': 'body'}),label='')
