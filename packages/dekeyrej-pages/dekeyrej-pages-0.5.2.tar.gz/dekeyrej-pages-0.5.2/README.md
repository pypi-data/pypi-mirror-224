# pages latest {version='0.5.2'}
Matrix - serverpage and displaypage classes

**Pages have been split (in __init__.py)**

now requires:
- from pages.displaypage import DisplayPage
- from pages.serverpage import ServerPage

*securedict has been relegated to 'other method'*
- reads encoded secrets from inside kubernetes cluster, or
- reads from JSON file