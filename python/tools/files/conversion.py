def save_pandas_to_latex_table(pd, tex_file, caption="", label="tab:", header=None):
    if header:
        pd.columns = header

    pd.to_latex(
        buf=tex_file,
        index=False,
        float_format='%.3f',
        caption=caption,
        label=label,
        escape=False
    )