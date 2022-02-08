from django.test import TestCase

from resume.models import Job

class JobModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Job.objects.create(slug='comp', title='company', description='About company')

    def test_slug_max_length(self):
        job=Job.objects.get(id=1)
        max_length = job._meta.get_field('title').max_length
        self.assertEquals(max_length,140)

    def test_site_max_length(self):
        job=Job.objects.get(id=1)
        max_length = job._meta.get_field('site').max_length
        self.assertEquals(max_length,200)

    def test_title_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('title').verbose_name
        self.assertEquals(field_label,'title')

    def test_slug_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('slug').verbose_name
        self.assertEquals(field_label,'slug')

    def test_description_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('description').verbose_name
        self.assertEquals(field_label,'description')

    def test_date_start_label(self):
        job=Job.objects.get(id=1)
        field_label = job._meta.get_field('date_start').verbose_name
        self.assertEquals(field_label,'Начало работы')

    def test_date_end_label(self):
        job=Job.objects.get(id=1)
        #print(str(job))
        field_label = job._meta.get_field('date_end').verbose_name
        self.assertEquals(field_label,'Окончание работы')

    def test_object_name_is_title(self):
        job=Job.objects.get(id=1)
        expected_object_name = (job.title)
        self.assertEquals(expected_object_name,str(job))

    def test_get_absolute_url(self):
        job=Job.objects.get(id=1)
        #This will also fail if the urlconf is not defined.
        self.assertEquals(job.get_absolute_url(),'/about')

