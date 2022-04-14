from typing import Optional

import pandas as pd

from api.logic.clean_data import get_clean_data, get_month_df
import config

async def monthly_excel(file):
    df = get_clean_data(file)
    month_df = get_month_df(df)
    month_df = month_df.reindex(config.COLUMN_SORT_MONTHLY_EXCEL, axis=1)
    month_df = month_df.sort_values(['User','Type','Price'], ascending=[True, True, False])
    return month_df