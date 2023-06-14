from pathlib import Path
from pydantic import BaseModel
from prisma.generator import GenericGenerator, GenericData, Manifest


class Config(BaseModel):
    header: str = '# My Prisma Models'


Data = GenericData[Config]


class MyGenerator(GenericGenerator[Data]):
    def get_manifest(self) -> Manifest:
        return Manifest(
            name='My Cool Generator',
            default_output=Path(__file__).parent / 'generated.md',
        )

    def generate(self, data: Data) -> None:
        lines = [
            data.generator.config.header,
            '',
        ]
        lines.extend(f'- {model.name}' for model in data.dmmf.datamodel.models)
        output = Path(data.generator.output.value)
        output.write_text('\n'.join(lines))


if __name__ == '__main__':
    MyGenerator.invoke()
