from django.db import models
from accounts.models import CustomUser
from django.contrib.auth.models import AbstractUser


class MailModel(models.Model):
    class Meta:
        verbose_name_plural = "メール"
        db_table = "mail"

    def __str__(self):
        return self.title

    author = models.ForeignKey(
        CustomUser,
        verbose_name="お名前",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="author_name"
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

    send_to = models.ForeignKey(
        CustomUser,
        verbose_name="送信相手",
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        related_name="receiver_name"
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




