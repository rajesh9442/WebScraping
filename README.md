# Web Scraping & Data Processing Strategy

## Exercise 1: Web Scraping Strategy & Implementation

### 1. Approach to Identifying Relevant Websites

- **Source Selection**: Prioritize high-traffic, industry-specific platforms (e.g., LinkedIn for job postings, Bloomberg for market trends, Amazon for product listings).
- **Robots.txt Compliance**: Check robots.txt for scraping permissions and adhere to crawl-delay directives.
- **Rate Limiting Mitigation**:  
  - Use rotating proxies (e.g., BrightData, ProxyMesh) and randomized user agents.  
  - Implement exponential backoff on HTTP 429 responses.  
  - Throttle requests with delays (e.g., 2-5 seconds between requests).

### 2. Handling Challenges

- **Pagination**: Detect "Next" button links or increment page parameters in URLs (e.g., `?page=2`). Track pagination state to avoid infinite loops.
- **Dynamic Content**: Use Selenium or Playwright for JavaScript-rendered content. Alternatively, reverse-engineer internal APIs (e.g., XHR/fetch requests).
- **Anti-Scraping**:  
  - Rotate IPs and user agents.  
  - Mimic human behavior (randomized click intervals, mouse movements).  
  - Use CAPTCHA-solving services (e.g., 2Captcha) if unavoidable.

### 3. Structured Data Model

```json
{
  "id": "sha256_hash(url + title)",
  "source": "website_name",
  "url": "https://example.com/job/123",
  "title": "Senior Data Scientist",
  "description": "Job requirements...",
  "posted_date": "2023-10-01T00:00:00Z",
  "location": "Remote",
  "company": "Tech Corp",
  "salary": "$120k - $150k",
  "metadata": {
    "scraped_at": "2023-10-05T12:34:56Z",
    "tags": ["full-time", "remote"]
  }
}
```

- **Justification**: JSON (stored in MongoDB) accommodates schema flexibility across sources while enabling nested fields (e.g., metadata). A unique id prevents duplicates.

---

### 4. Data Integrity

- **Duplicates**: Hash-based id checks before insertion.  
- **Missing Values**: Flag fields as null or apply default values (e.g., "N/A").  
- **Validation**: Use schema validators (e.g., Cerberus) to enforce data types (e.g., ISO dates).

---

### 5. Tools & Libraries

| Tool       | Justification                                                                 |
|------------|--------------------------------------------------------------------------------|
| Python     | Rich ecosystem (Scrapy, Selenium).                                             |
| Scrapy     | Built-in concurrency, middleware for proxies, and robust pipeline management. |
| Playwright | Headless browser automation with faster JS rendering than Selenium.            |
| MongoDB    | Schema-less storage for heterogeneous data.                                    |
| Redis      | Caching frequently accessed pages to reduce rescraping.                        |


## Exercise 2: Data Processing & Optimization

### 1. Data Preprocessing Workflow

1. **Deduplication**: Remove entries with duplicate id.
2. **Cleaning**:
   - **Text**: Lowercase, remove HTML tags, and standardize whitespace.
   - **Missing Values**: Impute using domain-specific rules (e.g., "Remote" for missing location).
3. **Outlier Handling**: Use IQR/Z-score to detect and cap anomalies (e.g., salaries > $500k).
4. **Standardization**:
   - Convert dates to ISO format.
   - Normalize categorical fields (e.g., "FT" → "Full-Time").

---

### 2. Machine Learning Preparation

- **Text Data**:
  - Tokenization with spaCy.
  - Embeddings via BERT or TF-IDF.
- **Categorical Data**:
  - One-hot encoding for small categories.
  - Embeddings for high cardinality fields.
- **Feature Engineering**: Derive features like `"days_since_posted"`.

---

### 3. Scraper Optimization

- **Concurrency**: Scale with Scrapy’s asynchronous requests or Celery for distributed tasks.
- **Caching**: Use Redis to store HTML responses for 24 hours.
- **APIs**: Switch to official APIs (e.g., LinkedIn API) if available.
- **Monitoring**: Logging and alerts for blocked requests or CAPTCHAs.

---

### 4. Long-Term Efficiency Strategies

- **Parallel Processing**: Deploy scrapers on cloud servers (AWS Lambda, Kubernetes).
- **Incremental Scraping**: Only fetch updated content using Last-Modified headers.
- **Proxies**: Maintain a pool of residential proxies to avoid IP bans.
- **Headless Browsers**: Use Playwright in stealth mode to evade detection.

---

### Final Output

A scalable scraper using **Scrapy/Playwright** stores JSON data in **MongoDB**, with preprocessing for **ML readiness** and optimizations like **proxy rotation** and **caching**.
