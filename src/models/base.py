from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    def __repr__(self):
        repr_cols_num = 3
        repr_cols = tuple()

        cols = []
        for idx, col in enumerate(self.__table__.columns.keys()):
            if col in repr_cols or idx < repr_cols_num:
                cols.append(f'{col}={getattr(self, col)}')

        return f'<{self.__class__.__name__} {", ".join(cols)}>'
