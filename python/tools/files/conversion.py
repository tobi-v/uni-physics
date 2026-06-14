def save_pandas_to_latex_table(pd, tex_file, caption="", label="tab:", header=None, max_rows=None):
    if header:
        pd.columns = header

    if max_rows is not None:
        pd = pd.head(max_rows)

    pd.to_latex(
        buf=tex_file,
        index=False,
        float_format='%.3f',
        caption=caption,
        label=label,
        escape=False
    )