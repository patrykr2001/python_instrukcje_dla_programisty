from pathlib import Path

contents = 'Uwielbiam programować!\n'
contents += 'Uwielbiam tworzyć gry!\n'
contents += 'Uwielbiam pracować z danymi!\n'

path = Path('programming.txt')
path.write_text(contents, encoding='utf8')
