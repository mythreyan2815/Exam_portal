from django.contrib.auth.models import Group
group_exists = Group.objects.filter(name='Professor').exists()
print(group_exists)
