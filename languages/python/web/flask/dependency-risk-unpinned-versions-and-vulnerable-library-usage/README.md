Проверка unpinned версий реализована в python-скрипте check_pinned_deps.py и вынесена отдельным policy в CI.

В CI добавить шаг:

- name: Check pinned dependencies
  run: |
    pip install toml
    python check_pinned_deps.py

## Что проверяет check_pinned_deps.py 

### requirements.txt:

Строки без ==<версия> (например, flask>2.0).

Версии с операторами (>=, ~=, *).

Комментарии и пустые строки игнорируются.

### pyproject.toml (Poetry):

Зависимости в [tool.poetry.dependencies] и группах [tool.poetry.group.<name>.dependencies].

Формат package = "==1.2.3" или package = {version = "==1.2.3"}.

Отмечает, если версия не в точном формате ==<цифры> или просто <цифры>.

Пример вывода
Если всё ок:

Все зависимости зафиксированы (==<версия>). OK.
Если есть проблемы:

НАЙДЕНЫ НЕЗАФИКСИРОВАННЫЕ ЗАВИСИМОСТИ:
  requirements.txt:3: requests>=2.30.0 — нефиксированная версия
  pyproject.toml: flask == ^2.3.2 — нефиксированная версия
Примечания
Скрипт учитывает комментарии после # в requirements.txt.

Для Poetry поддерживает оба формата указания версий: строковый и словарный.

Если какого‑то файла нет (например, только Poetry), скрипт выведет предупреждение, но продолжит проверку другого.

