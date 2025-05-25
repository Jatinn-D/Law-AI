from django.db import models

class UploadedPDF(models.Model):
    file = models.FileField(upload_to='pdfs/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.file.name

class ChatHistory(models.Model):
    pdf = models.ForeignKey(UploadedPDF, on_delete=models.CASCADE, related_name='chats')
    question = models.TextField()
    answer = models.TextField()
    asked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Q: {self.question[:30]}..."
