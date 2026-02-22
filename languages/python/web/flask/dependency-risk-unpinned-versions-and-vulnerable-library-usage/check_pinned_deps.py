#!/usr/bin/env python3
import re
import sys
from pathlib import Path
import toml  # требуется: pip install toml

# Паттерн для НЕзафиксированных версий (всё, кроме точного ==<номер>)
UNPINNED_PATTERN = re.compile(
    r'^(?!==\d+(\.\d+)*(\.[a-zA-Z0-9]+)?$)'  # не начинается с ==<версия>
    r'([<>~*^]|==\d+\.\d+\.\d+[a-zA-Z]|(?<!=)=\d)'  # или содержит операторы/суффиксы
)

def check_requirements_txt(path: Path) -> list:
    issues = []
    if not path.exists():
        print(f"WARNING: {path} не найден.")
        return issues

    with open(path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line or line.startswith('#') or line.startswith('-'):
                continue

            # Извлекаем имя пакета и версию (если есть)
            pkg = line.split('#')[0].strip()  # убираем комментарии
            if '==' not in pkg:
                issues.append(f"requirements.txt:{line_num}: {pkg} — нет ==<версии>")
                continue

            version_part = pkg.split('==', 1)[1]
            if UNPINNED_PATTERN.search(version_part):
                issues.append(f"requirements.txt:{line_num}: {pkg} — нефиксированная версия")

    return issues


def check_poetry_pyproject(path: Path) -> list:
    issues = []
    if not path.exists():
        print(f"WARNING: {path} не найден.")
        return issues

    try:
        data = toml.load(path)
    except Exception as e:
        issues.append(f"pyproject.toml: ошибка чтения TOML: {e}")
        return issues

    # Ищем зависимости в [tool.poetry.dependencies] и [tool.poetry.group.*.dependencies]
    deps_sections = []
    tool = data.get('tool', {})
    poetry = tool.get('poetry', {})

    # Основные зависимости
    if 'dependencies' in poetry:
        deps_sections.append(poetry['dependencies'])

    # Группы зависимостей (Poetry 1.2+)
    for group_name, group in poetry.get('group', {}).items():
        if 'dependencies' in group:
            deps_sections.append(group['dependencies'])

    for section in deps_sections:
        for pkg_name, version in section.items():
            if isinstance(version, str):
                if '==' not in version and not re.match(r'^\d+\.\d+\.\d+$', version):
                    issues.append(f"pyproject.toml: {pkg_name} == {version} — нефиксированная версия")
            elif isinstance(version, dict):
                # Поддержка формата {version = "...", ...}
                ver_str = version.get('version', '')
                if '==' not in ver_str and not re.match(r'^\d+\.\d+\.\d+$', ver_str):
                    issues.append(f"pyproject.toml: {pkg_name} == {ver_str} — нефиксированная версия")

    return issues

def main():
    issues = []
    issues.extend(check_requirements_txt(Path('requirements.txt')))
    issues.extend(check_poetry_pyproject(Path('pyproject.toml')))

    if issues:
        print("НАЙДЕНЫ НЕЗАФИКСИРОВАННЫЕ ЗАВИСИМОСТИ:")
        for issue in issues:
            print(f!  {issue}")
        sys.exit(1)  # Сигнализируем об ошибке в CI
    else:
        print("Все зависимости зафиксированы (==<версия>). OK.")
        sys.exit(0)

if __name__ == '__main__':
    main()
