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
    code="""import lineapy
import pandas as pd
import matplotlib.pyplot as plt
from PIL.Image import open

df = pd.read_csv(\'tests/simple_data.csv\')
plt.imsave(\'simple_data.png\', df)

img = open(\'simple_data.png\')
img = img.resize([200, 200])

lineapy.linea_publish(img, "Graph With Image")
""",
    location=PosixPath("[source file path]"),
)
import_1 = ImportNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=1,
        col_offset=0,
        end_lineno=1,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    library=Library(
        id=get_new_id(),
        name="lineapy",
    ),
)
call_5 = CallNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=33,
        source_code=source_1.id,
    ),
    arguments=[
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=0,
            value_node_id=LiteralNode(
                id=get_new_id(),
                session_id=session.id,
                source_location=SourceLocation(
                    lineno=7,
                    col_offset=11,
                    end_lineno=7,
                    end_col_offset=28,
                    source_code=source_1.id,
                ),
                value="simple_data.png",
            ).id,
        ).id,
        ArgumentNode(
            id=get_new_id(),
            session_id=session.id,
            positional_order=1,
            value_node_id=VariableNode(
                id=get_new_id(),
                session_id=session.id,
                source_location=SourceLocation(
                    lineno=6,
                    col_offset=0,
                    end_lineno=6,
                    end_col_offset=41,
                    source_code=source_1.id,
                ),
                source_node_id=CallNode(
                    id=get_new_id(),
                    session_id=session.id,
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=5,
                        end_lineno=6,
                        end_col_offset=41,
                        source_code=source_1.id,
                    ),
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=6,
                                    col_offset=17,
                                    end_lineno=6,
                                    end_col_offset=40,
                                    source_code=source_1.id,
                                ),
                                value="tests/simple_data.csv",
                            ).id,
                        ).id
                    ],
                    function_id=CallNode(
                        id=get_new_id(),
                        session_id=session.id,
                        source_location=SourceLocation(
                            lineno=6,
                            col_offset=5,
                            end_lineno=6,
                            end_col_offset=16,
                            source_code=source_1.id,
                        ),
                        arguments=[
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=0,
                                value_node_id=ImportNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    source_location=SourceLocation(
                                        lineno=2,
                                        col_offset=0,
                                        end_lineno=2,
                                        end_col_offset=19,
                                        source_code=source_1.id,
                                    ),
                                    library=Library(
                                        id=get_new_id(),
                                        name="pandas",
                                    ),
                                    alias="pd",
                                ).id,
                            ).id,
                            ArgumentNode(
                                id=get_new_id(),
                                session_id=session.id,
                                positional_order=1,
                                value_node_id=LiteralNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    value="read_csv",
                                ).id,
                            ).id,
                        ],
                        function_id=LookupNode(
                            id=get_new_id(),
                            session_id=session.id,
                            name="getattr",
                        ).id,
                    ).id,
                ).id,
                assigned_variable_name="df",
            ).id,
        ).id,
    ],
    function_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=7,
            col_offset=0,
            end_lineno=7,
            end_col_offset=10,
            source_code=source_1.id,
        ),
        arguments=[
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=0,
                value_node_id=ImportNode(
                    id=get_new_id(),
                    session_id=session.id,
                    source_location=SourceLocation(
                        lineno=3,
                        col_offset=0,
                        end_lineno=3,
                        end_col_offset=31,
                        source_code=source_1.id,
                    ),
                    library=Library(
                        id=get_new_id(),
                        name="matplotlib.pyplot",
                    ),
                    alias="plt",
                ).id,
            ).id,
            ArgumentNode(
                id=get_new_id(),
                session_id=session.id,
                positional_order=1,
                value_node_id=LiteralNode(
                    id=get_new_id(),
                    session_id=session.id,
                    value="imsave",
                ).id,
            ).id,
        ],
        function_id=LookupNode(
            id=get_new_id(),
            session_id=session.id,
            name="getattr",
        ).id,
    ).id,
)
variable_4 = VariableNode(
    id=get_new_id(),
    session_id=session.id,
    source_location=SourceLocation(
        lineno=10,
        col_offset=0,
        end_lineno=10,
        end_col_offset=28,
        source_code=source_1.id,
    ),
    source_node_id=CallNode(
        id=get_new_id(),
        session_id=session.id,
        source_location=SourceLocation(
            lineno=10,
            col_offset=6,
            end_lineno=10,
            end_col_offset=28,
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
                    source_location=SourceLocation(
                        lineno=10,
                        col_offset=17,
                        end_lineno=10,
                        end_col_offset=27,
                        source_code=source_1.id,
                    ),
                    arguments=[
                        ArgumentNode(
                            id=get_new_id(),
                            session_id=session.id,
                            positional_order=0,
                            value_node_id=LiteralNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_location=SourceLocation(
                                    lineno=10,
                                    col_offset=18,
                                    end_lineno=10,
                                    end_col_offset=21,
                                    source_code=source_1.id,
                                ),
                                value=200,
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
                                    lineno=10,
                                    col_offset=23,
                                    end_lineno=10,
                                    end_col_offset=26,
                                    source_code=source_1.id,
                                ),
                                value=200,
                            ).id,
                        ).id,
                    ],
                    function_id=LookupNode(
                        id=get_new_id(),
                        session_id=session.id,
                        name="__build_list__",
                    ).id,
                ).id,
            ).id
        ],
        function_id=CallNode(
            id=get_new_id(),
            session_id=session.id,
            source_location=SourceLocation(
                lineno=10,
                col_offset=6,
                end_lineno=10,
                end_col_offset=16,
                source_code=source_1.id,
            ),
            arguments=[
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=0,
                    value_node_id=VariableNode(
                        id=get_new_id(),
                        session_id=session.id,
                        source_location=SourceLocation(
                            lineno=9,
                            col_offset=0,
                            end_lineno=9,
                            end_col_offset=29,
                            source_code=source_1.id,
                        ),
                        source_node_id=CallNode(
                            id=get_new_id(),
                            session_id=session.id,
                            source_location=SourceLocation(
                                lineno=9,
                                col_offset=6,
                                end_lineno=9,
                                end_col_offset=29,
                                source_code=source_1.id,
                            ),
                            arguments=[
                                ArgumentNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    positional_order=0,
                                    value_node_id=LiteralNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        source_location=SourceLocation(
                                            lineno=9,
                                            col_offset=11,
                                            end_lineno=9,
                                            end_col_offset=28,
                                            source_code=source_1.id,
                                        ),
                                        value="simple_data.png",
                                    ).id,
                                ).id
                            ],
                            function_id=VariableNode(
                                id=get_new_id(),
                                session_id=session.id,
                                source_node_id=CallNode(
                                    id=get_new_id(),
                                    session_id=session.id,
                                    arguments=[
                                        ArgumentNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            positional_order=0,
                                            value_node_id=ImportNode(
                                                id=get_new_id(),
                                                session_id=session.id,
                                                source_location=SourceLocation(
                                                    lineno=4,
                                                    col_offset=0,
                                                    end_lineno=4,
                                                    end_col_offset=26,
                                                    source_code=source_1.id,
                                                ),
                                                library=Library(
                                                    id=get_new_id(),
                                                    name="PIL.Image",
                                                ),
                                                attributes={"open": "open"},
                                            ).id,
                                        ).id,
                                        ArgumentNode(
                                            id=get_new_id(),
                                            session_id=session.id,
                                            positional_order=1,
                                            value_node_id=LiteralNode(
                                                id=get_new_id(),
                                                session_id=session.id,
                                                value="open",
                                            ).id,
                                        ).id,
                                    ],
                                    function_id=LookupNode(
                                        id=get_new_id(),
                                        session_id=session.id,
                                        name="getattr",
                                    ).id,
                                ).id,
                                assigned_variable_name="open",
                            ).id,
                        ).id,
                        assigned_variable_name="img",
                    ).id,
                ).id,
                ArgumentNode(
                    id=get_new_id(),
                    session_id=session.id,
                    positional_order=1,
                    value_node_id=LiteralNode(
                        id=get_new_id(),
                        session_id=session.id,
                        value="resize",
                    ).id,
                ).id,
            ],
            function_id=LookupNode(
                id=get_new_id(),
                session_id=session.id,
                name="getattr",
            ).id,
        ).id,
    ).id,
    assigned_variable_name="img",
)
