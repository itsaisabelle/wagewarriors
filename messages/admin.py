from django.contrib import admin

# Register your models here.
class messages(admin.ModelAdmin):
    idConvo = admin.IntegerField()
    recruiterIDFK = admin.ForeignKey('account.recruiter', on_delete=admin.CASCADE)
    jobSeekerIDFK = admin.ForeignKey('account.jobSeeker', on_delete=admin.CASCADE)
    message = admin.TextField()