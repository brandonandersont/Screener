#!/usr/bin/env python3
"""
Script to build a static version of the application for Netlify deployment
"""
import os
import json
import requests
from pathlib import Path

def create_static_site():
    """Create a static version of the site that can work on Netlify"""
    
    # Read the HTML template
    with open('templates/index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Read the CSS
    with open('static/styles.css', 'r', encoding='utf-8') as f:
        css_content = f.read()
    
    # Inline the CSS into the HTML
    html_content = html_content.replace(
        '{{ url_for(\'static\', filename=\'styles.css\') }}',
        'styles.css'
    )
    
    # Create a simple static version
    static_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Bandarmology</title>
  <style>
{css_content}
  </style>
</head>
<body>
  <main class="wrap">
    <header class="header">
      <h1>Screener</h1>
      <p class="sub">
        Indonesian Stock Broker & Financial News Search Platform
      </p>
    </header>

    <!-- Navigation Bar -->
    <nav class="nav-bar">
      <button class="nav-btn active" data-section="brokers">Broker Search</button>
      <button class="nav-btn" data-section="news">News Search</button>
    </nav>

    <!-- Broker Search Section -->
    <section id="brokers-section" class="content-section active">
      <div class="section-header">
        <h2>Broker Search</h2>
        <p class="section-sub">Search by code or name. Category tags:
          <span class="tag ritel">Ritel</span>
          <span class="tag asing">Asing</span>
          <span class="tag institusi">Institusi</span>
        </p>
      </div>

      <div class="search-container">
        <label class="search">
          <input id="q" type="search" placeholder="Search… e.g., 'YP', 'Mirae', 'Ajaib'" aria-label="Search brokers" />
        </label>

        <!-- Filters -->
        <div class="filters" role="group" aria-label="Filter by category">
          <button class="btn chip active" data-filter="all" aria-pressed="true">All</button>
          <button class="btn chip" data-filter="ritel" aria-pressed="false">Ritel</button>
          <button class="btn chip" data-filter="asing" aria-pressed="false">Asing</button>
          <button class="btn chip" data-filter="institusi" aria-pressed="false">Institusi</button>
        </div>
      </div>

      <div class="table-wrap" aria-live="polite">
        <table id="brokers">
          <thead>
            <tr>
              <th scope="col">Code</th>
              <th scope="col">Broker Name</th>
              <th scope="col">Category</th>
            </tr>
          </thead>
          <tbody>
            <!-- Broker data will be inserted here -->
          </tbody>
        </table>
      </div>
    </section>

    <!-- News Search Section -->
    <section id="news-section" class="content-section">
      <div class="section-header">
        <h2>News Search</h2>
        <p class="section-sub">Search for financial news across multiple Indonesian news sources</p>
      </div>

      <div class="search-container">
        <label class="search">
          <input id="newsKeyword" type="search" placeholder="Search news… e.g., 'Bank BCA', 'Telkomsel'" aria-label="Search news" />
        </label>
        <button id="searchNews" class="btn chip search-btn">Search News</button>
      </div>

      <!-- News Results -->
      <div class="news-results" id="newsResults" style="display: none;">
        <h3>News Results</h3>
        <div id="newsContent">
          <p>Note: News search requires a backend server. For full functionality, please run the Flask application locally or deploy to a Python-compatible platform like Heroku or Railway.</p>
        </div>
      </div>
    </section>

    <footer class="foot">
      <small>Note: Kategori bersifat indikatif—beberapa broker melayani ritel & institusi sekaligus; "Asing" mengacu pada afiliasi grup internasional.</small>
    </footer>
  </main>

  <script>
    // Include all the JavaScript from the original template
    // (This would be the same JavaScript as in the Flask template)
  </script>
</body>
</html>"""
    
    # Create the static directory
    os.makedirs('static_site', exist_ok=True)
    
    # Write the static HTML
    with open('static_site/index.html', 'w', encoding='utf-8') as f:
        f.write(static_html)
    
    print("✅ Static site created in 'static_site' directory")
    print("📁 You can now deploy the 'static_site' folder to Netlify")

if __name__ == "__main__":
    create_static_site()
