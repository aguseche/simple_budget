from typing import Optional
from fastapi import APIRouter, BackgroundTasks, UploadFile, File
from fastapi.responses import FileResponse
import pandas as pd
from fastapi.responses import StreamingResponse
import io

from api.logic import generator_excel
router = APIRouter()
    
@router.post("/monthly-excel")
async def monthly_excel(file: UploadFile = File(...)):

    df = await generator_excel.monthly_excel(file.file)
    print(df)
    stream = io.StringIO()

    df.to_csv(stream, index = False)

    response = StreamingResponse(iter([stream.getvalue()]),
                        media_type="xls/xlsx"
    )

    response.headers["Content-Disposition"] = "attachment; filename=budget.xls"

    return response