# Generate python_book_table.html

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="Books CSV to HTML Table",
        description="Turn a pipe delimited CSV into an HTML table.",
    )

    parser.add_argument("input_file")
    parser.add_argument("output_file")
    args = parser.parse_args()

    csv_data = []
    with open(args.input_file, "r") as f:
        csv_data = f.readlines()

    html_header = """<!doctype html>
<html lang="en-US" class="dark" data-bs-theme="dark">

<head>
  <meta charset="uft-8" />
  <meta name="viewport" content="width=device-width" />

  <!-- Uses https://datatables.net/ and https://getbootstrap.com/docs/5.0/content/tables/ -->

  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.3/css/bootstrap.min.css" />
  <link rel="stylesheet" href="https://cdn.datatables.net/2.3.4/css/dataTables.bootstrap5.css" />
  <link rel="stylesheet" href="https://cdn.datatables.net/responsive/3.0.7/css/responsive.bootstrap5.css" />
  <link rel="stylesheet" href="https://cdn.datatables.net/columncontrol/1.1.0/css/columnControl.dataTables.min.css" />
  <link rel="stylesheet" href="styles/style.css" />
  
  <script src="https://code.jquery.com/jquery-3.7.1.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/5.3.3/js/bootstrap.bundle.min.js"></script>
  <script src="https://cdn.datatables.net/2.3.4/js/dataTables.js"></script>
  <script src="https://cdn.datatables.net/2.3.4/js/dataTables.bootstrap5.js"></script>
  <script src="https://cdn.datatables.net/responsive/3.0.7/js/dataTables.responsive.js"></script>
  <script src="https://cdn.datatables.net/responsive/3.0.7/js/responsive.bootstrap5.js"></script>
  <script src="https://cdn.datatables.net/columncontrol/1.1.0/js/dataTables.columnControl.min.js"></script>
  
  <title>David Freitag's Book List</title>

</head>
<body>
  <h1>David Freitag's Book List</h1>
  <p>These are books I have read, started to read, or want to read.</p>
  <p>I started keeping this list in "real time" in 2025, so books read before 2025 have a year of "NULL."<p>

  <div class="table-responsive">
  <table id="myTable" class="table table-striped table-hover table-bordered">
"""
    # create table row header
    # add row number column
    html_table_header_row = """    <thead>
    <tr>"""
    schema_cols = csv_data[0][:-1].split(sep="|") # drop the '\n' at the end of each line
    schema_cols.insert(0, '#') # add row number column
    for col in schema_cols:
        html_table_header_row += f"\n      <th>{col}</th>"
    html_table_header_row += """\n    </tr>
    </thead>"""

    # create remaining rows
    row_number = 1
    all_html_table_rows = "\n    <tbody>"
    for row in csv_data[1:]:
        html_table_data_row = "\n    <tr>"
        data = row[:-1].split(sep="|") # drop the '\n' at the end of each line
        data.insert(0, row_number) # add row number
        temp_col_counter = 1
        for col in data:
            if temp_col_counter == 2: # italicize the book title in the "Title" column
                html_table_data_row += f"""\n      <td><i><a href="https://www.amazon.com/s?k={col.replace(' ', '+')}" target="_new">{col}</a></i></td>"""
            else:
                html_table_data_row += f"\n      <td>{col}</td>"
            temp_col_counter += 1
        html_table_data_row += "\n    </tr>"
        all_html_table_rows += html_table_data_row
        row_number += 1
    all_html_table_rows += "\n    </tbody>"

    html_footer = """
  </table>
  </div>
<script src="scripts/main.js"></script>
</body>
</html>"""

    full_html = html_header + html_table_header_row + all_html_table_rows + html_footer

    with open(args.output_file, "w") as f:
        f.write(full_html)


if __name__ == "__main__":
    main()
