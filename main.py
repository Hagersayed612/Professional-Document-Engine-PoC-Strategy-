from fastapi import FastAPI, Request, Form
from fastapi.responses import Response, HTMLResponse
from fastapi.templating import Jinja2Templates
from xhtml2pdf import pisa
from datetime import datetime
import io

app = FastAPI()
templates = Jinja2Templates(directory="templates")


 
# =========================

def build_sections_html(form, section_count: int) -> str:
    sections_html = ""

    for i in range(section_count):
        title = form.get(f"section_title_{i}")
        content = form.get(f"section_content_{i}")

        if not title or not content:
            continue

        paragraphs = "".join(
            f"<p>{p}</p>"
            for p in content.split("\n")
            if p.strip()
        )

        sections_html += f"""
            <h3 style="margin-top:20px;color:#1a3a5f;">
                {title}
            </h3>
            {paragraphs}
        """

    return sections_html


def build_document_data(
    *,
    title: str,
    author: str,
    date: str,
    document_type: str,
    executive_summary: str,
    content: str,
    generation_date: str
) -> dict:
    return {
        "title": title,
        "author": author,
        "date": date,
        "document_type": document_type,
        "executive_summary": executive_summary,
        "content": content,
        "generation_date": generation_date,
    }


# =========================
# Routes
# =========================

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


@app.post("/preview", response_class=HTMLResponse)
async def preview(
    request: Request,
    title: str = Form(...),
    author: str = Form(...),
    date: str = Form(...),
    document_type: str = Form(...),
    executive_summary: str = Form(""),
    section_count: int = Form(...)
):
    form = await request.form()

    sections_html = build_sections_html(form, section_count)

    data = build_document_data(
        title=title,
        author=author,
        date=date,
        document_type=document_type,
        executive_summary=executive_summary,
        content=sections_html,
        generation_date="Preview Mode"
    )

    return templates.TemplateResponse(
        "report.html",
        {"request": request, "data": data}
    )


@app.post("/generate-pdf")
async def generate_pdf(
    request: Request,
    title: str = Form(...),
    author: str = Form(...),
    date: str = Form(...),
    document_type: str = Form("Business Report"),
    executive_summary: str = Form(""),
    section_count: int = Form(...)
):
    form = await request.form()

    sections_html = build_sections_html(form, section_count)

    data = build_document_data(
        title=title,
        author=author,
        date=date,
        document_type=document_type,
        executive_summary=executive_summary,
        content=sections_html,
        generation_date=datetime.now().strftime("%Y-%m-%d %H:%M")
    )

    rendered_html = templates.get_template("report.html").render(data=data)

    pdf_buffer = io.BytesIO()
    pisa_status = pisa.CreatePDF(
        io.BytesIO(rendered_html.encode("utf-8")),
        dest=pdf_buffer
    )

    if pisa_status.err:
        return {"error": "PDF generation failed"}

    return Response(
        content=pdf_buffer.getvalue(),
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=report.pdf"
        }
    )
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
