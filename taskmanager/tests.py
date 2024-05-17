from django.test import TestCase
from django.urls import reverse
from .models import Task


class TaskManagerTests(TestCase):

    # Set up a few tasks for testing
    def setUp(self):
        self.task1 = Task.objects.create(title='Task 1', description='Description 1', completed=False)
        self.task2 = Task.objects.create(title='Task 2', description='Description 2', completed=True)

    # Test case 1: Create a new task
    def test_task_create(self):
        response = self.client.post(reverse('task_create'), {
            'title': 'Task 3',
            'description': 'Descripton 3',
            'completed': False,
        })
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 3)
        self.assertEqual(Task.objects.last().title, 'Task 3')

    # Test case 2: Retrieve the task list
    def test_task_list(self):
        response = self.client.get(reverse('task_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Description 1')

    # Test case 3: Retrieve task details
    def test_task_details(self):
        response = self.client.get(reverse('task_detail', args=[self.task1.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Task 1')
        self.assertContains(response, 'Description 1')

    # Test case 4: Update an existing task
    def test_update_task(self):
        response = self.client.post(reverse('task_edit', args=[self.task1.pk]), {
            'title': 'Task 1 updated',
            'description': 'Description 1 updated',
            'completed': True,
        })
        self.assertEqual(response.status_code, 302)
        self.task1.refresh_from_db()
        self.assertEqual(self.task1.title, 'Task 1 updated')
        self.assertEqual(self.task1.completed, True)

    # Test case 5: Delete an existing task
    def test_delete_task(self):
        response = self.client.post(reverse('task_delete', args=[self.task1.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Task.objects.count(), 1)
        self.assertFalse(Task.objects.filter(pk=self.task1.pk).exists())