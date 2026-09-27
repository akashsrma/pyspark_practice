"""
Topic: 8. String / Date Functions
Dataset: dummy_data.csv (6 employees; note the messy spacing/casing in
         'raw_department' and leading/trailing spaces in 'full_name')

Q1. Clean 'raw_department' into a new column 'clean_department' by trimming
    whitespace and converting to uppercase.
Q2. Trim 'full_name', then split it on the space character into 'first_name'
    and 'last_name' columns (use split() and index into the resulting array).
Q3. Create a column 'employee_tag' that concatenates first_name and city with
    an underscore, using concat_ws('_', ...).
Q4. Convert the string column 'join_date' into an actual DateType column
    'join_date_parsed' using to_date(), then format it as 'dd-MM-yyyy' into a
    column 'join_date_formatted' using date_format().
Q5. Compute the number of days between join_date_parsed and today's date
    using datediff(current_date(), ...), store it in 'days_since_joining'.
"""
