from django.test import TestCase
from resume.models import Job
from django.urls import reverse

class WorkPageListTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Create authors for pagination tests
        number_of_jobs = 12
        for job_id in range(number_of_jobs):
            Job.objects.create(slug=f'comp{job_id}', title=f'company{job_id}', description=f'About company{job_id}')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'users/about.html')

    def test_lists_all_jobs(self):
        #Get second page and confirm it has (exactly)
        counter_jobs = 13 #  range does not include 13!
        for elem in range(counter_jobs):
            resp = self.client.get(reverse('about')+ f'?page={elem}')
        self.assertEqual(resp.status_code, 200)

    def test_lists_overflow_jobs(self):
        #Get second page when overflow
        resp = self.client.get(reverse('about')+ '?page=13')
        self.assertNotEqual(resp.status_code, 200)