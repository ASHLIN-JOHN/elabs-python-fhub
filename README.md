# elabs

A Python module for circuit design, simulation, and visualization. Easily create, connect, and view electronic circuits programmatically.

## Features
- Programmatic circuit creation (battery, bulb, led, resistor, etc.)
- Connect components with simple syntax
- Download files by extension
- View circuits in your browser

## Installation

```bash
pip install elabs
```

## Usage

```python
import elabs
battery = elabs.battery('9v')
bulb = elabs.bulb('minvolt','maxvolt')
circuit = elabs.Circuit()
circuit.add(battery, bulb)
circuit.connect(battery, 'pos', bulb, 'anode')
circuit.show()
```

## Downloading Files

```python
elabs.download_file_by_extension('.', '.txt', 'output.txt')
```

## View on Website

```python
elabs.view_on_website('http://localhost:3001')
```

## License

MIT
