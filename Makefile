install: # установка poetry при первом клонировании или после изменения зависимостей
	poetry install


brain-games: # запуск модуля brain_games.py из директории brain_games/scripts/
	poetry run brain-games


build: # запуск сборки пакета и подтверждения правильности настройки
	poetry build


publish: # запуск отладки публикаци аргумент применяется, чтобы не добавлять пакет в каталог PyPI
	poetry publish --dry-run


package-install: # установка пакета из операционной системы - запускать из корневой директории проекта
	python3 -m pip install --user dist/*.whl


test-coverage:
	poetry run pytest --cov=hexlet_python_package --cov-report xml
