# PHP API & Frontend Example

## Structure
- backend/api.php: Simple PHP API endpoint
- backend/setup.sql: MySQL setup script
- frontend/index.php: Frontend PHP page fetching API data

## Setup
1. Import backend/setup.sql into your MySQL server.
2. Update backend/api.php with your MySQL credentials if needed.
3. Serve both backend and frontend folders with a PHP server (e.g., XAMPP, WAMP).
4. Open frontend/index.php in your browser.

## Notes
- API returns JSON list of items from MySQL.
- Frontend fetches and displays items using JavaScript.
