import datetime
import os

def get_market_data():
    # In a real scenario, use APIs like NewsAPI, Finnhub, or AlphaVantage
    # For this example, we return a placeholder representing the logic
    return "Market Rundown Content for " + datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

def update_dashboard(markdown_content):
    now = datetime.datetime.now().strftime("%B %d, %Y - %H:%M")
    html_snippet = f"""
    <div class="entry">
        <h2>Report: {now}</h2>
        <div class="content">
            {markdown_content.replace('\\n', '<br>')}
        </div>
    </div>
    <hr>
    """
    
    # Read existing content and prepend the new entry
    if os.path.exists("index.html"):
        with open("index.html", "r") as f:
            old_content = f.read()
    else:
        old_content = "<html><body><h1>Market Archive</h1></body></html>"
        
    new_html = old_content.replace("<h1>Market Archive</h1>", f"<h1>Market Archive</h1>\\n{html_snippet}")
    
    with open("index.html", "w") as f:
        f.write(new_html)

if __name__ == "__main__":
    report = get_market_data()
    update_dashboard(report)
