import tablate as tb
from tablate import HtmlContainerStylesInput

tab = tb.Tablate(html_container_styles=HtmlContainerStylesInput(html_container_border_style="thin",
                                                                html_container_padding=20))

table_columns = [
    {
        "key": "col_one",
        "string": "Col One",
        "width": "50%"
    },
    {
        "key": "col_two",
        "string": "Col One",
    },
    {
        "key": "col_three",
        "string": "Col One",
    }
]

table_rows = [
    {
        "col_one": "Column One, Row One",
        "col_two": "Column Two, Row One",
        "col_three": "Column Three, Row One"
    },
    {
        "col_one": "Column One, Row Two",
        "col_two": "Column Two, Row Two",
        "col_three": "Column Three, Row Two"
    },
    {
        "col_one": "Column One, Row Three",
        "col_two": "Column Two, Row Three",
        "col_three": "Column Three, Row Three"
    }
]

tab = tb.Tablate()

tab.add_text_frame("This is an basic example for Tablate usage.")
tab.add_grid_frame(["One", "Two", "Three"])
tab.add_table_frame(columns=table_columns, rows=table_rows)
tab.print()
# or
print(tab.to_html())
tab.list_frames()

some_other_one = tb.Tablate()
some_other_one.add_text_frame("lalala")
some_other_one.add_text_frame("lalala")
some_other_one.add_text_frame("lalala")


tab.replace_frame(1, some_other_one)
tab.list_frames()

print(tab)