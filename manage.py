from flask_script import Manager
from flask_migrate import Migrate

from startup import app, db

manager = Manager(app)
# Migrate() 需要绑定app 和 db
migrate = Migrate(app, db)
# 子命令  MigrateCommand 包含三个方法 init migrate upgrade
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
