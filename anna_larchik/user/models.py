from django.db import models


class Test(models.Model):
    """Model definition for Test."""

    # TODO: Define fields here

    title = models.CharField(max_length=255)
    text = models.TextField(blank=True, max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        """Meta definition for Test."""
        # name = '@ofd'
        ordering = ['-updated']
        verbose_name = 'test'
        # verbose_name_plural = 'Tests'

    def __str__(self):
        """Unicode representation of Test."""
        return self.title


class Columns(models.Model):
    """Model definition for Columns."""

    name = models.CharField(max_length=50)
    k = models.IntegerField()

    class Meta:
        """Meta definition for Columns."""

        verbose_name = 'Ценовые колонки'
        verbose_name_plural = 'Columnss'

    def __str__(self):
        """Unicode representation of Columns."""
        return self.name


class Users(models.Model):
    """Model definition for Users."""

    user_id = models.IntegerField()
    username = models.CharField(max_length=128, null=True)
    fullname = models.CharField(max_length=128, null=True)
    role = models.ForeignKey(Columns, null=True, on_delete=models.CASCADE)
    referal_code = models.IntegerField()
    referal_id = models.IntegerField(null=True)
    balance = models.IntegerField(null=True)

    class Meta:
        """Meta definition for Users."""

        verbose_name = 'Users'
        verbose_name_plural = 'Userss'

    def __str__(self):
        """Unicode representation of Users."""
        return self.username


class Categories(models.Model):
    """Model definition for Category."""

    # TODO: Define fields here
    name = models.CharField(max_length=64)
    desc = models.CharField(max_length=255)
    pic = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name


class Subcategories(models.Model):
    """Model definition for Subcategories."""

    name = models.CharField(max_length=128)
    category = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Subcategories."""

        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'

    def __str__(self):
        """Unicode representation of Subcategories."""
        return self.name


class Items(models.Model):
    """Model definition for Item."""

    # TODO: Define fields here
    name = models.CharField(max_length=255)
    desc = models.TextField(max_length=512)
    minimum = models.IntegerField()
    price = models.IntegerField()
    stored = models.CharField(max_length=50)
    count = models.IntegerField()
    category = models.ForeignKey(Categories, null=True, on_delete=models.CASCADE)
    subcategory_id = models.IntegerField(null=True)

    class Meta:
        """Meta definition for Item."""

        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        """Unicode representation of Item."""
        return self.name


class Purchases(models.Model):
    """Model definition for Purchase."""

    # TODO: Define fields here
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)
    item = models.ForeignKey(Items, null=True, on_delete=models.CASCADE)
    amount = models.IntegerField()
    price = models.IntegerField()

    # class Meta:
    #     """Meta definition for Purchase."""

    #     verbose_name = 'Покупки'
    #     verbose_name_plural = 'Покупки'

    def __str__(self):
        """Unicode representation of Purchase."""
        return self.item


class Mlm(models.Model):
    """Model definition for Mlm."""

    lvl = models.IntegerField()
    coe = models.IntegerField()

    class Meta:
        """Meta definition for Mlm."""

        verbose_name = 'Реферальная система'
        verbose_name_plural = 'Реферальная система'

    def __str__(self):
        """Unicode representation of Mlm."""
        return self.lvl


class Answers(models.Model):
    """Model definition for Answers."""

    answer = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Answers."""

        verbose_name = 'Answers'
        verbose_name_plural = 'Answerss'

    def __str__(self):
        """Unicode representation of Answers."""
        return self.answer


class Polled(models.Model):
    """Model definition for Polled."""

    answer = models.ForeignKey(Answers, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(Users, null=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Polled."""

        verbose_name = 'Polled'
        verbose_name_plural = 'Polleds'

    def __str__(self):
        """Unicode representation of Polled."""
        pass


class Questions(models.Model):
    """Model definition for Questions."""

    question = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Questions."""

        verbose_name = 'Вопрос'
        verbose_name_plural = 'Questionss'

    def __str__(self):
        """Unicode representation of Questions."""
        return self.answer


class Polls(models.Model):
    """Model definition for Polls."""

    question = models.ForeignKey(Questions, null=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, null=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Polls."""

        verbose_name = 'Опросы'
        verbose_name_plural = 'Опросы'

    def __str__(self):
        """Unicode representation of Polls."""
        pass


class Tags(models.Model):
    """Model definition for Tags."""

    tag = models.CharField(max_length=50)

    class Meta:
        """Meta definition for Tags."""

        verbose_name = 'Tags'
        verbose_name_plural = 'Tagss'

    def __str__(self):
        """Unicode representation of Tags."""
        return self.tag


class Tagged(models.Model):
    """Model definition for Tagged."""

    tag = models.ForeignKey(Tags, null=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answers, null=True, on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Tagged."""

        verbose_name = 'Tagged'
        verbose_name_plural = 'Taggeds'

    def __str__(self):
        """Unicode representation of Tagged."""
        return self.tag


class Mailing(models.Model):
    """Model definition for Mailing."""

    # TODO: Define fields here

    text = models.TextField(max_length=512)
    column = models.CharField(max_length=255, blank=True)
    purchase = models.IntegerField(blank=True)
    tag = models.CharField(max_length=255, blank=True)
    poll = models.IntegerField(blank=True)

    class Meta:
        """Meta definition for Mailing."""

        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'

    def __str__(self):
        """Unicode representation of Mailing."""
        return self.text
