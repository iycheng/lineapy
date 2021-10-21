import datetime
from pathlib import *
from lineapy.data.types import *
from lineapy.utils import get_new_id

source_1 = SourceCode(
    code="""
ls = [1,2,3,4]
ls[0] = 1
a = 4
ls[1] = a
ls[2:3] = [30]
ls[3:a] = [40]
""",
    location=PosixPath("[source file path]"),
)
call_1 = CallNode(
    source_location=SourceLocation(
        lineno=2,
        col_offset=5,
        end_lineno=2,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="__build_list__",
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=6,
                end_lineno=2,
                end_col_offset=7,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=8,
                end_lineno=2,
                end_col_offset=9,
                source_code=source_1.id,
            ),
            value=2,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=10,
                end_lineno=2,
                end_col_offset=11,
                source_code=source_1.id,
            ),
            value=3,
        ).id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=2,
                col_offset=12,
                end_lineno=2,
                end_col_offset=13,
                source_code=source_1.id,
            ),
            value=4,
        ).id,
    ],
)
mutate_1 = MutateNode(
    source_id=call_1.id,
    call_id=CallNode(
        source_location=SourceLocation(
            lineno=3,
            col_offset=0,
            end_lineno=3,
            end_col_offset=9,
            source_code=source_1.id,
        ),
        function_id=LookupNode(
            name="setitem",
        ).id,
        positional_args=[
            call_1.id,
            LiteralNode(
                source_location=SourceLocation(
                    lineno=3,
                    col_offset=3,
                    end_lineno=3,
                    end_col_offset=4,
                    source_code=source_1.id,
                ),
                value=0,
            ).id,
            LiteralNode(
                source_location=SourceLocation(
                    lineno=3,
                    col_offset=8,
                    end_lineno=3,
                    end_col_offset=9,
                    source_code=source_1.id,
                ),
                value=1,
            ).id,
        ],
    ).id,
)
literal_7 = LiteralNode(
    source_location=SourceLocation(
        lineno=4,
        col_offset=4,
        end_lineno=4,
        end_col_offset=5,
        source_code=source_1.id,
    ),
    value=4,
)
call_3 = CallNode(
    source_location=SourceLocation(
        lineno=5,
        col_offset=0,
        end_lineno=5,
        end_col_offset=9,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        mutate_1.id,
        LiteralNode(
            source_location=SourceLocation(
                lineno=5,
                col_offset=3,
                end_lineno=5,
                end_col_offset=4,
                source_code=source_1.id,
            ),
            value=1,
        ).id,
        literal_7.id,
    ],
)
mutate_2 = MutateNode(
    source_id=mutate_1.id,
    call_id=call_3.id,
)
mutate_3 = MutateNode(
    source_id=mutate_2.id,
    call_id=call_3.id,
)
call_5 = CallNode(
    source_location=SourceLocation(
        lineno=6,
        col_offset=10,
        end_lineno=6,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="__build_list__",
    ).id,
    positional_args=[
        LiteralNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=11,
                end_lineno=6,
                end_col_offset=13,
                source_code=source_1.id,
            ),
            value=30,
        ).id
    ],
)
call_6 = CallNode(
    source_location=SourceLocation(
        lineno=6,
        col_offset=0,
        end_lineno=6,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        mutate_3.id,
        CallNode(
            source_location=SourceLocation(
                lineno=6,
                col_offset=3,
                end_lineno=6,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=3,
                        end_lineno=6,
                        end_col_offset=4,
                        source_code=source_1.id,
                    ),
                    value=2,
                ).id,
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=6,
                        col_offset=5,
                        end_lineno=6,
                        end_col_offset=6,
                        source_code=source_1.id,
                    ),
                    value=3,
                ).id,
            ],
        ).id,
        call_5.id,
    ],
)
mutate_4 = MutateNode(
    source_id=mutate_2.id,
    call_id=call_6.id,
)
mutate_5 = MutateNode(
    source_id=mutate_3.id,
    call_id=call_6.id,
)
mutate_6 = MutateNode(
    source_id=mutate_4.id,
    call_id=call_6.id,
)
mutate_7 = MutateNode(
    source_id=mutate_6.id,
    call_id=call_6.id,
)
call_9 = CallNode(
    source_location=SourceLocation(
        lineno=7,
        col_offset=0,
        end_lineno=7,
        end_col_offset=14,
        source_code=source_1.id,
    ),
    function_id=LookupNode(
        name="setitem",
    ).id,
    positional_args=[
        mutate_7.id,
        CallNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=3,
                end_lineno=7,
                end_col_offset=6,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="slice",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=3,
                        end_lineno=7,
                        end_col_offset=4,
                        source_code=source_1.id,
                    ),
                    value=3,
                ).id,
                literal_7.id,
            ],
        ).id,
        CallNode(
            source_location=SourceLocation(
                lineno=7,
                col_offset=10,
                end_lineno=7,
                end_col_offset=14,
                source_code=source_1.id,
            ),
            function_id=LookupNode(
                name="__build_list__",
            ).id,
            positional_args=[
                LiteralNode(
                    source_location=SourceLocation(
                        lineno=7,
                        col_offset=11,
                        end_lineno=7,
                        end_col_offset=13,
                        source_code=source_1.id,
                    ),
                    value=40,
                ).id
            ],
        ).id,
    ],
)
mutate_9 = MutateNode(
    source_id=call_5.id,
    call_id=call_9.id,
)
mutate_10 = MutateNode(
    source_id=mutate_7.id,
    call_id=call_9.id,
)
mutate_13 = MutateNode(
    source_id=MutateNode(
        source_id=MutateNode(
            source_id=mutate_6.id,
            call_id=call_9.id,
        ).id,
        call_id=call_9.id,
    ).id,
    call_id=call_9.id,
)
mutate_14 = MutateNode(
    source_id=MutateNode(
        source_id=mutate_4.id,
        call_id=call_9.id,
    ).id,
    call_id=call_9.id,
)
mutate_15 = MutateNode(
    source_id=mutate_5.id,
    call_id=call_9.id,
)
mutate_16 = MutateNode(
    source_id=mutate_5.id,
    call_id=call_9.id,
)
