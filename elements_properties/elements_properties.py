# Import required libraries
import ifcopenshell
import json

# Import model
model = ifcopenshell.open('/app/sherier_place_arch.ifc')

# Initialize data dictionary
data = {}

# Extract building elements and their properties
elements = model.by_type("IfcBuildingElement")

data['building_elements'] = []

for element in elements:
    element_data = {
        "type": element.is_a(),
        "name": element.Name,
        "global_id": element.GlobalId,
        "properties": {}
    }
    if element.IsDefinedBy:
        for definition in element.IsDefinedBy:
            if hasattr(definition, 'RelatingPropertyDefinition'):
                property_set = definition.RelatingPropertyDefinition
                if hasattr(property_set, 'HasProperties'):
                    for prop in property_set.HasProperties:
                        if hasattr(prop, 'Name') and hasattr(prop, 'NominalValue'):
                            element_data["properties"][prop.Name] = str(prop.NominalValue)
    data['building_elements'].append(element_data)

# Perform simple analysis - 
# Calculate total area of all walls
total_wall_area = 0.0
walls = model.by_type("IfcWall")
for wall in walls:
    if wall.IsDefinedBy:
        for definition in wall.IsDefinedBy:
            if hasattr(definition, 'RelatingPropertyDefinition'):
                property_set = definition.RelatingPropertyDefinition
                if hasattr(property_set, 'HasProperties'):
                    for prop in property_set.HasProperties:
                        if prop.Name == "Area" and hasattr(prop, 'NominalValue'):
                            total_wall_area += float(prop.NominalValue.wrappedValue)

data['total_wall_area'] = total_wall_area

# Count total number of elements
data['total number of elements'] = len(elements)

# Count total number of doors and windows
doors = model.by_type("IfcDoor")
windows = model.by_type("IfcWindow")
data['door_count'] = len(doors)
data['window_count'] = len(windows)

# Save data to JSON file
output_path = "ifc_elements_properties.json"
with open(output_path, "w") as json_file:
    json.dump(data, json_file, indent=4)

print(f"Data has been successfully processed and saved to {output_path}")

