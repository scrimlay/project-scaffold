# Project Scaffold Generator

A CLI tool to quickly scaffold new development projects with best practices, saving you hours of setup time.

## Features

- 🚀 **Quick Setup**: Create new projects in seconds, not hours
- 📦 **Multiple Templates**: Support for React, Python, Node.js, and Vanilla JS
- 🎯 **Best Practices**: Includes .gitignore, README, and proper project structure
- 🔧 **Extensible**: Easy to add custom templates
- 💡 **Zero Dependencies**: No external dependencies required for basic usage

## Installation

### Option 1: Direct Usage (Recommended for Quick Start)

```bash
# Clone the repository
git clone https://github.com/scrimlay/project-scaffold.git
cd project-scaffold

# Make the script executable (Linux/Mac)
chmod +x scaffold.py

# Run directly
./scaffold.py my-project -t react
```

### Option 2: Install as Python Package

```bash
# Clone the repository
git clone https://github.com/scrimlay/project-scaffold.git
cd project-scaffold

# Install in development mode
pip install -e .

# Now you can use the command anywhere
scaffold my-project -t python
```

## Usage

### Basic Usage

```bash
# Create a vanilla HTML/CSS/JS project
scaffold my-project

# Create a React project
scaffold my-react-app -t react

# Create a Python project
scaffold my-python-app -t python

# Create a Node.js project
scaffold my-node-app -t node
```

### List Available Templates

```bash
scaffold --list-templates
```

### Available Templates

| Template | Description | Best For |
|----------|-------------|----------|
| `vanilla` | HTML, CSS, JavaScript | Simple websites, learning |
| `react` | React with CRA structure | SPAs, web applications |
| `python` | Python with src/tests structure | Scripts, APIs, data science |
| `node` | Node.js with Express-ready structure | Backend services, APIs |

## Project Structure

Each generated project includes:

```
my-project/
├── .gitignore          # Standard ignore patterns
├── README.md           # Project documentation
├── [template files]    # Template-specific files
└── [src/ or similar]   # Source code directory
```

### React Template Structure

```
my-react-app/
├── public/
│   └── index.html
├── src/
│   ├── App.js
│   ├── App.css
│   ├── index.js
│   └── index.css
├── package.json
├── .gitignore
└── README.md
```

### Python Template Structure

```
my-python-app/
├── src/
│   ├── __init__.py
│   └── main.py
├── tests/
│   ├── __init__.py
│   └── test_main.py
├── requirements.txt
├── setup.py
├── .gitignore
└── README.md
```

### Node.js Template Structure

```
my-node-app/
├── src/
├── tests/
│   └── index.test.js
├── index.js
├── package.json
├── .gitignore
└── README.md
```

### Vanilla Template Structure

```
my-vanilla-app/
├── index.html
├── styles.css
├── script.js
├── .gitignore
└── README.md
```

## Examples

### Creating a React Project

```bash
scaffold my-react-app -t react
cd my-react-app
npm install
npm start
```

### Creating a Python Project

```bash
scaffold my-python-app -t python
cd my-python-app
pip install -r requirements.txt
python src/main.py
```

### Creating a Node.js Project

```bash
scaffold my-node-app -t node
cd my-node-app
npm install
npm start
```

## Customization

### Adding Custom Templates

You can easily add custom templates by modifying the `scaffold.py` file:

1. Add your template function to the `ProjectScaffold` class
2. Register it in the `self.templates` dictionary
3. Add it to the choices in the argument parser

Example:

```python
def _my_custom_template(self, project_path: Path, project_name: str, **options):
    """Create custom project template"""
    self._create_common_files(project_path, project_name)
    # Add your custom files here
    (project_path / "custom_file.txt").write_text("Custom content")

# In __init__:
self.templates = {
    # ... existing templates ...
    "custom": self._my_custom_template,
}
```

## Best Practices Included

- **.gitignore**: Pre-configured for common development files
- **README.md**: Template with standard sections
- **Project Structure**: Follows industry best practices
- **Security**: Environment variables excluded from version control

## Development

### Running Tests

```bash
# Test the tool
python3 scaffold.py test-project -t react

# Clean up
rm -rf test-project
```

### Adding New Features

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License.

## Author

Created by scrimlay as a practical developer tool for everyday use.

## Why This Tool?

As a developer, I found myself repeatedly setting up the same project structure. This tool saves time and ensures consistency across projects. It's especially useful for:

- Students starting new assignments
- Developers prototyping ideas quickly
- Teams maintaining consistent project structures
- Anyone who wants to skip the setup phase and start coding

## Future Enhancements

- [ ] Add more templates (Vue, Angular, Django, Flask, etc.)
- [ ] Interactive template customization
- [ ] Template configuration files
- [ ] Integration with package managers
- [ ] Project initialization with git
- [ ] CI/CD configuration generation
