from __future__ import annotations

import nox


def generate(
    session: nox.Session,
    *,
    schema: str | None = 'tests/data/schema.prisma',
    clean: bool = True,
) -> None:
    if clean:
        session.run('python', '-m', 'prisma_cleanup')

    args = (f'--schema={schema}', ) if schema else ()
    session.run('prisma', 'generate', *args)
