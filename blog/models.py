from django.db import models
from django.utils import timezone

class Post(models.Model):
	title = models.CharField(max_length = 200, verbose_name = 'Titulo')
	author = models.ForeignKey("auth.User", on_delete = models.CASCADE, verbose_name = 'Autor')
	image = models.ImageField(upload_to = 'images', null = True, blank = True)
	text = models.TextField(verbose_name = 'Texto do blog')
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return '{} - {}'.format(self.title, self.author)

	def post_new(request):
		if request.method == "POST":
			form=Postform(request.POST)
			if form.is_valid():
				post = form.save(commit = False)
				post.author = request.user
				post.published_date = timezone.now()
				post.save()
				return reidrect('post_detail', pk= post.pk)
		else:
		form = Postform()
		return render(request, 'blog/post_edit.html', {'form':form})



# Create your models here.
