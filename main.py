import os
import datetime

def get_market_analysis():
    # This is the content that will be generated. 
    # In the future, you can hook this up to an AI API.
    date_str = datetime.datetime.now().strftime("%B %d, %Y - %H:%M ET")
    
    markdown_content = f"""
    <div class="briefing">
        <h2>Report: {date_str}</h2>
        <p><strong>Macro Context:</strong> Market is showing resilience ahead of retail data...</p>
        <p><strong>Top Movers:</strong> NVDA (+2.1%) on fresh AI demand; AAPL (-0.5%) on regulatory news.</p>
        <hr>
    </div>
    """
    return markdown_content

def update_html(new_html_snippet):
    # Check if index.html exists, if not create a basic structure
    if not os.path.exists("index.html"):
        with open("index.html", "w") as f:
            f.write('<html><body><h1>📈 Market Rundown Dashboard</h1><div id="content"><!-- INSERT_HERE --></div></body></html>')

    with open("index.html", "r") as f:
        content = f.read()

    # Place the new report at the TOP of the list
    placeholder = "<!-- INSERT_HERE -->"
    if placeholder in content:
        updated_content = content.replace(placeholder, f"{placeholder}\n{new_html_snippet}")
    else:
        # Fallback if placeholder is missing
        updated_content = content + new_html_snippet

    with open("index.html", "w") as f:
        f.write(updated_content)

if __name__ == "__main__":
    report = get_market_analysis()
    update_html(report)
