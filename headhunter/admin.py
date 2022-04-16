from django.contrib import admin
from headhunter.models import Resume, Experiences, Educations, Vacancy, Respond, Message, RespondMessage

admin.site.register(Resume)
admin.site.register(Experiences)
admin.site.register(Educations)

admin.site.register(Vacancy)
admin.site.register(Respond)
admin.site.register(Message)
admin.site.register(RespondMessage)
