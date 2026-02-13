"""
elabs Python module for circuit design and visualization.

Example usage:
    import elabs
    battery = elabs.battery('9v')
    bulb = elabs.bulb('minvolt','maxvolt')
    circuit = elabs.Circuit()
    circuit.add(battery, bulb)
    circuit.connect(battery, 'pos', bulb, 'anode')
    circuit.show()
"""


import webbrowser
import os
import urllib.request
from typing import Dict, List, Any, Optional

# Utility function to download a file by extension
def download_file_by_extension(directory: str, extension: str, output_path: str):
    """
    Download the first file found in the directory with the given extension and save to output_path.
    Returns True if successful, False otherwise.
    """
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(extension):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'rb') as src, open(output_path, 'wb') as dst:
                        dst.write(src.read())
                    return True
                except Exception:
                    return False
    return False

# Utility function to view a file or circuit on a website
def view_on_website(url: str):
    """
    Redirects the user to the given website URL in their default browser.
    """
    webbrowser.open(url)

# Base component class
class Component:
    def __init__(self, comp_type: str, properties: Dict[str, Any], position: Optional[Dict[str, int]] = None, rotation: int = 0):
        self.id = f"{comp_type}{id(self)}"
        self.type = comp_type
        self.position = position or {"x": 0, "y": 0}
        self.rotation = rotation
        self.properties = properties
        self.connections = []

# Component factory functions
def battery(voltage: str):
    return Component("battery", {"voltage": voltage})

def bulb(minvolt: str, maxvolt: str):
    return Component("bulb", {"minvolt": minvolt, "maxvolt": maxvolt})

def led(color: str = "red"):
    return Component("led", {"color": color})

def resistor(resistance: str):
    return Component("resistor", {"resistance": resistance})

def switch(closed: bool = False):
    return Component("switch", {"closed": closed})

def buzzer(frequency: str = "1000"):
    return Component("buzzer", {"frequency": frequency})

def arduino(code: str = "", isRunning: bool = False):
    return Component("arduino-uno", {"code": code, "isRunning": isRunning})

def capacitor(capacitance: str):
    return Component("capacitor", {"capacitance": capacitance})

def potentiometer(resistance: str):
    return Component("potentiometer", {"resistance": resistance})

def relay():
    return Component("relay", {})

def inductor(inductance: str):
    return Component("inductor", {"inductance": inductance})

def transistor(type_: str = "NPN", gain: str = "100"):
    return Component("transistor-npn", {"type": type_, "gain": gain})

# Add more as needed...

class Wire:
    def __init__(self, from_comp: Component, from_term: str, to_comp: Component, to_term: str, color: str = "red"):
        self.id = f"w{from_comp.id}_{to_comp.id}"
        self.fromComponentId = from_comp.id
        self.fromTerminal = from_term
        self.toComponentId = to_comp.id
        self.toTerminal = to_term
        self.color = color
        self.points = []
        self.isComplete = True

class Circuit:
    def __init__(self):
        self.components: List[Component] = []
        self.wires: List[Wire] = []

    def add(self, *comps):
        for comp in comps:
            self.components.append(comp)

    def connect(self, from_comp: Component, from_term: str, to_comp: Component, to_term: str, color: str = "red"):
        wire = Wire(from_comp, from_term, to_comp, to_term, color)
        self.wires.append(wire)

    def to_dict(self):
        return {
            "components": [self._component_dict(c) for c in self.components],
            "wires": [vars(w) for w in self.wires]
        }

    def _component_dict(self, c: Component):
        return {
            "id": c.id,
            "type": c.type,
            "position": c.position,
            "rotation": c.rotation,
            "properties": c.properties,
            "connections": c.connections
        }

    def show(self, frontend_url: str = "http://localhost:3001"):
        # For now, just open the frontend
        webbrowser.open(frontend_url)

# Example usage:
# import elabs
# battery = elabs.battery('9v')
# bulb = elabs.bulb('1.5v','3v')
# circuit = elabs.Circuit()
# circuit.add(battery, bulb)
# circuit.connect(battery, 'pos', bulb, 'anode')
# circuit.show()
