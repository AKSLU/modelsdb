import migrations 
import context_db 
import models

migrations.create_table()
users = models.Users.all_users()
obj = models.Users("akslulog", "pass", "worker")
obj.save()
obj = models.Users("adminuser", "pass123", "admin")
obj.save()
obj = models.Users("adminuser", "pass123", "texpoderzka")
obj.save()

print(context_db.filtered_context())


