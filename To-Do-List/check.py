# import unittest
# from models.task import Task
# from models.task_manager import TaskManager

# class TestTaskManager(unittest.TestCase):
#     def setUp(self):
#         # Use a test file to avoid interfering with actual data
#         self.manager = TaskManager(filepath='data/test_tasks.json')

#     def tearDown(self):
#         # Clean up test file after tests
#         import os
#         if os.path.exists('data/test_tasks.json'):
#             os.remove('data/test_tasks.json')

#     def test_add_task(self):
#         task = Task(description="Test Task")
#         self.manager.add_task(task)
#         self.assertEqual(len(self.manager.tasks), 1)
#         self.assertEqual(self.manager.tasks[0].description, "Test Task")

#     def test_delete_task(self):
#         task = Task(description="Delete Task")
#         self.manager.add_task(task)
#         self.manager.delete_task(task.id)
#         self.assertEqual(len(self.manager.tasks), 0)

#     def test_update_task(self):
#         task = Task(description="Old Description")
#         self.manager.add_task(task)
#         self.manager.update_task(task.id, description="New Description")
#         updated_task = self.manager.get_task(task.id)
#         self.assertEqual(updated_task.description, "New Description")

#     def test_list_tasks(self):
#         task1 = Task(description="Task 1", status="Incomplete")
#         task2 = Task(description="Task 2", status="Complete")
#         self.manager.add_task(task1)
#         self.manager.add_task(task2)
#         incomplete = self.manager.list_tasks(filter_status="Incomplete")
#         self.assertEqual(len(incomplete), 1)
#         self.assertEqual(incomplete[0].description, "Task 1")

# if __name__ == '__main__':
#     unittest.main()
