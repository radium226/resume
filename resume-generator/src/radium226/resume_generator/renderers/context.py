from contextvars import ContextVar


CURRENT_CONTEXT = ContextVar("CURRENT_CONTEXT")


class RenderContext():

    def __init__(self):
        self.number_of_tables = 10

    def next_table_name(self) -> str:
        self.number_of_tables += 1
        return f"Tableau_{self.number_of_tables}"


def init_current_render_context() -> None:
    CURRENT_CONTEXT.set(RenderContext())


def get_current_render_context() -> RenderContext:
    return CURRENT_CONTEXT.get()
