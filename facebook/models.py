from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# comment options

# option_1 = 'Nice Post!'
# option_2 = 'I am not agree with you!'
# option_3 = 'Good opinion'
# option_4 = 'Cool sentences'

# all_comments = [
# (option_1, 'Nice Post!'),
# (option_2, 'I am not agree with you!'),
# (option_3, 'Good opinion'),
# (option_4, 'Cool sentences'),
# ]

# end comment options

# Post status options

status = 'I like Pizza'
status1 = 'Hello World'
status2 = 'What is coronavirus'
status3 = 'What is the meaning of life'

all_status = [
(status, 'I like Pizza'),
(status1, 'Hello World'),
(status2, 'What is coronavirus'),
(status3, 'What is the meaning of life'),
]

# end Post status options

class Post(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=50,
        choices=all_status,
        default='I like Pizza',
    )
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.status


class Comment(models.Model):
    # option_1 = models.CharField(
    #     max_length=50,
    #     choices=all_comments,
    #     default='Nice Post!',
    # )
    comment_name = models.CharField(max_length=50,)


    PS = '0$'
    PS1 = '1$'
    PS2 = '2$'

    all_PS = [
        (PS, '0$'),
        (PS1, '1$'),
        (PS2, '2$'),

    ]
    PS = models.CharField(
        max_length=50,
        choices=all_PS,
        default='0$',
    )

    burden = '0$'
    burden1 = '1$'
    burden2 = '2$'
    
    all_burden = [
        (burden, '0$'),
        (burden1, '1$'),
        (burden2, '2$'),

    ]
    burden = models.CharField(
        max_length=50,
        choices=all_burden,
        default='0$',
    )

    benefit = '0$'
    benefit1 = '1$'
    benefit2 = '2$'
    
    all_benefit = [
        (benefit, '0$'),
        (benefit1, '1$'),
        (benefit2, '2$'),

    ]
    benefit = models.CharField(
        max_length=50,
        choices=all_benefit,
        default='0$',
    )
    def __str__(self):
        return self.comment_name


class Status(models.Model):

    status_1 = models.CharField(max_length=50)

    PS = '0$'
    PS1 = '1$'
    PS2 = '2$'

    all_PS = [
        (PS, '0$'),
        (PS1, '1$'),
        (PS2, '2$'),

    ]
    PS = models.CharField(
        max_length=50,
        choices=all_PS,
        default='0$',
    )

    burden = '0$'
    burden1 = '1$'
    burden2 = '2$'
    
    all_burden = [
        (burden, '0$'),
        (burden1, '1$'),
        (burden2, '2$'),

    ]
    burden = models.CharField(
        max_length=50,
        choices=all_burden,
        default='0$',
    )

    benefit = '0$'
    benefit1 = '1$'
    benefit2 = '2$'
    
    all_benefit = [
        (benefit, '0$'),
        (benefit1, '1$'),
        (benefit2, '2$'),

    ]
    benefit = models.CharField(
        max_length=50,
        choices=all_benefit,
        default='0$',
    )
    def __str__(self):
        return self.status_1

class Post_Comments(models.Model):
    

