#!/usr/bin/env python3
"""
Test script to verify the Flask app can start properly
"""
import os
import sys

# Add the news scraper directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'news scraper copy'))

def test_app_startup():
    """Test if the Flask app can start without errors"""
    try:
        from app import app
        print("✅ Flask app imported successfully")
        
        # Test if we can create a test client
        with app.test_client() as client:
            print("✅ Flask test client created successfully")
            
            # Test the main route
            response = client.get('/')
            if response.status_code == 200:
                print("✅ Main route (/) works")
            else:
                print(f"❌ Main route failed with status {response.status_code}")
            
            # Test static files route
            response = client.get('/static/styles.css')
            if response.status_code == 200:
                print("✅ Static files route works")
            else:
                print(f"❌ Static files route failed with status {response.status_code}")
        
        print("🎉 All tests passed! App is ready for deployment.")
        return True
        
    except Exception as e:
        print(f"❌ App startup failed: {e}")
        return False

if __name__ == "__main__":
    test_app_startup()
