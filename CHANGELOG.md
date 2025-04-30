# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.4.0] - 2025-05-05

### Added
- Introduced comprehensive animation support throughout the library using Animate.css under the hood
- Support for animation configuration on the run through the string parameter (`animate=None` by default), which processes the string value to follow Animate.css pattern
- Better example.py with enhanced demonstrations showcasing all features

### Improved
- More robust exception handling across all display components
- Better code refactoring resulting in cleaner, more maintainable codebase
- Enhanced function docstrings with more detailed parameter descriptions and usage examples

## [0.3.0] - 2025-04-30

### Added
- Progress bar functionality with full tqdm compatibility
- Support for both determined and undetermined progress states
- New `progress()` function [tqdm-like] for easy progress tracking
- Enhanced exception hierarchy with detailed error context and improved tracebacks
- Advanced ListDisplay capabilities for rendering nested structures, matrices, and array-like objects
- Automatic detection and optimized display for NumPy arrays and Pandas data structures

### Improved
- Comprehensive input validation across all display methods
- Better style override mechanisms with more intuitive syntax
- Consistent error handling throughout the codebase
- Enhanced style inheritance for nested content elements
- More robust color processing and validation

### Changed
- Standardized display behavior across different content types
- Redesigned progress visualization with animations
- Updated all display components to properly propagate and handle exceptions
- Enhanced style definitions with better visual consistency

### Fixed
- Inconsistent error handling in various displayer components
- Improved exception context preservation for better debugging
- Standardized HTML generation and rendering process

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