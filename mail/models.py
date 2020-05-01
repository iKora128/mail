from django.db import models
from django.contrib.auth.models import User


class MailModel(models.Model):
    class Meta:
        verbose_name_plural = "メール"
        db_table = "mail"

    def __str__(self):
        return self.title

    author = models.ForeignKey(
        User,
        verbose_name="お名前",
        null=False,
        blank=False,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        verbose_name="タイトル",
        max_length=50,
        blank=False,
        null=False
    )

    text = models.CharField(
        verbose_name="テキスト",
        max_length=200,
        blank=False,
        null=False
    )

    like_counter = models.IntegerField(
        verbose_name="いいね数",
        default=0,
        blank=True,
        null=False
    )

    created_at = models.DateField(
        verbose_name="作成時間",
        blank=True,
        null=True,
        auto_now_add=True
    )




