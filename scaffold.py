#!/usr/bin/env python3
"""
Project Scaffold Generator - A CLI tool to quickly scaffold new development projects
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import Dict, List


class ProjectScaffold:
    """Main scaffold generator class"""
    
    def __init__(self):
        self.templates = {
            "react": self._react_template,
            "python": self._python_template,
            "node": self._node_template,
            "vanilla": self._vanilla_template,
        }
    
    def create_project(self, project_name: str, template: str, **options):
        """Create a new project from template"""
        if template not in self.templates:
            print(f"Error: Template '{template}' not found")
            print(f"Available templates: {', '.join(self.templates.keys())}")
            sys.exit(1)
        
        project_path = Path(project_name)
        
        if project_path.exists():
            print(f"Error: Directory '{project_name}' already exists")
            sys.exit(1)
        
        print(f"Creating {template} project: {project_name}")
        project_path.mkdir()
        
        # Call the template function
        self.templates[template](project_path, project_name, **options)
        
        print(f"\n✓ Project '{project_name}' created successfully!")
        print(f"  cd {project_name}")
        print(f"  # Add your custom configuration and start coding!")
    
    def _create_common_files(self, project_path: Path, project_name: str):
        """Create common files for all projects"""
        # .gitignore
        gitignore_content = """# Dependencies
node_modules/
__pycache__/
*.py[cod]
*$py.class
venv/
env/
.venv/

# Environment variables
.env
.env.local
.env.*.local

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Build outputs
dist/
build/
*.log
"""
        (project_path / ".gitignore").write_text(gitignore_content)
        
        # README.md
        readme_content = f"""# {project_name}

## Description
Add your project description here.

## Installation
```bash
# Add installation instructions here
```

## Usage
```bash
# Add usage instructions here
```

## Development
```bash
# Add development instructions here
```

## License
MIT
"""
        (project_path / "README.md").write_text(readme_content)
    
    def _react_template(self, project_path: Path, project_name: str, **options):
        """Create React project template"""
        self._create_common_files(project_path, project_name)
        
        # package.json
        package_json = {
            "name": project_name,
            "version": "0.1.0",
            "private": True,
            "dependencies": {
                "react": "^18.2.0",
                "react-dom": "^18.2.0",
                "react-scripts": "5.0.1"
            },
            "scripts": {
                "start": "react-scripts start",
                "build": "react-scripts build",
                "test": "react-scripts test",
                "eject": "react-scripts eject"
            },
            "eslintConfig": {
                "extends": ["react-app"]
            },
            "browserslist": {
                "production": [">0.2%", "not dead", "not op_mini all"],
                "development": ["last 1 chrome version", "last 1 firefox version", "last 1 safari version"]
            }
        }
        (project_path / "package.json").write_text(json.dumps(package_json, indent=2))
        
        # Create src directory
        src_path = project_path / "src"
        src_path.mkdir()
        
        # App.js
        app_js = """import React from 'react';
import './App.css';

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <h1>Welcome to Your React App</h1>
        <p>Start editing to see some magic happen!</p>
      </header>
    </div>
  );
}

export default App;
"""
        (src_path / "App.js").write_text(app_js)
        
        # App.css
        app_css = """.App {
  text-align: center;
}

.App-header {
  background-color: #282c34;
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
}

h1 {
  margin-bottom: 20px;
}
"""
        (src_path / "App.css").write_text(app_css)
        
        # index.js
        index_js = """import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);
"""
        (src_path / "index.js").write_text(index_js)
        
        # index.css
        index_css = """body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen',
    'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue',
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, 'Courier New',
    monospace;
}
"""
        (src_path / "index.css").write_text(index_css)
        
        # public/index.html
        public_path = project_path / "public"
        public_path.mkdir()
        index_html = f"""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta name="description" content="React app" />
    <title>{project_name}</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>
"""
        (public_path / "index.html").write_text(index_html)
    
    def _python_template(self, project_path: Path, project_name: str, **options):
        """Create Python project template"""
        self._create_common_files(project_path, project_name)
        
        # requirements.txt
        requirements = """# Add your dependencies here
# pytest>=7.0.0
# black>=22.0.0
# flake8>=4.0.0
"""
        (project_path / "requirements.txt").write_text(requirements)
        
        # setup.py
        setup_py = f"""from setuptools import setup, find_packages

setup(
    name="{project_name}",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # Add dependencies here
    ],
)
"""
        (project_path / "setup.py").write_text(setup_py)
        
        # Create src directory structure
        src_path = project_path / "src"
        src_path.mkdir()
        (src_path / "__init__.py").write_text("")
        
        # main.py
        main_py = """#!/usr/bin/env python3
\"\"\"
Main entry point for the application.
\"\"\"

def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""
        (src_path / "main.py").write_text(main_py)
        
        # tests directory
        tests_path = project_path / "tests"
        tests_path.mkdir()
        (tests_path / "__init__.py").write_text("")
        (tests_path / "test_main.py").write_text("""import pytest
from src.main import main

def test_main():
    # Add your tests here
    assert True
""")
    
    def _node_template(self, project_path: Path, project_name: str, **options):
        """Create Node.js project template"""
        self._create_common_files(project_path, project_name)
        
        # package.json
        package_json = {
            "name": project_name,
            "version": "1.0.0",
            "description": "",
            "main": "index.js",
            "scripts": {
                "start": "node index.js",
                "dev": "nodemon index.js",
                "test": "jest"
            },
            "keywords": [],
            "author": "",
            "license": "MIT",
            "dependencies": {},
            "devDependencies": {
                "nodemon": "^2.0.20",
                "jest": "^29.0.0"
            }
        }
        (project_path / "package.json").write_text(json.dumps(package_json, indent=2))
        
        # index.js
        index_js = """/**
 * Main entry point for the application
 */

function main() {
    console.log('Hello, World!');
}

main();
"""
        (project_path / "index.js").write_text(index_js)
        
        # Create src directory
        src_path = project_path / "src"
        src_path.mkdir()
        
        # Create tests directory
        tests_path = project_path / "tests"
        tests_path.mkdir()
        (tests_path / "index.test.js").write_text("""const main = require('../index');

test('basic test', () => {
    expect(true).toBe(true);
});
""")
    
    def _vanilla_template(self, project_path: Path, project_name: str, **options):
        """Create vanilla HTML/CSS/JS project template"""
        self._create_common_files(project_path, project_name)
        
        # index.html
        index_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{project_name}</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <h1>Welcome to {project_name}</h1>
    </header>
    <main>
        <p>Start editing to see some magic happen!</p>
    </main>
    <script src="script.js"></script>
</body>
</html>
"""
        (project_path / "index.html").write_text(index_html)
        
        # styles.css
        styles_css = """* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
}

header {
    background-color: #282c34;
    color: white;
    padding: 2rem;
    text-align: center;
}

main {
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
}
"""
        (project_path / "styles.css").write_text(styles_css)
        
        # script.js
        script_js = """// Main JavaScript file
console.log('Welcome to your project!');

// Add your JavaScript code here
"""
        (project_path / "script.js").write_text(script_js)


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Project Scaffold Generator - Create new projects quickly"
    )
    parser.add_argument(
        "project_name",
        nargs="?",
        help="Name of the project to create"
    )
    parser.add_argument(
        "-t", "--template",
        choices=["react", "python", "node", "vanilla"],
        default="vanilla",
        help="Project template to use (default: vanilla)"
    )
    parser.add_argument(
        "--list-templates",
        action="store_true",
        help="List available templates and exit"
    )
    
    args = parser.parse_args()
    
    scaffold = ProjectScaffold()
    
    if args.list_templates:
        print("Available templates:")
        for template in scaffold.templates.keys():
            print(f"  - {template}")
        sys.exit(0)
    
    if not args.project_name:
        parser.error("project_name is required when not using --list-templates")
    
    scaffold.create_project(args.project_name, args.template)


if __name__ == "__main__":
    main()