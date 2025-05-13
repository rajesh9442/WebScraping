# Data schema definitions placeholder
item_schema = {
    "id": {"type": "string"},
    "source": {"type": "string"},
    "url": {"type": "string"},
    "title": {"type": "string"},
    "description": {"type": "string"},
    "posted_date": {"type": "string", "regex": r"^\d{4}-\d{2}-\d{2}T.*Z?$"},
    "location": {"type": "string"},
    "company": {"type": "string"},
    "salary": {"type": "string"},
    "metadata": {
        "type": "dict",
        "schema": {
            "scraped_at": {"type": "string"},
            "tags": {"type": "list"}
        }
    }
}
