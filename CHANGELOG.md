# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2025-04-25

### Added
- New display styles including `code_block`, `quote`, `card`, `notice`, `badge`, `footer`, `data_highlight`, and `section_divider`
- Added specialized styles for different content types: `df`, `table`, `list`, and `dict`
- Global shortcut functions for all styles (e.g., `header()`, `title()`, `success()`)
- Content-specific display shortcuts: `dfd()`, `table()`, `list_()`, and `dict_()`
- Style overloading capabilities through inline style parameters
- Helper dataclasses: `DFDisplayParams` and `TableDisplayParams`

### Changed
- Enhanced visualization with better borders, shadows, and spacing
- Improved color contrast for better accessibility and readability
- Extended style properties for all display formats
- Optimized display behavior with more consistent margins and padding
- Better handling of nested structures in lists and dictionaries

### Improved
- Enhanced example.py with comprehensive demonstrations
- Better documentation with more usage examples
- Graceful fallback behavior outside Jupyter/Colab environments
- More consistent styling between different display functions

## [0.1.0.post1] - 2025-04-22

### Fixed
- Minor fixes and improvements from the initial release

## [0.1.0] - 2023-04-22

### Added
- Initial release with basic display functionality
- Support for styled text display
- Support for table display
- Support for DataFrame display
- Support for list display
- Support for dictionary display
- Default style themes 