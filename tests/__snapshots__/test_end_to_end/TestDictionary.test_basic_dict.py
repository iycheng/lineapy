import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

session = SessionContext(
    id=get_new_id(),
    environment_type=SessionType.SCRIPT,
    creation_time=datetime.datetime(1, 1, 1, 0, 0),
    working_directory="dummy_linea_repo/",
)
source_1 = SourceCode(
    id=get_new_id(),
    code="x = {'a': 1, 'b': 2}",
    location=PosixPath("[source file path]"),
)
variable_1 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=20,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=1,
            col_offset=4,
            end_lineno=1,
            end_col_offset=20,
            source_code=source_1.id,
        ),
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=5,
                                    end_lineno=1,
                                    end_col_offset=8,
                                    source_code=source_1.id,
                                ),
                                value="a",
                            ).id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=10,
                                    end_lineno=1,
                                    end_col_offset=11,
                                    source_code=source_1.id,
                                ),
                                value=1,
                            ).id,
                        ).id,
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="__build_tuple__",
                    ).id,
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=13,
                                    end_lineno=1,
                                    end_col_offset=16,
                                    source_code=source_1.id,
                                ),
                                value="b",
                            ).id,
                        ).id,
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=1,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=1,
                                    col_offset=18,
                                    end_lineno=1,
                                    end_col_offset=19,
                                    source_code=source_1.id,
                                ),
                                value=2,
                            ).id,
                        ).id,
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="__build_tuple__",
                    ).id,
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="__build_dict__",
        ).id,
    ).id,
    assigned_variable_name="x",
)
